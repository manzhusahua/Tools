import os
import codecs
import chardet


def split_text(textfile,savedir):
    content=codecs.open(textfile,'rb').read()
    word = open(textfile,'r',encoding=chardet.detect(content)['encoding']).readlines()
    for line  in word:
        with open(os.path.join(savedir,line.split('\t')[0]+".txt"),'w',encoding='utf8') as f:
            f.write(line.split('\t')[-1])   


if __name__ == "__main__":
    split_text(r"C:\Users\v-zhazhai\Desktop\words\Scripts.txt",r"C:\Users\v-zhazhai\Desktop\words\Scripts")