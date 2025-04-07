import pandas as pd

line = 'SSB06930002.wav	武 wu3 术 shu4 始 shi3 终 zhong1 被 bei4 看 kan4 作 zuo4 我 wo3 国 guo2 的 de5 国 guo2 粹 cui4'

def find_values(names):
    map = pd.read_csv(r"C:\Users\v-zhazhai\Desktop\data_aishell3\spk-info.csv",sep="|",encoding='utf8',low_memory=False)
    index = list(range(map.shape[0]))
    age_group,gender,accent = "","",""
    for i in index:
        line = map.iloc[i]
        if line['Names'] == names:
            age_group = map.iloc[i]["age group"]
            gender = map.iloc[i]["gender"]
            accent = map.iloc[i]["accent"]
    return age_group,gender,accent

AudioFileName = line.split('\t')[0]

Transcription = ''
for n in range(0,len(line.split('\t')[-1].split(" ")),2):
    Transcription+=line.split('\t')[-1].split(" ")[n]

age_group,gender,accent = find_values(AudioFileName[:7])
row_values = {
                    "AudioFileName": "{}".format(AudioFileName),
                    "Transcription": "{}".format(Transcription),
                    "AgeRroup": "{}".format(age_group),
                    "Gender": "{}".format(gender),
                    "Accent": "{}".format(accent),
                    "DataName": "{}".format(accent),
                    "Source": "emotional",
                }