import pandas as pd


def get_speech_lengths(metadata_files):
    data = pd.read_csv(metadata_files,sep="|",encoding='utf8',low_memory=False)
    speech_lengths = []
    for i in range(len(data)):
        speech_length = float(data.iloc[i]["speech_length_in_s"])
        speech_lengths.append(speech_length)
    print(str(round(sum(speech_lengths)/3600, 5)))


if __name__ == "__main__":
    get_speech_lengths(r"C:\Users\v-zhazhai\Downloads\metadata_0.csv")