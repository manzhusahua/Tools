import os
import codecs 
import chardet

class MERGERDIR():

    def __init__(self) -> None:
        super().__init__()

    def merger_files(self,inpudir):
        with open(inpudir+'.txt','w',encoding='utf8') as s:
            for name in os.listdir(inpudir):
                content=codecs.open(os.path.join(inpudir,name),'rb').read()
                f = open(os.path.join(inpudir,name),'r',encoding=chardet.detect(content)['encoding']).read()
                s.writelines(f+'\n') 

INPUT_STEP = None

def init():

    global INPUT_STEP
    INPUT_STEP = MERGERDIR()

    INPUT_STEP.prs_step_init()

def run(mini_batch):

    return MERGERDIR.prs_step_run(mini_batch)

if __name__ == "__main__":
    merger_dir = MERGERDIR()

    inpudir = r"C:\Users\v-zhazhai\Downloads\filenames_set_output"
    outputdir = r"C:\Users\v-zhazhai\Downloads\zh-CN\zhCN_140k"
    merger_dir.merger_files(inpudir)