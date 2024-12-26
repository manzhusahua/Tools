import codecs
import chardet

class READFILE():
    def __init__(self) -> None:
        super().__init__()
    
    def read_file(self,file_path):
         content=codecs.open(file_path,'rb').read()
         word = open(file_path,'r',encoding=chardet.detect(content)['encoding']).readlines()
         return word


INPUT_STEP = None

def init():

    global INPUT_STEP
    INPUT_STEP = READFILE()

    INPUT_STEP.prs_step_init()

def run(mini_batch):

    return INPUT_STEP.prs_step_run(mini_batch)

if __name__ == "__main__":
    read_file = READFILE()
    import numpy as np
    # word = read_file.read_file(r"C:\Users\v-zhazhai\Downloads\ms_score1")[0]
    # # data = np.loadtxt(r"C:\Users\v-zhazhai\Downloads\ms_score1")
    # print(np.fromfile(r"C:\Users\v-zhazhai\Downloads\ms_score1"))
    # print(np.fromfile(r"C:\Users\v-zhazhai\Downloads\ms_score2"))
    