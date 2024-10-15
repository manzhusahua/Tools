import os
import codecs
import chardet
import json

class TTSPREPARE():
    def __init__(self) -> None:
        super().__init__()
    
    def get_json(self,inputdir,outputdir,style):
        with open(os.path.join(outputdir+".json"),"w",encoding="utf8",) as save_json:
            waves_values = {}
            for name in os.listdir(inputdir):
                file_path = os.path.join(inputdir,name)
                content=codecs.open(file_path,'rb').read()
                word = open(file_path,'r',encoding=chardet.detect(content)['encoding']).readlines()
                for line in word:
                    wave_name = line.split('\t')[0]
                    wave_name_values = {
                        "speaker": "ZhCNM903",
                        "gender": "female",
                        "style": "{}".format(style)
                    }
                    waves_values[wave_name] = wave_name_values
            row_values = {
                "metadata": {
                    "speaker": "ZhCNM903",
                    "gender": "female",
                    "locale": "zh-cn"
                    },
                "sentencemetadata": waves_values
            }
            json.dump(row_values, save_json, indent=4)

    def info_json(self,inputdir,outuptdir):
        wave_name = []
        waves_values  = {}
        for name in os.listdir(inputdir):
            json_file = os.path.join(inputdir,name)
            # json_file = r"C:\Users\v-zhazhai\Desktop\M903\json_files\Assistant.json"
            with open(json_file,'r') as f:
                users = json.load(f)
            
            for user in users["sentencemetadata"]:
                if user not in wave_name:
                    wave_name.append(user)
                    waves_values[user] = users["sentencemetadata"][user]
                else:
                    print(str(user),end='\t')
                    print(users["sentencemetadata"][user]["style"])
        row_values = {
            "metadata": {
                "speaker": "ZhCNM903",
                "gender": "female",
                "locale": "zh-cn"
                },
                "sentencemetadata": waves_values
        }
        with open(outuptdir,"w",encoding="utf8",) as save_json:
            json.dump(row_values, save_json, indent=4)
INPUT_STEP = None

def init():

    global INPUT_STEP
    INPUT_STEP = TTSPREPARE()

    INPUT_STEP.prs_step_init()

def run(mini_batch):

    return INPUT_STEP.prs_step_run(mini_batch)

if __name__ == "__main__":
    TTS_parepare = TTSPREPARE()
    inputdir = r"C:\Users\v-zhazhai\Desktop\20230219085455\json_files"
    outputdir = r"C:\Users\v-zhazhai\Desktop\20230219085455\trans.txt"
    style = "PureEnglish"
    TTS_parepare.info_json(inputdir,outputdir)