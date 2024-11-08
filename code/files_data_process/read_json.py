import json, sys, os


def read_json(jsonfile):
    # 打开 JSON 文件
    with open(jsonfile, "r") as file:
        data = json.load(file)
    print(data[2:-2])
    json.loads(data[2:-2].replace("'", '"'))
    # print(json.loads(line, strict=False))
    # durations = [int(line["duration"]) for line in data["fileInfo"]]
    # for use in data["Results"]:
    #     print(use)
    # print([int(line["duration"]) for line in data["metadata"]])
    # 打印读取的 JSON 数据
    # print(os.path.split(jsonfile)[0] + "\t" + str(round(sum(durations) / 3600, 5)))
    # print(durations)


if __name__ == "__main__":

    # read_json(sys.argv[1])
    read_json(
        r"C:\Users\v-zhazhai\Downloads\statistic\andrew\chunk_4aa5654794548e9d2a23d589b00ff2f9_0_statistics.stats"
    )
