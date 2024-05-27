import os
import codecs
import chardet


class V3Prepare:
    def __init__(self) -> None:
        super().__init__()

    def get_text(self,filepath,outputdir):
        if os.path.isdir(filepath):
            for filename in os.listdir(filepath):
                file_path = os.path.join(filepath,filename)
                content=codecs.open(file_path,'rb').read()
                word = open(file_path,'r',encoding=chardet.detect(content)['encoding']).readlines()
                for line in word:
                    name = line.split('\t')[0]
                    save_path = os.path.join(outputdir,name)
                    if not os.path.exists(save_path):
                        os.makedirs(save_path, exist_ok=True)
                    with open(os.path.join(save_path,name+'.txt'),'w',encoding='utf8') as s:
                        s.writelines(line.split('\t')[-1])
        else:
            content=codecs.open(filepath,'rb').read()
            word = open(filepath,'r',encoding=chardet.detect(content)['encoding']).readlines()
            for line in word:
                name = line.split('\t')[0]
                save_path = os.path.join(outputdir,name)
                if not os.path.exists(save_path):
                    os.makedirs(save_path, exist_ok=True)
                with open(os.path.join(outputdir,name+'.txt'),'w',encoding='utf8') as s:
                    s.writelines(line.split('\t')[-1])
    
    def get_audio(self,inputdir,outputdir):
        for name in os.listdir(inputdir):
            save_path = os.path.join(outputdir,name.replace('.wav',''))
            if not os.path.exists(save_path):
                os.makedirs(save_path, exist_ok=True)
            os.system("copy "+os.path.join(inputdir,name)+" "+os.path.join(save_path,name))
            # if os.path.isdir(wave_files):
            #     for wavename in os.listdir(wave_files):
            #         save_path = os.path.join(wave_files,wavename)
            #         if not os.path.exists(save_path):
            #             os.makedirs(save_path, exist_ok=True)
            #         os.system("copy "+os.path.join(save_path,wavename))
                

INPUT_STEP = None

def init():

    global INPUT_STEP
    INPUT_STEP = V3Prepare()

    INPUT_STEP.prs_step_init()

def run(mini_batch):

    return INPUT_STEP.prs_step_run(mini_batch)

if __name__ == "__main__":
    inputdir = r"C:\Users\v-zhazhai\Downloads\TextScripts"
    waveputdir = r"C:\Users\v-zhazhai\Downloads\wave"
    outputdir = r"C:\Users\v-zhazhai\Downloads\wave"

    V3_Prepare = V3Prepare()
    V3_Prepare.get_text(inputdir,outputdir)
    # V3_Prepare.get_audio(inputdir)