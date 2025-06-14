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

def fast_transcription_result_wus2(ft_result_file):    
    with open(ft_result_file, "r", encoding="utf-8") as f:
        ft_result = json.load(f)
        total_duration = (ft_result.get("durationMilliseconds", 0) / 1000)  # Convert milliseconds to seconds
        print(f"Total duration: {total_duration} seconds")
    
        segment_total_duration = 0
        segments = ft_result.get("phrases", [])
        for segment in segments:
            segment_duration = (
                segment.get("durationMilliseconds", 0) / 1000
            )  # Convert milliseconds to seconds
            segment_total_duration += segment_duration
    
    print(f"Total duration of segments: {segment_total_duration} seconds")

def get_trans(txtfile,savedir):
    with open(txtfile, 'r', encoding='utf8') as f:
        lines = f.readlines()
    
    if not os.path.exists(savedir):
        os.makedirs(savedir)
    
    for line in lines:
        with open(os.path.join(savedir,line.split('\t')[0]+".txt"),'w',encoding='utf8') as s:
            s.writelines(line.split('\t')[-1])
if __name__ == "__main__":
    get_trans(r"C:\Users\v-zhazhai\Desktop\Scripts01_clean.txt",
              r"C:\Users\v-zhazhai\Desktop\trans")
    