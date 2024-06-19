import os
import codecs
import chardet
import pandas as pd
import csv

"""
准备xml
"""

class XMLDUMP():
    def __init__(self) -> None:
        super().__init__()
    
    def process_a_filelist(self, input_dir, output_dir):
        data_frame = None

        for name in os.listdir(input_dir):
            file_path = os.path.join(input_dir,name)
            content=codecs.open(file_path,'rb').read()
            word = open(file_path,'r',encoding=chardet.detect(content)['encoding']).readlines()
            for line in word:
                wav_file_name = line.split('\t')[0]
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
        data_frame.to_csv(
            meta_file, sep="|", encoding="utf-8", index=False, quoting=csv.QUOTE_NONE
            )
INPUT_STEP = None

def init():

    global INPUT_STEP
    INPUT_STEP = XMLDUMP()

    INPUT_STEP.prs_step_init()

def run(mini_batch):

    return INPUT_STEP.prs_step_run(mini_batch)

if __name__ == "__main__":
    xml_dump = XMLDUMP()

    input_dir = r"C:\Users\v-zhazhai\Downloads\CaiQing\test"
    output_dir = r"C:\Users\v-zhazhai\Downloads\CaiQing"
    xml_dump.process_a_filelist(input_dir,output_dir)