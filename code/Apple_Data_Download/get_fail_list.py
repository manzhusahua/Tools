""""
用于获取fasttranscription 失败的filelist
"""

import os,sys

def get_fail_list(logdir,savelist):
    with open(savelist, 'w') as s:
        for file in os.listdir(logdir):
            with open(os.path.join(logdir, file), 'r') as f:
                for line in f.readlines():
                    if "get sr result failed" in line:
                        s.writelines(line.split('"')[1]+'\n')

def get_fail_lists(jsondir,filelist):
    jsonlist = open(jsondir,'r').readlines()
    with open(filelist, 'r') as f,open(os.path.join(os.path.split(filelist)[0],"fail_list.txt"),'w') as s:
        for line in f.readlines():
            names = "_".join(line.split('/')[-2:]).replace(".mp3",".json")
            if names not in jsonlist:
                s.writelines(line)
            

if __name__ == "__main__":
    logdir = r"C:\Users\v-zhazhai\Downloads\log"
    savelist = r"C:\Users\v-zhazhai\Downloads\frfr_clean.txt"
    # get_fail_lists(sys.argv[1],sys.argv[2])
    get_fail_list(logdir,savelist)
    