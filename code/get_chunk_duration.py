import json,sys,os

def get_duration(json_path):
    with open(json_path,'r',encoding='utf8')as fp:
        json_data = json.load(fp)
    duration = float(json_data['metadata']['duration'])
    return duration


if __name__ == "__main__":
    # json_path = sys.argv[1]
    json_path = r"C:\Users\v-zhazhai\Downloads\json"
    durations = []
    for name in os.listdir(json_path):
        if ".json" in name:
            duration = get_duration(os.path.join(json_path,name))
            # print(name+" duration:"+duration)
            durations.append(duration)
    # print(sum(durations))
    print(str(round(sum(durations)/3600, 5)))