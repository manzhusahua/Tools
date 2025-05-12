import os
import codecs
import chardet


file_path = r"C:\Users\v-zhazhai\Desktop\en-us_youtube\check\20250226_clean.txt"
save_dir = r"C:\Users\v-zhazhai\Desktop\en-us_youtube\check\en-us_youtube"
os.makedirs(save_dir, exist_ok=True)

content=codecs.open(file_path,'rb').read()
word = open(file_path,'r',encoding=chardet.detect(content)['encoding']).readlines()

for line in word:
    # print(line.split('/')[8])
    savedir = os.path.join(save_dir,line.split('/')[8])
    if not os.path.exists(savedir):
        os.makedirs(savedir)
    with open(os.path.join(savedir,"filelist.txt"),'a') as s:
        s.writelines(line)