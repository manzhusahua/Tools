import wave
import os
import glob

def get_wav_time(wav_path):
    time_counts=[]
    for file in glob.glob(os.path.join(wav_path,"**\\*.*"), recursive=True):
        if ".wav" in file:
            f = wave.open(file, 'rb')
            time_count = f.getparams().nframes/f.getparams().framerate
            time_counts.append(time_count)
    print(sum(time_counts))
    print(str(round(sum(time_counts)/3600, 5)))

if __name__ == "__main__":
    wav_path = r"C:\Users\v-zhazhai\Downloads\Emo-DB\wav"
    get_wav_time(wav_path)