import json, sys, os
import numpy as np

def statistics_result_list(jsondir,savelist):
    with open(savelist,'w') as s:
        name = "data_chunks_summary.json"
        # for name in os.listdir(jsondir):
        with open(os.path.join(jsondir,name), "r") as file:
                data = json.load(file)
        for use in data:
                if float(data[use]["valid_ratio"].replace("%","")) >30:
                    # print(os.path.join(jsondir,name.replace(".json",""),use+".json"))
                    # s.writelines(os.path.join(jsondir,name.replace(".json",""),use+".json")+'\t'++'\n')
                    s.writelines(use+".json\t"+str(float(data[use]["valid_ratio"].replace("%","")))+'\n')

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



def valid_ratio_duration(jsonfile):
    duration_list=[]
    with open(jsonfile, "r") as file:
        data = json.load(file)
    for use in data:    
        duration_list.append(float(data[use]["valid_ratio"].replace("%","")))
    p10 = np.percentile(duration_list, 10)
    print(f"The 10th percentile (P10) of the list is: {p10}")
    p20 = np.percentile(duration_list, 20)
    print(f"The 20th percentile (P20) of the list is: {p20}")
    p30 = np.percentile(duration_list, 30)
    print(f"The 30th percentile (P30) of the list is: {p30}")
    p40 = np.percentile(duration_list, 40)
    print(f"The 40th percentile (P40) of the list is: {p40}")
    p50 = np.percentile(duration_list, 50)
    print(f"The 50th percentile (P50) of the list is: {p50}")
    p60 = np.percentile(duration_list, 60)
    print(f"The 60th percentile (P60) of the list is: {p60}")
    p70 = np.percentile(duration_list, 70)
    print(f"The 70th percentile (P70) of the list is: {p70}")
    p80 = np.percentile(duration_list, 80)
    print(f"The 80th percentile (P80) of the list is: {p80}")
    p90 = np.percentile(duration_list, 90)
    print(f"The 90th percentile (P90) of the list is: {p90}")
if __name__ == "__main__":
    jsondir = r"C:\Users\v-zhazhai\Environment\CookingSpeech\RealisticTTSDatasets\dataset\tier4\bn-in\podcast_rss"
    savelist = r"C:\Users\v-zhazhai\Environment\CookingSpeech\RealisticTTSDatasets\dataset\tier4\bn-in\podcast_rss\all.txt"
    # statistics_result_list_V3(jsondir,savelist)
    # statistics_result_list(r"C:\Users\v-zhazhai\Desktop",r"C:\Users\v-zhazhai\Desktop\average_duration_15-35.txt")
    valid_ratio_duration(r"C:\Users\v-zhazhai\Desktop\data_chunks_summary.json")