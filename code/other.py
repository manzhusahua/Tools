import codecs
import chardet
import os

class OtherTools():
    def __init__(self) -> None:
        super().__init__()
    
    def split_txtfile_to_txtfiles(self,inputfile,outputdir):
        """
        将trans文件拆分成单个id的trans文件
        """
        if not os.path.exists(outputdir):
            os.makedirs(outputdir, exist_ok=True)
        
        content=codecs.open(inputfile,'rb').read()
        word = open(inputfile,'r',encoding=chardet.detect(content)['encoding']).readlines()
        for line in word:
            with open(os.path.join(outputdir,line.split('\t')[0]+'.txt'),'w',encoding='utf8') as s:
                s.writelines(line.split('\t')[-1])

    def rename_file(self,inputdir,outputdir,word):
        for line in os.listdir(inputdir):
            os.renames(os.path.join(inputdir,line),os.path.join(outputdir,line.replace(word,'')))
INPUT_STEP = None

def init():

    global INPUT_STEP
    INPUT_STEP = OtherTools()

    INPUT_STEP.prs_step_init()

def run(mini_batch):

    return INPUT_STEP.prs_step_run(mini_batch)

if __name__ == "__main__":
    Other_Tools = OtherTools()
    
    
    inputfile = r"C:\Users\v-zhazhai\Downloads\EMNS\raw_webm_wave"
    outputdir = r"C:\Users\v-zhazhai\Downloads\output"
    
    Other_Tools.rename_file(inputfile,inputfile,".webm")