import os
import json

list_file_name = [r"FY24Q1-2\YouTube\Autos_Vehicles"]
inputdir = r"C:\Users\v-zhazhai\Downloads\de-DE"
outputdir = r"C:\Users\v-zhazhai\Downloads\de-DE\batch01_test"
if not os.path.exists(outputdir):
    os.makedirs(outputdir)
for item in list_file_name:
    list_file = os.path.join(inputdir, item, "audioList.txt")
    #print(list_file)
    audio_information_list = open(list_file, "r", encoding="utf-8").readlines()
        
    keys = "AudioFileName	AudioTitle	AudioUrl	Duration	BitRate	SampleRate	SpeechRatio	Snr	CaptionType	CaptionFileName"
    keys = keys.split("\t")
    for i, audio_information in enumerate(audio_information_list):
        if i == 0:
            continue
        audio_information = audio_information.strip()
        audio_items = audio_information.split("\t")
        if len(keys) == len(audio_items):
            audio_dict = dict(zip(keys, audio_items))
            audio_dict.update({"source": "Youtube"})
            audio_filename = os.path.basename(audio_dict["AudioFileName"])
            audio_filename = os.path.splitext(audio_filename)[0]
            audio_additional_filename = f"{audio_filename}.json"
            audio_additional_filename_path = os.path.join(outputdir, audio_additional_filename)
            print(audio_additional_filename_path)
            with open(audio_additional_filename_path, "w", encoding="utf-8") as f:
                json.dump(audio_dict, f, indent=4)
            #break
        else:
            print("error")