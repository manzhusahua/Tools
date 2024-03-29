import json
import os
import sys
import shutil


def eg():
    {
    "metadata":{
            "speaker":"DeDEConrad",
            "locale":"de-de"
        },
    "sentencemetadata":{
            "3000000001":{
                "style":"NeutralChat",
                "role":"",
                "speaker":"unknown",
                "domain": "general"
            },
            "uttid2":{
                "style":"happy",
                "role":"abcde",
                "speaker":"",
                "domain": ""
            }
        }
    }

def Tier2_json():
    {
        "Speaker": "ArEGShaKir",
        "TextScripts": "\\ttsdata\ttsdata\ar-EG\Voices\ShaKir\TextScripts",
        "Wave48k": "\\ttsdata\ttsdata\ar-EG\Voices\ShaKir\Speech\Wave48k",
        "ForceAlign": "\\ttsdata\ttsdata\ar-EG\Voices\ShaKir\Alignment\ForcedAlignment.Phone.NoSR",
        "XmlScripts": "\\ttsdata\ttsdata\ar-EG\Voices\ShaKir\XmlScripts",
        "Wave24kNormalized": "\\ttsdata\ttsdata\ar-EG\Voices\ShaKir\Speech\Wave24kNormalized",
        "Wave48kNormalized": "\\ttsdata\ttsdata\ar-EG\Voices\ShaKir\Speech\Wave48kNormalized",
        "Style": 
          {
              "NeutralChat": ["3000000001-3000000500"],
              "NeutralCustomerService": ["4000000001-4000000500"],
              "Cheerfulchat": ["9130000001-9130000500"],
              "CheerfulCustomerService": ["9140000001-9140000500"]
          },
      
        "Domain": 
          {
              "Question": ["0100000001-0100000500", "0100000501-0100001000"],
              "Exclamation": ["0200000001-0200000500", "0200000501-0200001000"],
              "Word": ["0400000001-0400000500"],
              "Mixlingual": ["0500000001-0500000500", "0500000501-0500001000"],
              "English": ["0600000001-0600000500"]
          }
      }

class GetJson():
    def __init__(self) -> None:
        super().__init__()
    
    def get_styleWave(self, style,style_list,wave_list,speaker):
        sid = {}
        with open(wave_list,'r',encoding='utf8') as f:
                for name in f.readlines():
                    if '.wav' in name:
                        wave_name  = os.path.split(name)[-1].replace('.wav\n','')
                        for audio_range in style_list[style]:
                            if audio_range.split('-')[0] <= wave_name <= audio_range.split('-')[-1]:
                                sid[wave_name] = {"style":style,"role":"","speaker":speaker,"domain":""}
        return sid

    def process_file_list(self, input_file_list, output_dir):
        try:

            if not os.path.exists(output_dir):
                os.mkdir(output_dir)

            for input_file in input_file_list:
                print("Start processing %s." % (input_file))
                if not os.path.isfile(input_file):
                    raise Exception("setting %s does not exist!" % input_file)
                else:
                    with open(input_file) as f:
                        sf = f.read()
                    setting =json.loads(sf.replace('\\', '\\\\'))
                    speakers = setting['speakers']
                    

                    for i in range(0, len(speakers)):
                        line = setting['speakers'][i]
                        speaker = line['Speaker'].split('_')[0]
                        if speaker == "ArEGShaKir":
                            speaker_word = {}
                            metadata  = {"metadata":{"speaker":speaker,"locale":"en-us"}}
                            sentencemetadata = {}
                            # Wave48kNormalized_path = line['Wave48kNormalized']
                            # wave_list = os.path.join(output_dir,speaker)+".txt"
                            wave_list = r"C:\Users\v-zhazhai\Toosl\code\metadata_json\output\ArEGShaKir.txt"
                            # os.system('dir /b/s '+Wave48kNormalized_path+'\* > '+wave_list)
                            style_list = line['Style']
                            for line in style_list:                            
                                uttid = self.get_styleWave(line,style_list[line],wave_list,"ArEGShaKir")
                                sentencemetadata.update(uttid)
                            speaker_word.update(metadata)
                            speaker_word.update({"sentencemetadata":sentencemetadata})
                            # with open(os.path.join(output_dir,speaker)+".txt",'r',encoding='utf8') as f:
                            #     for wavename in f.readlines():
                            #         print(wavename)

                            with open(os.path.join(output_dir,"record.json"),'a') as write_f:
                                json.dump(speaker_word, write_f, indent=4, ensure_ascii=False)


        except Exception as e:
            print("Failed to processing about %s." % e)


def init():

    global GET_JSON
    GET_JSON = GetJson()

    GET_JSON.prs_step_init()

def run(mini_batch):

    return GET_JSON.prs_step_run(mini_batch)


# End of the required functions for AML PRS step

# This function can contain main func so we can quickly local dev and debug this module
if __name__ == "__main__":
    get_json = GetJson()

    input_file_path = r"C:\Users\v-zhazhai\Toosl\code\metadata_json\json_files"
    input_file_list = []
    output_dir = r'C:\Users\v-zhazhai\Toosl\code\metadata_json\output'

    for name in os.listdir(input_file_path):
        file_path = os.path.join(input_file_path,name)
        input_file_list.append(file_path)

    get_json.process_file_list(input_file_list, output_dir)


    # style = {'NeutralChat': ['3000000001-3000000500'], 'NeutralCustomerService': ['4000000001-4000000500'], 'Cheerfulchat': ['9130000001-9130000500'], 'CheerfulCustomerService': ['9140000001-9140000500']}

    # output_dir = r'C:\Users\v-zhazhai\Toosl\code\metadata_json\output'
    # wave_list = r"C:\Users\v-zhazhai\Toosl\code\metadata_json\output\ArEGShaKir.txt"
    # for names in style:
    #     uttid = get_json.get_styleWave(names,style,wave_list,"ArEGShaKir")
