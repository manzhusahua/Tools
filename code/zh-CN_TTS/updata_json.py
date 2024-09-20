"""
用于更新json files
"""

import json


def get_updata_json(dataset, tyleanme, tyle):
    value = {
        "Speaker": "ZhCN{}".format(dataset),
        "Gender": "Female",
        "ForceAlign": "\\stcvm-862\TTSData\zh-CN\Voices\{}\CNV\{}\Alignment".format(
            dataset, tyleanme
        ),
        "XmlScripts": "\\stcvm-862\TTSData\zh-CN\Voices\{}\CNV\{}\XmlScripts".format(
            dataset, tyleanme
        ),
        "Wave24kNormalized": "\\stcvm-862\TTSData\zh-CN\Voices\{}\CNV\{}\Speech\Wave24kNormalized".format(
            dataset, tyleanme
        ),
        "Wave48kNormalized": "\\stcvm-862\TTSData\zh-CN\Voices\{}\CNV\{}\Speech\Wave48kNormalized".format(
            dataset, tyleanme
        ),
        "TextScript": "\\stcvm-862\TTSData\zh-CN\Voices\{}\CNV\{}\TextScripts".format(
            dataset, tyleanme
        ),
        "Wave48k": "\\stcvm-862\TTSData\zh-CN\Voices\{}\CNV\{}\Speech\Wave48k".format(
            dataset, tyleanme
        ),
        "tyle": list({"{}".format(tyle)}),
    }
    # print(value)
    return value


if __name__ == "__main__":

    with open(r"C:\Users\v-zhazhai\Downloads\test.json", "a", encoding="utf8") as s:
        word = [
            "AlertnessResponse",
            "Birthdaysong",
            "CarControl",
            "CharacteristicVocabulary",
            "Encyclopedia",
            "Mixlingual",
            "Multimedia",
            "Navigation",
            "RechargeReplace",
            "Speech",
            "Weather",
            "Word",
        ]
        for line in word:
            value = get_updata_json(
                "ZhCNF138",
                line,
                '"{}": []'.format(line),
            )
            json.dump(value, s, indent=4)
        # print(value)
