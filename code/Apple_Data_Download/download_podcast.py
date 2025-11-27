#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys
import json
import time
import math
import shutil
import urllib.parse
from datetime import datetime
from typing import List, Dict, Optional

try:
    import requests
except ImportError:
    print("需要安装 requests：pip install requests")
    sys.exit(1)

LOOKUP_BASE = "https://itunes.apple.com/lookup"

# —— 新增：全局会话与默认请求头（复用连接，减少 TLS 握手） —— #
SESSION = requests.Session()
DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/119.0 Safari/537.36 PythonDownloader/1.0"
    ),
    "Accept": "*/*",
    "Connection": "keep-alive",
}


def get_feed_url(itunes_id: str, country: str = "jp") -> Dict[str, str]:
    # 用 iTunes Lookup API 获取 feedUrl 和节目元数据
    params = {"id": itunes_id, "country": country}
    r = SESSION.get(LOOKUP_BASE, params=params, timeout=(10, 30), headers=DEFAULT_HEADERS)
    r.raise_for_status()
    data = r.json()
    if data.get("resultCount", 0) < 1:
        raise RuntimeError(f"未找到节目（id={itunes_id}, country={country}）")
    result = data["results"][0]
    feed_url = result.get("feedUrl")
    collection_name = result.get("collectionName", f"podcast_{itunes_id}")
    artist_name = result.get("artistName", "")
    if not feed_url:
        raise RuntimeError("该节目未公开 RSS（feedUrl 为空），无法批量下载。")
    return {"feed_url": feed_url, "title": collection_name, "artist": artist_name}


def sanitize_filename(name: str) -> str:
    name = re.sub(r'[\/:*?"<>|]+', "_", name).strip()
    name = re.sub(r'\s+', ' ', name)
    return name[:240]  # 避免过长路径


def human_size(n: Optional[int]) -> str:
    if not n or n < 0:
        return "unknown"
    units = ["B", "KB", "MB", "GB", "TB"]
    i = 0
    while n >= 1024 and i < len(units) - 1:
        n /= 1024.0
        i += 1
    return f"{n:.2f} {units[i]}"


# —— 增强：更稳健的网络请求封装 —— #

def safe_request(url: str, method: str = "GET", max_retries: int = 4, timeout=(10, 90), **kwargs):
    # 更强的网络请求封装：读超时/429/5xx/连接错误均重试，指数退避
    delay = 2.0
    for attempt in range(1, max_retries + 1):
        try:
            headers = kwargs.pop("headers", {})
            merged_headers = {**DEFAULT_HEADERS, **headers}
            resp = SESSION.request(method, url, headers=merged_headers, timeout=timeout, **kwargs)
            if resp.status_code in (429, 500, 502, 503, 504):
                raise requests.RequestException(f"HTTP {resp.status_code}")
            return resp
        except (requests.ReadTimeout, requests.ConnectTimeout, requests.ConnectionError, requests.RequestException):
            if attempt >= max_retries:
                raise
            time.sleep(delay)
            delay = min(delay * 2, 20.0)  # 指数退避
        except Exception:
            raise


def _probe_head(url: str) -> dict:
    # HEAD 探测：尽量拿到长度与是否支持 Range
    info = {"content_length": None, "accept_ranges": False}
    try:
        hr = safe_request(url, method="HEAD", timeout=(10, 30))
        cl = hr.headers.get("Content-Length")
        if cl and cl.isdigit():
            info["content_length"] = int(cl)
        ar = hr.headers.get("Accept-Ranges", "")
        info["accept_ranges"] = ("bytes" in ar.lower())
    except Exception:
        pass
    return info


def parse_rss(feed_url: str) -> List[Dict[str, str]]:
    # 解析 RSS：返回 [{title, audio_url, pub_date}] 列表
    resp = safe_request(feed_url)
    resp.raise_for_status()
    xml = resp.text

    import xml.etree.ElementTree as ET
    root = ET.fromstring(xml)

    items = []
    for item in root.findall("./channel/item"):
        title_el = item.find("title")
        pub_el = item.find("pubDate")
        enc_el = item.find("enclosure")
        audio_url = enc_el.get("url") if enc_el is not None else None
        if not audio_url:
            link_el = item.find("link")
            audio_url = link_el.text if link_el is not None else None

        title = title_el.text.strip() if title_el is not None and title_el.text else "untitled"
        pub_date = pub_el.text.strip() if pub_el is not None and pub_el.text else ""
        items.append({
            "title": title,
            "audio_url": audio_url,
            "pub_date": pub_date
        })
    return items


# —— 增强：支持断点续传、长读超时与稳定进度 —— #

