import os
import codecs 
import chardet
import glob

class MERGERDIR():

    def __init__(self) -> None:
        super().__init__()

    def merger_files(self,inpudir):
        with open(inpudir+'.txt','w',encoding='utf8') as s:
            for name in glob.glob(os.path.join(inpudir, "**", "*.txt"), recursive=True):
            # for names in os.listdir(inpudir):
                if ".txt" in name:
                    # name = os.path.join(inpudir,names)
                    content=codecs.open(name,'rb').read()
                    f = open(name,'r',encoding=chardet.detect(content)['encoding']).read()
                    # s.writelines(f+'\n') 
                    s.writelines(f) 
    def merger_files2(self,inpudir):
        words = []
        with open(inpudir+'.txt','w',encoding='utf8') as s:
            for name in glob.glob(os.path.join(inpudir, "**", "*.txt"), recursive=True):
                if ".txt" in name:
                    content=codecs.open(name,'rb').read()
                    f = open(name,'r',encoding=chardet.detect(content)['encoding']).readlines()
                    for line in f:
                        if line not in words:
                            words.append(line)
                            s.writelines(line)
INPUT_STEP = None

def init():

    global INPUT_STEP
    INPUT_STEP = MERGERDIR()

    INPUT_STEP.prs_step_init()

def run(mini_batch):

    return MERGERDIR.prs_step_run(mini_batch)

if __name__ == "__main__":
    merger_dir = MERGERDIR()

    inpudir = r"C:\Users\v-zhazhai\Desktop\en-us_youtube\20250226"
    outputdir = r"C:\Users\v-zhazhai\Downloads\zh-CN\zhCN_140k"
    merger_dir.merger_files(inpudir)