import json, sys, os


def read_json(jsonfile):
    # 打开 JSON 文件
    with open(jsonfile, "r") as file:
        data = json.load(file)
    # durations = [int(line["duration"]) for line in data["fileInfo"]]
    print(data["metadata"]["duration"])
    # print([int(line["duration"]) for line in data["metadata"]])
    # 打印读取的 JSON 数据
    # print(os.path.split(jsonfile)[0] + "\t" + str(round(sum(durations) / 3600, 5)))
    # print(durations)


if __name__ == "__main__":

    # read_json(sys.argv[1])
    read_json(
        r"C:\Users\v-zhazhai\Downloads\chunk_000ceb014377cbe0f627e9b0f38eb4d3_0.json"
    )
