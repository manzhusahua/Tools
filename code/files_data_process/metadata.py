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


if __name__ == "__main__":
    metadata_files = r"C:\Users\v-zhazhai\Downloads\metadata_0.csv"
    Get_Durationss(metadata_files)
