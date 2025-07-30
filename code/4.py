import os,shutil
import glob
import json

folders = ["average_duration_0-15","average_duration_15-35","average_duration_35-50","average_duration_50"]

inputdir = r"C:\Users\v-zhazhai\Downloads\dataset\tier4\uk-ua\podcast_rss"
for line in folders:
    os.makedirs(os.path.join(inputdir,line), exist_ok=True)


for jsonfile in glob.glob(os.path.join(inputdir, "**", "*.json"), recursive=True):
    with open(jsonfile, "r",encoding='utf8') as file:
            data = json.load(file)
    with open(os.path.join(inputdir,os.path.basename(jsonfile).replace(".json",""),"filelist.txt"),'w',encoding='utf8') as s:
        for line in data:
            # print(line)
            word = "/".join(["/datablob/realisticttsdataset_v3/train/chunks/tier4/uk-ua/podcast_rss",os.path.basename(jsonfile).replace(".json",""),line+".json\n"])
            # print(word)
            s.writelines(word)
# txtfile = ''
# for txtfile in glob.glob(os.path.join(inputdir, "**", "*.txt"), recursive=True):
# # for txtfiles in os.listdir(inputdir):
# #     if ".txt" in txtfiles:
# #         txtfile = os.path.join(inputdir,txtfiles)
            
# #     print(txtfile)
#     with open(txtfile,'r',encoding='utf8') as f,open(os.path.join(inputdir,os.path.basename(txtfile).replace(".txt",""),"filelist.txt"),'w',encoding='utf8') as s:
#         for line in f.readlines():
            
#             word = "/".join(["/datablob/realisticttsdataset_v3/train/chunks/tier4/uk-ua/podcast_rss",os.path.basename(txtfile).replace(".txt",""),line])
#                 # print(word)
#             s.writelines(word)