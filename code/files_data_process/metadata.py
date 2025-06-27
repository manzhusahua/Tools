import pandas as pd
import os


def Get_Durationss(metadata_files):
    data = pd.read_csv(metadata_files, sep="|", encoding="utf-8", low_memory=False)
    index = list(range(data.shape[0]))
    time_counts = []
    for i in index:
        line = data.iloc[i]
        time_counts.append(float(line["speech_length_in_s"]))
    print(str(round(sum(time_counts) / 3600, 5)), end="")

def get_list(metadata_files,savefile):
    filelist = []
    times = 0.0
    for line in os.listdir(metadata_files):
        data = pd.read_csv(os.path.join(metadata_files,line), sep="|", encoding="utf-8", low_memory=False)
        index = list(range(data.shape[0]))
        for i in index:
            line = data.iloc[i]
            # print(line["ratio"])
            if line["ratio"] > 0.6:
                filelist.append(line["wav"])
                times += float(line["duration"])
    with open(savefile, 'w', encoding='utf-8') as s:
        for file in filelist:
            s.writelines(os.path.basename(file).replace(".mp3",".wav")+'\n')
            
    print("Total duration: ", str(times))
            

if __name__ == "__main__":
    metadata_files = r"C:\Users\v-zhazhai\Downloads\metadata_0.csv"
    # Get_Durationss(metadata_files)
    get_list(r"C:\Users\v-zhazhai\Downloads\filelist",r"C:\Users\v-zhazhai\Downloads\zhcn.txt")