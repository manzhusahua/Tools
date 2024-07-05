import pandas as pd
import csv,os
word = open(r"C:\Users\v-zhazhai\Downloads\trans.txt",'r',encoding='utf8').readlines()
data_frame = None
for line in word:
    wav_name = line.split('\t')[0]+'.wav'
    text = line.split('\t')[-1].replace('\n','')
    row_values = {
        "wav": [wav_name],
        "text": [text],
        "textless": ["false"],
        "human_voice": ["true"],
        "multispeaker_detect_score": ["-9999"],}
    if data_frame is None:
        data_frame = pd.DataFrame(row_values)
    else:
        newdata = pd.DataFrame(row_values)
        data_frame = pd.concat([data_frame, newdata], axis=0, ignore_index=True)
meta_file = os.path.join(r"C:\Users\v-zhazhai\Downloads", "metadata.csv")
data_frame.to_csv(
    meta_file, sep="|", encoding="utf-8", index=False, quoting=csv.QUOTE_NONE
    )