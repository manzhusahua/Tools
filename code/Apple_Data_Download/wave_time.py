import eyed3
import glob
import os
def get_duration_eyed3(file_path):
    audiofile = eyed3.load(file_path)
    return audiofile.info.time_secs


def get_duration_floder(inputdir):
    time_counts=[]
    for file in glob.glob(os.path.join(inputdir,"**\\*.mp3"), recursive=True):
        duration = get_duration_eyed3(file)
        time_counts.append(duration)
    print(str(round(sum(time_counts)/3600, 2)))
    # return str(round(sum(time_counts)/3600, 2))

if __name__ == "__main__":
    inputdir = r"C:\Users\v-zhazhai\Desktop\Apple_data\batch01\it\id1773061271"
    print('it:',end='\t')
    get_duration_floder(inputdir)