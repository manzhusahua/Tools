import re


def clean(desstr, restr=""):
    # 过滤表情
    try:
        co = re.compile(
            "[" "\U0001F300-\U0001F64F" "\U0001F680-\U0001F6FF" "\u2600-\u2B55]+"
        )
    except re.error:
        co = re.compile(
            "("
            "\ud83c[\udf00-\udfff]|"
            "\ud83d[\udc00-\ude4f\ude80-\udeff]|"
            "[\u2600-\u2B55])+"
        )
    return co.sub(restr, desstr)


if __name__ == "__main__":
    # files_name = r"D:\users\v-zhazhai\TTS\zh-CN\20240229\output_chat_2\xlsx_all_split_30s\5.txt"
    # with open(files_name,'r',encoding='utf8') as f,open(files_name.replace(".txt","_clean.txt"),'w',encoding='utf8') as s:
    #     for line in f.readlines():
    #         line = clean(line)
    #         s.writelines(line)
    word = "s1afsvsdc"
    print(re.findall("s^[0-9]*$", word))
