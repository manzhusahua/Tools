import os
import codecs
import chardet
import pandas as pd
import csv
import glob

"""
准备xml
"""

class XMLDUMP():
    def __init__(self) -> None:
        super().__init__()
    
    def process_a_filelist(self, input_dir, output_dir):
        data_frame = None
        for file_path in glob.glob(os.path.join(input_dir, "**", "*.txt"), recursive=True):
            content=codecs.open(file_path,'rb').read()
            word = open(file_path,'r',encoding=chardet.detect(content)['encoding']).readlines()
            # word = open(file_path,'r',encoding='utf8').readlines()
            
            
            for line in word:
                text = line.split('\t')[-1].replace('\n','')
                row_values = {
                            # "wav": [name.replace('.txt','.wav')],
                            "wav": [line.split('\t')[0].replace('.wav','')],
                            "text": [text],
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
        with open(file_dir,'r',encoding='utf8') as f:
            for line in f.readlines():
                row_values = {
                        "wav": [line.split('\t')[0]],
                        "text": [line.split('\t')[-1].replace('\n','')],
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

    input_dir = r"C:\Users\v-zhazhai\Desktop\YFD-zh_cn\4f5330c5-af9d-4552-a689-6f3df78177de.txt"
    # output_dir = r"C:\Users\v-zhazhai\Downloads\input\xiaoxin_shi_zhcn_40"
    xml_dump.process_a_file(input_dir)