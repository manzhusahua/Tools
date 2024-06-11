import wave
import os,sys
wav_path = sys.argv[1]

time_counts=[]
for name in os.listdir(wav_path):
    wav_name = os.path.join(wav_path,name)
    f = wave.open(wav_name, 'rb')
    time_count = f.getparams().nframes/f.getparams().framerate
    time_counts.append(time_count)
print(sum(time_counts))
print(str(round(sum(time_counts)/3600, 5)))