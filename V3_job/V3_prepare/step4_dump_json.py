import os,sys
import json

class step4:
    def __init__(self) -> None:
        super().__init__()
    
    def step4_dump_json(self,list_file_name,inputdir,batch):
        outputdir = os.path.join(inputdir,batch)
        if not os.path.exists(outputdir):
            os.makedirs(outputdir)
        for item in list_file_name:
            list_file = os.path.join(inputdir, item, "audioList.txt")
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

if __name__ == "__main__":
    list_file_name = sys.argv[1]
    # list_file_name = [r"FY23Q2\BingYouTube\Education",r"FY23Q2\YouTube\Education",r"FY23Q4-1\YouTube\Education",r"FY23Q4-2\YouTube\Education",r"FY23Q4-3\YouTube\Education",r"FY24Q1-1\YouTube\Education",r"FY24Q1-2\YouTube\Education",r"FY24Q1-3\YouTube\Education",r"FY24Q2-1\YouTube\Education",r"FY24Q2-2\YouTube\Education",r"FY24Q2-3\YouTube\Education",r"FY24Q3-1\YouTube\Education"]
    # inputdir = r"C:\Users\v-zhazhai\Downloads\fr-FR"
    inputdir = sys.argv[2]
    batch = sys.argv[3]
    step4.step4_dump_json(list_file_name,inputdir,batch)