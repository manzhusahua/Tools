import json, sys, os

def read_json(jsonfile):
    with open(jsonfile, "r") as file:
        data = json.load(file)
    data["metadata"]["dataset_name"] = "podcast_Single_Speaker"
    with open(jsonfile.replace(".json","_v1.json"),'w',encoding='utf8') as s:
        json.dump(data, s, indent=4)
    os.remove(jsonfile)
    os.renames(jsonfile.replace(".json","_v1.json"),jsonfile)

if __name__ == "__main__":
    inputdir = r"C:\Users\v-zhazhai\Downloads\podcast_Single_Speaker\it-it"
    for line in os.listdir(inputdir):
     read_json(os.path.join(inputdir,line))