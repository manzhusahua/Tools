import os 
import json
import codecs
import chardet
from files_data_process.read_files import READFILE
from files_data_process.zipDir import ZIPDIR
import re
import codecs
import chardet

def read_json(jsonfile,trasnfile):
    # 打开 JSON 文件
    content=codecs.open(jsonfile,'rb').read()
    with open(jsonfile,'r',encoding=chardet.detect(content)['encoding']) as file:
        data = json.load(file)
    with open(trasnfile,'a',encoding='utf8') as s:
        for use in data["Results"]:
            Audio = use["Audio"].split('/')[-1].replace('.wav','')
            word = Audio+'\t'+use["FullTranscription"]+'\n'
            s.writelines(word)

def clean_trans(trasnfile,savefiles):
    # ZIPDIR.zipDir(r"C:\Users\v-zhazhai\Desktop\20230219085455\waves",r"C:\Users\v-zhazhai\Desktop\20230219085455\waves.zip")
    ids = []
    pattern = 'qwertyuiopasdfghjklzxcvbnm'

    word = READFILE().read_file(trasnfile)
    with open(savefiles,'w',encoding='utf8') as s:
        for line in word:
            # print(line)
            name = line.split('\t')[0]
            if name not in ids:
                ids.append(name)
                new_trans = ''
                trans = line.split('\t')[-1].replace('\n','').split(' ')
                for n in range(len(trans)):
                    # print(trans[n+1][0])
                    if n==len(trans)-1:
                        new_trans = new_trans+trans[n]+'。'
                    elif str(trans[n][-1]).lower() not in pattern and str(trans[n+1][0]).lower() not in pattern:
                        new_trans = new_trans+trans[n]+'，'
                    elif str(trans[n][-1]).lower() in pattern and str(trans[n+1][0]).lower() not in pattern:
                        new_trans = new_trans+trans[n]+'，'
                    elif str(trans[n][-1]).lower() not in pattern and str(trans[n+1][0]).lower() in pattern:
                        new_trans = new_trans+trans[n]+'，'
                    else:
                        new_trans = new_trans+trans[n]+' '
                s.writelines(name+'\t'+new_trans+'\n')
            else:
                continue


if __name__ == "__main__":
    inputdir = r"C:\Users\v-zhazhai\debug\richland\xmly_zhcnenus_learning_output"
    trasnfile = r"C:\Users\v-zhazhai\debug\richland\xmly_zhcnenus_learning_output\E2E_trans.txt"
    savefiles = r"C:\Users\v-zhazhai\debug\richland\xmly_zhcnenus_learning_output\E2E_trans_punc.txt"
    for line in os.listdir(inputdir):
        if '.json' in line:
            jsonfile = os.path.join(inputdir,line)
            read_json(jsonfile,trasnfile)
    clean_trans(trasnfile,savefiles)