import os 
import json
import codecs
import chardet
from files_data_process.read_files import READFILE
import re
import wave
import os
import glob
from scipy.io.wavfile import read

def read_json(jsonfile):
    # 打开 JSON 文件
    content=codecs.open(jsonfile,'rb').read()
    with open(jsonfile,'r',encoding=chardet.detect(content)['encoding']) as file:
        data = json.load(file)
    f = wave.open(jsonfile.replace('.json','.wav'), 'rb')
    time_count = f.getparams().nframes/f.getparams().framerate

    return data["Style"]+'\t'+ str(time_count)

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

def wave_Style_Statistics(inputdir):
    # S01_achievement_low_03
    f = wave.open(inputdir, 'rb')
    # f = read(inputdir)
    time_count = f.getparams().nframes/f.getparams().framerate
    return os.path.basename(inputdir).split('_')[1]+'\t'+ str(time_count)
    
if __name__ == "__main__":
    inputdir = r"C:\Users\v-zhazhai\Downloads\EMNS\raw_webm_wave"
    # trasnfile = r"C:\Users\v-zhazhai\debug\richland\xmly_zhcnenus_learning_output\E2E_trans.txt"
    # savefiles = r"C:\Users\v-zhazhai\debug\richland\xmly_zhcnenus_learning_output\E2E_trans_punc.txt"
    with open(inputdir+".txt",'w',encoding='utf8') as s:
        for line in os.listdir(inputdir):
            if '.json' in line :
                try:
                    jsonfile = os.path.join(inputdir,line)
                    word = read_json(jsonfile)
                    s.writelines(word+'\n')
                except Exception as e:
                    print(f"Failed due to {e}")
                    continue
            # word = wave_Style_Statistics(os.path.join(inputdir,line))
                # s.writelines(word+'\n')
    # clean_trans(trasnfile,savefiles)
    
    
