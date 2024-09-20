import pandas as pd
import os

files = r"C:\Users\v-zhazhai\Desktop\filenames.txt"

output = r"C:\Users\v-zhazhai\Desktop\Paragraph\trans"
# data1 = pd.read_csv(files,sep=",",encoding='utf8',low_memory=False)
# index = list(range(data1.shape[0]))
# maps = { "IEO":"It's eleven o'clock.","TIE":"That is exactly what happened.","IOM":"I'm on my way to the meeting.","IWW":"I wonder what this is about.","TAI":"The airplane is almost full.","MTI":"Maybe tomorrow it will be cold.","IWL":"I would like a new alarm clock.","ITH":"I think I have a doctor's appointment.","DFA":"Don't forget a jacket.","ITS":"I think I've seen this before.","TSI":"The surface is slick.","WSI":"We'll stop in a couple of minutes"}
# for i in index:
#     line = str(data1.iloc[i]["clipName"])
#     name = line.split("_")[1]
#     # print(name)
#     # print(maps.get(name))
#     with open(os.path.join(output,line+'.txt'),'w',encoding='utf8') as s:
#         s.writelines(str(maps.get(name)))

with open(files,'r',encoding='utf8') as f:
    for line in f.readlines()[:2]:
        print(line)