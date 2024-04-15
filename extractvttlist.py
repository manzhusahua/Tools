import os

rootdir = r"C:\Users\v-zhazhai\Downloads\de-DE"
output = r"C:\Users\v-zhazhai\Downloads\de-DE\de-DE.txt"
list_file_name = "audioList.txt"
FYdirs = os.listdir(rootdir)
for FYdir in FYdirs:
    FYdirpath = os.path.join(rootdir, FYdir)
    Youtubedirs = os.listdir(FYdirpath)
    for Youtubedir in Youtubedirs:
        Youtubedirpath = os.path.join(FYdirpath, Youtubedir)
        domaindirs = os.listdir(Youtubedirpath)
        for domaindir in domaindirs:
            domaindirpath = os.path.join(Youtubedirpath, domaindir)
            if not os.path.isdir(domaindirpath):
                print("not dir:" + domaindirpath)
                continue
            sourceaudiolist = os.path.join(domaindirpath, list_file_name)
            if not os.path.isfile(sourceaudiolist):
                print("file not exist:" + sourceaudiolist)
                continue
            audio_information_list = open(sourceaudiolist, "r", encoding="utf-8").readlines()
            
            keys = "AudioFileName	AudioTitle	AudioUrl	Duration	BitRate	SampleRate	SpeechRatio	Snr	CaptionType	CaptionFileName"
            keys = keys.split("\t")
            taotalDuration = 0
            for i, audio_information in enumerate(audio_information_list):
                if i == 0:
                    continue
            
                audio_information = audio_information.strip()
                audio_items = audio_information.split("\t")
                if len(keys) == len(audio_items):
                    audio_dict = dict(zip(keys, audio_items))
                    #print(audio_dict["Duration"])
                    taotalDuration = taotalDuration + float(audio_dict["Duration"])
            taotalDuration = taotalDuration / 3600
            print(sourceaudiolist)
            print(taotalDuration)
            with open(output, "a", encoding="utf-8") as f:
                f.write(sourceaudiolist + '\t' + str(taotalDuration))
                f.write("\n")

