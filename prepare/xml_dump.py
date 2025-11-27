import os
import codecs
import chardet
import pandas as pd
import csv
import glob
import html
import re
"""
准备xml
"""

class XMLDUMP():
    def __init__(self) -> None:
        super().__init__()
    def add_lang_tags(self, text, chunk_locale):
        if chunk_locale == "zh-cn":
            text_new = html.escape(text.replace('\n','')).replace('&#x27;',"\'")
            if re.compile(r'[a-zA-Z]+').search(text_new):
                add_tags = re.sub(r'([a-zA-Z&;]+)', r"<lang xml:lang='en-US'>\1</lang>", text_new)
                result = "<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xmlns:mstts='https://www.w3.org/2001/mstts' xml:lang='zh-CN'><voice name='Microsoft Server Speech Text to Speech Voice (zh-CN, YunyangNeural)'>{}</voice></speak>".format(add_tags).replace("</lang>'<lang xml:lang='en-US'>","\'")
            else:
                result = text_new
        else:
            result = text
        return result
        
    def process_a_filelist(self, input_dir, output_dir):
        data_frame = None
        for file_path in glob.glob(os.path.join(input_dir, "**", "*.txt"), recursive=True):
            content=codecs.open(file_path,'rb').read()
            word = open(file_path,'r',encoding=chardet.detect(content)['encoding']).readlines()
            # word = open(file_path,'r',encoding='utf8').readlines()
            
            
            for line in word:
                text = line.split('\t')[-1].replace('\n','')
                newtext = self.add_lang_tags(text,"zh-cn")
                row_values = {
                            # "wav": [name.replace('.txt','.wav')],
                            "wav": [line.split('\t')[0].replace('.wav','')],
                            # "text": [text],
                            "text": [newtext],
                            "textless": ["false"],
                            "human_voice": ["true"],
                            "multispeaker_detect_score": ["-9999"],
                        }
                if data_frame is None:
                    data_frame = pd.DataFrame(row_values)
                else:
                    newdata = pd.DataFrame(row_values)
                    data_frame = pd.concat([data_frame, newdata], axis=0, ignore_index=True)
        meta_file = os.path.join(output_dir, "metadata.csv")
        data_frame.to_csv(meta_file, sep="|", encoding="utf-8", index=False, quoting=csv.QUOTE_MINIMAL,escapechar='|')

    def process_a_filelists(self, input_dir, output_dir):
        data_frame = None
        for file_path in glob.glob(os.path.join(input_dir, "**", "*.txt"), recursive=True):
            content=codecs.open(file_path,'rb').read()
            word = open(file_path,'r',encoding=chardet.detect(content)['encoding']).readlines()
            row_values = {
                "wav": [os.path.basename(file_path).replace('.txt','')],
                "text": [word[0].replace('\n','')],
                "textless": ["false"],
                "human_voice": ["true"],
                "multispeaker_detect_score": ["-9999"],
                }
            if data_frame is None:
                data_frame = pd.DataFrame(row_values)
            else:
                newdata = pd.DataFrame(row_values)
                data_frame = pd.concat([data_frame, newdata], axis=0, ignore_index=True)
        meta_file = os.path.join(output_dir, "metadata.csv")
        data_frame.to_csv(meta_file, sep="|", encoding="utf-8", index=False, quoting=csv.QUOTE_MINIMAL,escapechar='|')
    
    def process_a_file(self, file_dir):
        data_frame = None
        content=codecs.open(file_dir,'rb').read()
        with open(file_dir,'r',encoding=chardet.detect(content)['encoding']) as f:
            for line in f.readlines():
                text = line.split('\t')[-1].replace('\n','')
                newtext = self.add_lang_tags(text,"zh-cn")
                print(newtext)
                row_values = {
                        "wav": [line.split('\t')[0]],
                        # "text": [line.split('\t')[-1].replace('\n','')],
                        "text": [newtext],
                        "textless": ["false"],
                        "human_voice": ["true"],
                        "multispeaker_detect_score": ["-9999"],
                        }
                if data_frame is None:
                    data_frame = pd.DataFrame(row_values)
                else:
                    newdata = pd.DataFrame(row_values)
                    data_frame = pd.concat([data_frame, newdata], axis=0, ignore_index=True)
        meta_file = os.path.join(os.path.split(file_dir)[0], "metadata.csv")
        data_frame.to_csv(meta_file, sep="|", encoding="utf-8", index=False, quoting=csv.QUOTE_MINIMAL,escapechar='|')

INPUT_STEP = None

def init():

    global INPUT_STEP
    INPUT_STEP = XMLDUMP()

    INPUT_STEP.prs_step_init()

def run(mini_batch):

    return INPUT_STEP.prs_step_run(mini_batch)

if __name__ == "__main__":
    xml_dump = XMLDUMP()

    input_dir = r"C:\Users\v-zhazhai\Downloads\xpboy\shao3.txt"
    # output_dir = r"C:\Users\v-zhazhai\Downloads\input\xiaoxin_shi_zhcn_40"
    xml_dump.process_a_file(input_dir)