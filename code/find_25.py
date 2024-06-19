import pandas as pd
import os,sys

def updat_sid_file(metadata_files,save_files,speaker_id,node):
    data1 = pd.read_csv(metadata_files,sep="|",encoding='utf8',low_memory=False)
    save_data = pd.DataFrame()
    audio_book_names=list(set(["_".join(x.split('_')[2:-2]) for x in data1['sid']]))
    audio_book_names.sort()
    # audio_book_jie=list(set([int(x.split('_')[-2]) for x in data1['sid']]))
    audio_book_jie=list(set([x.split('_')[-2] for x in data1['sid']]))
    audio_book_jie.sort()
    audio_book_chai = list(set([int(x.split('_')[-1]) for x in data1['sid']]))
    audio_book_chai.sort()
    for i in audio_book_names:
        for j in audio_book_jie:
            for m in audio_book_chai:
                for x in data1['sid']:
                    if "_".join([str(i),str(j).zfill(int(node)),str(m)]) in x:
                        save_data = save_data._append(data1.iloc[int(list(data1['sid']).index(x))])
    save_data['speaker'] = save_data.apply(lambda x: speaker_id, axis=1)
    save_data.to_csv(save_files,sep="|",encoding='utf8',index=False)

def find_25(metadata_files):
    data = pd.read_csv(metadata_files,sep="|",encoding='utf8',low_memory=False)
    id = []
    for i in range(len(data)):
        speech_length = float(data.iloc[i]["speech_length_in_s"])
        sid = str(data.iloc[i]["sid"].split("_")[-2])
        if (speech_length > 25.0) and (sid not in id):
            id.append(sid)
            print(sid)




if __name__ == "__main__":
    files = r"C:\Users\v-zhazhai\Downloads\metadata_PtBRMacerioOAI_general.csv"
    # files = sys.argv[1]
    speaker_id = "PtBRMacerioOAI"
    # speaker_id = sys.argv[2]
    node = 10
    # node = sys.argv[3]
    updat_sid_file(files,files.replace(".csv","_v1.csv"),speaker_id,node)
    # os.remove(files)
    # os.renames(files.replace(".csv","_v1.csv"),files)
    # find_25(files)
