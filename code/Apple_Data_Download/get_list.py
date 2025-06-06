"""
用于获取podcast下载后音频的list
"""

import os,sys,glob
import json

def get_audiolist(inputdir,listpath):
    with open(listpath,'w',encoding='utf8') as s:
        for file_path in glob.glob(os.path.join(inputdir, "**", "*"), recursive=True):
            # print(file_path)
            s.writelines(file_path+'\n')

def get_average_duration_list(inputdir,listpath):
    with open(inputdir,'r',encoding='utf8') as f,open(listpath,'w',encoding='utf8') as s:
        for line in f.readlines():
            line = "_".join(line.split("_")[1:])
            s.writelines(line)
    os.remove(inputdir)
    os.renames(listpath,inputdir)

def clean_audiolist(inputdir):
    with open(inputdir,'r',encoding='utf8') as f,open(inputdir.replace('.txt','_clean.txt'),'w',encoding='utf8') as s:
        for line in f.readlines():
            if ".json" not in line:
                s.writelines(line)
    os.remove(inputdir)
    os.renames(inputdir.replace('.txt','_clean.txt'),inputdir)

def json_list(jsonfile):
    with open(jsonfile, "r") as file:
        data = json.load(file)
if __name__ == "__main__":
    # get_audiolist(sys.argv[1],sys.argv[2])
    # get_average_duration_list(r"C:\Users\v-zhazhai\Downloads\test\filelist_50.txt",r"C:\Users\v-zhazhai\Downloads\test\filelist_501.txt")
    clean_audiolist(r"C:\Users\v-zhazhai\Downloads\data_batch02.txt")