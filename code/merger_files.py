
import os

files_path = r"C:\Users\v-zhazhai\debug\richland\F128\General\TextScripts"

for name in os.listdir(files_path):
    with open(files_path+'.txt','a',encoding='utf8') as s:
        with open(os.path.join(files_path,name),'r',encoding='utf16') as f:
            for line in f.readlines():
                s.writelines(line)