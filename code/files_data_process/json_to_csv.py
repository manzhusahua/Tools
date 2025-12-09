
import json
import csv
import pandas as pd

# 原始 JSON 数据
with open(r"C:\Users\v-zhazhai\Desktop\input.json", "r") as file:
    data = json.load(file)

# 输出 CSV 文件
with open(r"C:\Users\v-zhazhai\Desktop\input_re.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    # 写表头
    writer.writerow(["Locale","Dataset names","Description","Raw data amount(hours)","V3 chunk data amount(hours)","Valid data amount in V3(hours)","Valid data ratio","File List","Yaml List"," Statistics result path","Data processed result path","Data process job"])
#     # 写数据
    for key, value in data.items():
        writer.writerow([key.replace(" ",","), value["Description"], value["Raw data amount(hours)"], value["V3 chunk data amount(hours)"], value["Valid data amount in V3(hours)"], value["Valid data ratio"], value["File List"], value["Yaml List"], value["Statistics result path"], value["Data processed result path"], value["Data process job"]])

# print("转换完成，已生成 output.csv")

