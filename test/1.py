import os
import pandas as pd


metdata_path = r"C:\Users\v-zhazhai\Downloads\CaiQing\data_change\EnUSZo.csv"
data = pd.read_csv(metdata_path,sep="|",encoding='utf8')

chunk_path = []
for i in range(len(data)):
    line = data.iloc[i]
    speech_path = line["speech_path"].split('/')[1]
    if speech_path not in chunk_path:
        chunk_path.append(speech_path)
        print(speech_path)