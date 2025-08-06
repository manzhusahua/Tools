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
import shutil

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
    
    os.makedirs(savedir, exist_ok=True)
    
    for line in lines:
        try:
            # savedirs = os.path.join(savedir,line.split('\t')[0].split("/")[0])
            # os.makedirs(savedirs, exist_ok=True)
            # with open(os.path.join(savedirs,line.split('\t')[0].split("/")[-1].replace(".wav",".txt")),'w',encoding='utf8') as s:
            with open(os.path.join(savedir,line.split('\t')[0]+".txt"),'w',encoding='utf8') as s:
                s.writelines(line.split('\t')[-1])
        except Exception as e:
            print(f"Error processing line {line}: {e}")

def get_transcription_result(ft_result_file):
    with open(ft_result_file, "r", encoding="utf-8") as f,open(ft_result_file.replace('.txt','_clean.txt'), 'w', encoding='utf-8') as s:
        for line in f.readlines():
            if ".json" not in line:
                s.writelines(line)
        
def average_duration(filelist,cleanlist):
    word = open(cleanlist, 'r', encoding='utf8').readlines()
    with open(filelist,'r',encoding='utf8') as f,open(filelist.replace('.txt','_average.txt'),'w',encoding='utf8') as s:
        for line in f.readlines():
            # print(line)
            if line in word:
                s.writelines(line)

def renames(inputdir,outputdir):
    os.makedirs(outputdir, exist_ok=True)
    n=0
    with open(os.path.join(os.path.split(outputdir)[0],"map.txt"),'w',encoding='utf8') as s:
        for file in glob.glob(os.path.join(inputdir,"**\\*.*"), recursive=True):
            name = os.path.basename(file)
            rename = str(n).zfill(8)+"."+file.split(".")[-1]
            shutil.copyfile(file,os.path.join(outputdir,rename))
            s.writelines(file+'\t'+os.path.join(outputdir,rename)+'\n')
            n+=1

def read_info(infofile):
    word = READFILE().read_file(infofile)
    print(word)
  
             
if __name__ == "__main__":
    get_trans(r"C:\Users\v-zhazhai\Downloads\1\vi.txt",r"C:\Users\v-zhazhai\Desktop\vi")
    # average_duration(r"C:\Users\v-zhazhai\Downloads\filelist_0-15.txt",r"C:\Users\v-zhazhai\Downloads\v3_input_json.txt")
    # average_duration(r"C:\Users\v-zhazhai\Downloads\filelist_15-35.txt",r"C:\Users\v-zhazhai\Downloads\v3_input_json.txt")
    # average_duration(r"C:\Users\v-zhazhai\Downloads\filelist_35-50.txt",r"C:\Users\v-zhazhai\Downloads\v3_input_json.txt")
    # average_duration(r"C:\Users\v-zhazhai\Downloads\filelist_50.txt",r"C:\Users\v-zhazhai\Downloads\v3_input_json.txt")
    # read_info(r"C:\Users\v-zhazhai\Downloads\chunk_1aaaf19763e993534d35e7f72d323c01_107.info")
    # with open(r"C:\Users\v-zhazhai\Downloads\all_20250304.txt",'r',encoding="utf8") as f,open(r"C:\Users\v-zhazhai\Downloads\all_20250304_clean.txt",'w',encoding="utf8") as s:
    #     words = []
    #     for line in f.readlines():
    #         lines = "/".join(line.split('/')[:-1])
    #         if lines not in words:
    #             words.append(lines)
    #     for word in words:
    #         s.writelines(word+'\n')