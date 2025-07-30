import json, sys, os

def statistics_result_list(jsondir,savelist):
    with open(savelist,'w') as s:
        for name in os.listdir(jsondir):
            with open(os.path.join(jsondir,name), "r") as file:
                data = json.load(file)
            for use in data:
                # if float(data[use]["valid_ratio"].replace("%","")) >30:
                    # print(os.path.join(jsondir,name.replace(".json",""),use+".json"))
                    s.writelines(os.path.join(jsondir,name.replace(".json",""),use+".json")+'\n')

def statistics_result_list_V3(jsondir,savelist):
    with open(savelist,'w') as s:
        for name in os.listdir(jsondir):
            if ".json" in name:
                with open(os.path.join(jsondir,name), "r") as file:
                    data = json.load(file)
                for use in data:
                    s.writelines(os.path.join(jsondir,name.replace(".json",""),use+".json").replace(r"C:\Users\v-zhazhai\Environment\CookingSpeech\RealisticTTSDatasets\dataset","/datablob/realisticttsdataset_v3/train/chunks").replace("\\","/")+'\n')
    for name in os.listdir(jsondir):
        if ".json" in name:
            save_path = os.path.join(jsondir,name.replace(".json",""))
            os.makedirs(save_path, exist_ok=True)
            with open(os.path.join(save_path,"filelist.txt"),'w',encoding='utf8') as s1:
                with open(os.path.join(jsondir,name), "r") as file:
                    data = json.load(file)
                for use in data:
                    s1.writelines(os.path.join(jsondir,name.replace(".json",""),use+".json").replace(r"C:\Users\v-zhazhai\Environment\CookingSpeech\RealisticTTSDatasets\dataset","/datablob/realisticttsdataset_v3/train/chunks").replace("\\","/")+'\n')

if __name__ == "__main__":
    jsondir = r"C:\Users\v-zhazhai\Environment\CookingSpeech\RealisticTTSDatasets\dataset\tier4\bn-in\podcast_rss"
    savelist = r"C:\Users\v-zhazhai\Environment\CookingSpeech\RealisticTTSDatasets\dataset\tier4\bn-in\podcast_rss\all.txt"
    statistics_result_list_V3(jsondir,savelist)