""""
用于获取fasttranscription 失败的filelist
"""

import os

def get_fail_list(logdir,savelist):
    with open(savelist, 'w') as s:
        for file in os.listdir(logdir):
            with open(os.path.join(logdir, file), 'r') as f:
                for line in f.readlines():
                    if "get sr result failed" in line:
                        s.writelines(line.split('"')[1]+'\n')
if __name__ == "__main__":
    logdir = r"C:\Users\v-zhazhai\Downloads\log"
    savelist = r'C:\Users\v-zhazhai\Downloads\frca.txt'
    get_fail_list(logdir,savelist)
    