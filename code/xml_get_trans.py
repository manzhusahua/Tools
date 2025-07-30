import os
import codecs
import chardet
import glob

"""
用于从xml中提取文本
"""

def get_trans(inputdir,savedir):
    # for file_path in glob.glob(os.path.join(inputdir, "**", "*.xml"), recursive=True):
    # for file_path in glob.glob(os.path.join(inputdir, "**", "*.xml"), recursive=True):
        file_path = inputdir
        n=0
        content=codecs.open(file_path,'rb').read()
        word = open(file_path,'r',encoding=chardet.detect(content)['encoding']).readlines()
        for line in word:
            if "  <si id=" in line:
                name = line.split('"')[1]
                with open(os.path.join(savedir,name+".txt"),'w',encoding='utf8') as s:
                    s.writelines(word[n+1].split("<text>")[1].split("</text>")[0]+'\n')
                # print(line)
                # print(word[n+1])
            n+=1


if __name__ =="__main__":
    save_dir = r"C:\Users\v-zhazhai\Downloads\trans"
    inputdir = r"C:\Users\v-zhazhai\Downloads\XmlScripts"
    
    os.makedirs(save_dir, exist_ok=True)
    for line in os.listdir(inputdir):
        save_dirs = os.path.join(save_dir,line.replace(".xml",""))
        os.makedirs(save_dirs, exist_ok=True)
        get_trans(os.path.join(inputdir,line),save_dirs)