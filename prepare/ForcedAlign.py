"""
修改xml用于ForcedAlign run
"""
import os
import codecs
import chardet
import pandas as pd
import csv


class ForcedAlign():
    def __init__(self) -> None:
        super().__init__()
    
    def process_a_filelist(self, input_dir, output_dir):
        file_path = os.path.join(input_dir,"4_XmlScriptWithPron_AddDot")
        for name in os.listdir(file_path):
            xml_path = os.path.join(file_path,name)
            save_path = os.path.join(output_dir,"4_XmlScriptWithPron_AddDot",name.replace('.xml',"_v1.xml"))
            content=codecs.open(xml_path,'rb').read()
            word = open(xml_path,'r',encoding=chardet.detect(content)['encoding']).readlines()
            # word = open(file_path,'r',encoding='utf8').readlines()
            with open(save_path,'w',encoding=chardet.detect(content)['encoding']) as s:
                for line in word:
                    if "text_beforeTN" not in line:
                        s.writelines(line)
        
INPUT_STEP = None

def init():

    global INPUT_STEP
    INPUT_STEP = ForcedAlign()

    INPUT_STEP.prs_step_init()

def run(mini_batch):

    return INPUT_STEP.prs_step_run(mini_batch)

if __name__ == "__main__":
    xml_dump = ForcedAlign()

    input_dir = r"D:\users\v-zhazhai\TTS\zh-CN\yinbiao\data\xiaochen\mixligual"
    output_dir = r"D:\users\v-zhazhai\TTS\zh-CN\yinbiao\data\xiaochen"
    xml_dump.process_a_filelist(input_dir,input_dir)