
import json
import re

def parse_int_from_str(s: str) -> int:
    # 去掉千位分隔逗号，并确保仅数字与小数点
    clean = s.replace(",", "").strip()
    # 有些表可能是浮点，统一转为 int（你的示例为整数小时）
    return int(float(clean))

def parse_line_to_obj(row: dict) -> (str, dict):
    # 组合键
    key = f"{row['Locale'].strip()} {row['Dataset names'].strip()}"
    obj = {
        "Description": row["Description"].strip(),
        "Raw data amount(hours)": parse_int_from_str(row["Raw data amount(hours)"]),
        "V3 chunk data amount(hours)": parse_int_from_str(row["V3 chunk data amount(hours)"]),
        "Valid data amount in V3(hours)": parse_int_from_str(row["Valid data amount in V3(hours)"]),
        "Valid data ratio": row["Valid data ratio"].strip(),
        "File List": row["File List"].strip(),
        "Yaml List": row["Yaml List"].strip(),
        "Statistics result path": row["Statistics result path"].strip(),
        "Data processed result path": row["Data processed result path"].strip(),
        "Data process job": row["Data process job"].strip(),
    }
    return key, obj

def load_tsv(path: str) -> list:
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    headers = [h.strip() for h in lines[0].split("\t")]
    for line in lines[1:]:
        if not line.strip():
            continue
        cols = [c.strip() for c in line.split("\t")]
        # 若行中包含内嵌制表符或列数不齐，可以做简单修正
        if len(cols) < len(headers):
            # 尝试将尾部以空格拼接（根据具体数据调整）
            cols += [""] * (len(headers) - len(cols))
        row = {h: (cols[i] if i < len(cols) else "") for i, h in enumerate(headers)}
        rows.append(row)
    return rows

def convert_tsv_to_json(input_path: str, output_path: str):
    data = {}
    for row in load_tsv(input_path):
        key, obj = parse_line_to_obj(row)
        data[key] = obj
    with open(output_path, "w", encoding="utf-8") as out:
        json.dump(data, out, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    # 把你的表格内容（包含表头）保存为 input.tsv，然后运行
    convert_tsv_to_json(r"C:\Users\v-zhazhai\Desktop\input.tsv", r"C:\Users\v-zhazhai\Desktop\input.json")
   
