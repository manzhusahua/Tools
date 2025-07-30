import re

def transform_text_batch(texts):
    transformed = []

    for text in texts:
        add_tags = ''
        # 查找英文单词（逗号或引号前的）
        word = list(set(re.findall( r'[a-zA-Z]+', text)))
        # 替换英文单词为 <lang> 标签形式（不保留引号）
        for line in re.findall( r'[a-zA-Z]+', text):
            add_tags = re.sub(r'([a-zA-Z&;]+)', r"<lang xml:lang='en-US'>\1</lang>", text).replace("</lang>'<lang xml:lang='en-US'>","'")


        # 查找所有音标对（/.../ 漏读了 或 /.../ 发成了 /.../）
        ipa_pairs = re.findall(r'/([^/]+)/\s*(漏读了|发成了)\s*(?:/([^/]+)/)?', text)
        # ipa_pairs = re.findall(r'/([^/]+)([^/]+)/)?', text)
        # ipa_pairs = list(set([x.replace('/','') for x in re.findall(r'/[^/]+/', text)])) 
        # print(ipa_pairs)
        print(ipa_pairs)
        for ipa_from, action, ipa_to in ipa_pairs:
            print(ipa_from)
            print(action)
            print(ipa_to)
            # 构造带 phoneme 标签的音标
            annotated_ipa_from = f"<lang xml:lang='en-US'><phoneme alphabet=\"ipa\" ph=\"{ipa_from}\">/{ipa_from}/</phoneme></lang>"
            text = re.sub(f"/{re.escape(ipa_from)}/", annotated_ipa_from, text)

            if ipa_to:
                print("text:",text)
                annotated_ipa_to = f"<lang xml:lang='en-US'><phoneme alphabet=\"ipa\" ph=\"{ipa_to}\">/{ipa_to}/</phoneme></lang>"
                text = re.sub(f"/{re.escape(ipa_to)}/", annotated_ipa_to, text)

        transformed.append(text)

    return transformed

# 示例文本列表
texts = [
    # '整体读得不错，表现很好。单词"doctor"中， /ə/ 漏读了， /t/ 发成了 /ɡ/ 。',
    # '单词"we\'re"中， /ɪə/ 发成了 /iːə/',
    # '单词"they\'re"中， /eə/ 发成了 /ɛə/',
    '单词"you\'re"中， /ʊə/ 发成了 /uːə/',
    # '/t/,/t/,/t/,单词want的/t/发音不够清晰。',
    # '单词"bird"中， /ɜː/ 漏读了。',
    # '/ɜː/'
]

# 批量处理
results = transform_text_batch(texts)

# 输出结果
for r in results:
    print(r)

