import wave
import os,sys
import glob
from tinytag import TinyTag

def get_wav_time(wav_path):
    time_counts=[]
    for file in glob.glob(os.path.join(wav_path,"**\\*.*"), recursive=True):
        if ".wav" in file:
            f = wave.open(file, 'rb')
            time_count = f.getparams().nframes/f.getparams().framerate
            time_counts.append(time_count)
    print(sum(time_counts))
    print(str(round(sum(time_counts)/3600, 5)))

def get_wav_time1(wav_path):
    for index, elements in enumerate(os.listdir(wav_path)):
        duration = TinyTag.get(os.path.join(wav_path,elements)).duration
        print(duration)

def get_wav_time2(wav_list):
    time_counts=[]
    with open(wav_list, 'r', encoding='utf8') as f:
        for line in f.readlines():
            f = wave.open(line.replace('\n',''), 'rb')
            time_count = f.getparams().nframes/f.getparams().framerate
            time_counts.append(time_count)
    print(sum(time_counts))
    print(str(round(sum(time_counts)/3600, 5)))
                
if __name__ == "__main__":
    wav_list = sys.argv[1]
    # wav_list = r'C:\Users\v-zhazhai\Downloads\zhcn'
    # get_wav_time(wav_list)
    get_wav_time2(wav_list)