def download_file(url: str, dest_path: str) -> None:
    # 断点续传（Range）+ 更长超时 + 稳定进度输出
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    temp_path = dest_path + ".part"

    probe = _probe_head(url)
    total_size = probe["content_length"]
    accept_ranges = probe["accept_ranges"]

    headers = {}
    existing = 0
    if os.path.exists(temp_path):
        existing = os.path.getsize(temp_path)
        if accept_ranges and existing > 0:
            headers["Range"] = f"bytes={existing}-"

    with safe_request(url, headers=headers, stream=True, timeout=(10, 120)) as r:
        mode = "ab" if headers.get("Range") and r.status_code == 206 else "wb"
        if r.status_code == 206:
            cr = r.headers.get("Content-Range", "")
            try:
                total_size = int(cr.split("/")[-1])
            except Exception:
                total_size = existing + int(r.headers.get("Content-Length", "0") or 0)
        else:
            total_size = int(r.headers.get("Content-Length", "0") or 0)

        chunk = 1024 * 512  # 512KB
        downloaded = existing
        last_log = time.time()

        with open(temp_path, mode) as f:
            for chunk_bytes in r.iter_content(chunk_size=chunk):
                if not chunk_bytes:
                    continue
                f.write(chunk_bytes)
                downloaded += len(chunk_bytes)

                now = time.time()
                if now - last_log >= 0.5:
                    if total_size > 0:
                        pct = downloaded / total_size * 100
                        sys.stdout.write(f"[{os.path.basename(dest_path)}] {pct:5.1f}% "f"({human_size(downloaded)}/{human_size(total_size)})")
                    else:
                        sys.stdout.write(f"[{os.path.basename(dest_path)}] {human_size(downloaded)} downloaded")
                    sys.stdout.flush()
                    last_log = now
            print()

    shutil.move(temp_path, dest_path)


def pick_audio_extension(url: str) -> str:
    path = urllib.parse.urlparse(url).path
    ext = os.path.splitext(path)[1].lower()
    if ext in [".mp3", ".m4a", ".aac", ".wav", ".flac", ".ogg"]:
        return ext
    return ".m4a"  # 常见 Apple 播客音频容器


def within_range(pub_date_str: str, start: Optional[str], end: Optional[str]) -> bool:
    if not (start or end):
        return True
    try:
        # RFC822 时间格式，如：Mon, 19 Jun 2023 08:00:00 +0900
        dt = datetime.strptime(pub_date_str, "%a, %d %b %Y %H:%M:%S %z")
    except Exception:
        return True  # 无法解析则不过滤
    if start:
        s = datetime.fromisoformat(start)
        if dt.replace(tzinfo=None) < s:
            return False
    if end:
        e = datetime.fromisoformat(end)
        if dt.replace(tzinfo=None) > e:
            return False
    return True


def main(out_pat):
    # 命令行示例：
    # python download_podcast.py --id 1794070876 --country jp --limit 0 --start 2025-01-01 --end 2025-12-31
    import argparse
    ap = argparse.ArgumentParser(description="Batch download Apple Podcasts by iTunes ID")
    ap.add_argument("--id", required=True, help="iTunes/Apple Podcasts 节目 ID（例如 1794070876）")
    ap.add_argument("--country", default="jp", help="国家/地区代码（默认 jp）")
    ap.add_argument("--limit", type=int, default=0, help="最多下载 N 条；0 表示全部")
    ap.add_argument("--start", default=None, help="开始日期（YYYY-MM-DD，可选）")
    ap.add_argument("--end", default=None, help="结束日期（YYYY-MM-DD，可选）")
    ap.add_argument("--out", default="downloads", help="输出根目录（默认 downloads）")
    args = ap.parse_args()

    meta = get_feed_url(args.id, args.country)
    feed_url = meta["feed_url"]
    title = sanitize_filename(meta["title"])
    print(f"节目：{meta['title']}（艺术家：{meta['artist']}）")
    print(f"RSS：{feed_url}")

    items = parse_rss(feed_url)
    if not items:
        print("RSS 中未找到条目。")
        return

    out_dir = os.path.join(args.out, title)
    os.makedirs(out_dir, exist_ok=True)

    count = 0
    for i, it in enumerate(items, start=1):
        audio_url = it.get("audio_url")
        if not audio_url:
            print(f"[跳过] 无音频链接：{it.get('title')}")
            continue
        if not within_range(it.get("pub_date", ""), args.start, args.end):
            continue

        ext = pick_audio_extension(audio_url)
        fname = sanitize_filename(f"{i:03d} - {it.get('title','untitled')}{ext}")
        dest = os.path.join(out_dir, fname)
        if os.path.exists(dest):
            print(f"[已存在] {fname}")
        else:
            print(f"[下载] {fname}")
            try:
                download_file(audio_url, dest)
            except Exception as e:
                print(f"[失败] {fname}: {e}")

        count += 1
        if args.limit > 0 and count >= args.limit:
            break

    print(f"完成：下载 {count} 个文件，存放于 {out_dir}")


if __name__ == "__main__":
    main()
    # python download_podcast.py --id 1618409086 --country jp
