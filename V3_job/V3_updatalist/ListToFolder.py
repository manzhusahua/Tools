import os
"""
用于拆封all.txt
"""

def ListToFolder(allpath,savdir):
    os.makedirs(savdir, exist_ok=True)
    with open(allpath,'r',encoding='utf8') as f:
        for line in f.readlines():
            if "bilibili_resize" in line:
                with open(os.path.join(savdir,"all.txt"),'a',encoding='utf8') as s:
                    s.writelines(line)

def split_all(allpath,savdir):
    with open(allpath,'r',encoding='utf8') as f:
        for line in f.readlines():
            name = line.replace('/datablob/realisticttsdataset_v3/train/chunks/tier1/zh-cn/bilibili_resize/','').split('/')[0]
            os.makedirs(os.path.join(savdir,name), exist_ok=True)
            with open(os.path.join(savdir,name,"filelist.txt"),'a',encoding='utf8') as s:
                    s.writelines(line)
# ListToFolder(r"C:\Users\v-zhazhai\Desktop\zh-cn\all_20250304.txt",r"C:\Users\v-zhazhai\Desktop\zh-cn\bilibili_resize")
split_all(r"C:\Users\v-zhazhai\Desktop\zh-cn\bilibili_resize\all.txt",r"C:\Users\v-zhazhai\Desktop\zh-cn\bilibili_resize")