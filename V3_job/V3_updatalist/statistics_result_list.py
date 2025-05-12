import json, sys, os

def statistics_result_list(jsondir,savelist):
    with open(savelist,'w') as s:
        for name in os.listdir(jsondir):
            with open(os.path.join(jsondir,name), "r") as file:
                data = json.load(file)
            for use in data:
                if float(data[use]["valid_ratio"].replace("%","")) >30:
                    # print(os.path.join(jsondir,name.replace(".json",""),use+".json"))
                    s.writelines(os.path.join(jsondir,name.replace(".json",""),use+".json")+'\n')
if __name__ == "__main__":
    jsondir = r"C:\Users\v-zhazhai\Desktop\en-us_youtube\Nonprofits_Activism"
    savelist = r"C:\Users\v-zhazhai\Desktop\en-us_youtube\Nonprofits_Activism.txt"
    statistics_result_list(jsondir,savelist)