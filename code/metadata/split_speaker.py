import os
import pandas as pd


"""
用于split metadata中的不同speaker
"""
class SPLITSPEAKER():
    def __init__(self) -> None:
        super().__init__()

    def split_metadata(self,metadata_path,speaker):
        save_path = os.path.join(os.path.split(metadata_path)[0],speaker+".csv")
        save_data = pd.DataFrame()
        data = pd.read_csv(metadata_path, sep='|', encoding='utf-8',low_memory=False)
        index = list(range(data.shape[0]))
        for i in index:
            line = data.iloc[i]
            speakers = line['speaker']
            if speaker == speakers:
                save_data = save_data._append(line)
        save_data.to_csv(save_path,sep="|",encoding='utf8',index=False)

if __name__ == "__main__":
    split_metadata = SPLITSPEAKER()
    metadata_path = r"C:\Users\v-zhazhai\Downloads\metadata.csv"
    speaker = "IdIDArdi"
    save_path = r"C:\Users\v-zhazhai\Downloads\{}.csv".format(speaker)
    # print(save_path)

    split_metadata.split_metadata(metadata_path,speaker)