""""
进行语言检测
"""

import langid
import glob
import os
import codecs
import chardet
import numpy as np


# word = 'મિત્રો સ્ટાર.'

# locals = str(langid.classify(word)).split(",")[0].replace('(','')
# print(locals)
def LanguageDetection(segnmentdir,locals):
    count = len(glob.glob(os.path.join(segnmentdir, "**", "segment_transcription"), recursive=True))
    not_locals = 0
    for file_path in glob.glob(os.path.join(segnmentdir, "**", "segment_transcription"), recursive=True):
        content=codecs.open(file_path,'rb').read()
        word = open(file_path,'r',encoding=chardet.detect(content)['encoding']).readlines()[0]
        word_local = str(langid.classify(word)).split(",")[0].replace('(','').replace("'","")
        if word_local != locals:
            print(f"{word}\t{word_local}\t{file_path}")
            not_locals+=1
        
    return not_locals/count
    
if __name__ == "__main__":
    rato_list = []
    inputdir = r"C:\Users\v-zhazhai\Downloads\batch02"
    for line in os.listdir(inputdir):
        if "coarse_segment_files" in line:
            rato = LanguageDetection(os.path.join(inputdir,line),"gu")
            rato_list.append(rato)
    print(str(round(np.mean(rato_list), 3)))
