import json, sys, os


def read_json(jsonfile):
    # 打开 JSON 文件
    with open(jsonfile, "r",encoding='utf8') as file:
        data = json.load(file)
    Durations = 0.0
    # durations = [int(line["duration"]) for line in data["fileInfo"]]
    if 'h' in data["Duration"] and "min" not in data["Duration"]:
        Durations=int(data["Duration"].split(' ')[0]).replace('h','')
    if 'h' in data["Duration"] and "min" in data["Duration"]:
        Durations=float(data["Duration"].split(' ')[0].replace('h',''))+int(data["Duration"].split(' ')[2].replace('min',''))/60
    if 'h' not in data["Duration"] and "min" in data["Duration"]:
        Durations=int(data["Duration"].split(' ')[0].replace('min',''))/60
    return Durations
    # print([int(line["duration"]) for line in data["metadata"]])
    # 打印读取的 JSON 数据
    # print(os.path.split(jsonfile)[0] + "\t" + str(round(sum(durations) / 3600, 5)))
    # print(durations)

def run(inputdir):
    for line in os.listdir(inputdir):
            Duration = []
            for name in os.listdir(os.path.join(inputdir,line)):
                try:
                    if '.json' in name:
                        Durations = read_json(os.path.join(inputdir,line,name))
                        Duration.append(Durations)
                except Exception as e:
                    print("Failed Length_Of_Time due to %s" % e)
            print(line+'\t'+str(sum(Duration)))
if __name__ == "__main__":
    import glob
    Duration = []
    for line in glob.glob(os.path.join(r"C:\Users\v-zhazhai\Desktop\Apple_data\batch02\ca\id1322200189", "**", "*.json"), recursive=True):
        try:
            Durations = read_json(line)
            Duration.append(Durations)
        except Exception as e:
            print(line)
    print(str(sum(Duration)))
    
    # read_json(sys.argv[1])
    # inputdir = sys.argv[1]
    # inputdir = r"C:\Users\v-zhazhai\Desktop\Apple_data\batch02\fr"
    # print('fr:',end='\t')
    # run(inputdir)
    
    # inputdir = r"C:\Users\v-zhazhai\Desktop\Apple_data\batch02\it"
    # print('it:',end='\t')
    # run(inputdir)
    
    # inputdir = r"C:\Users\v-zhazhai\Desktop\Apple_data\batch02\ca"
    # print('ca:',end='\t')
    # run(inputdir)
    
    # inputdir = r"C:\Users\v-zhazhai\Desktop\alignment\mixlingual\Test1"
    # for line in os.listdir(inputdir):
    #     os.renames(os.path.join(inputdir,line),
    #                os.path.join(inputdir,line.replace('_','')))
    