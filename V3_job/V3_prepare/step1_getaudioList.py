import os

class STEP1():
    def __init__(self) -> None:
        super().__init__()
    def init(self, snapshot_dir="", resource_dir_dict={}, arg_list=[]):
        self.token = resource_dir_dict["--token"]
        # self.inputdir = resource_dir_dict["--inputdir"]
        # self.locals = resource_dir_dict["--locals"]

    def step1_getaudioList(self,inputdir,locals):
        if not os.path.exists(inputdir):
            os.makedirs(inputdir, exist_ok=True)
        output_list = os.path.join(inputdir,locals+'.txt')
        word1 = 'C:/Users/v-zhazhai/Toosl/Tools/azcopy.exe list "https://speechdatacrawlrgwusdiag.blob.core.windows.net/rawpublicdata/{}/{}" > "{}"'.format(locals,self.token,output_list)
        print(word1)
        os.system(word1)
        return output_list
    
    def step1_download(self,output_list):
        locals = os.path.split(output_list)[-1].replace('.txt','')
        save_path =  '\\'.join(os.path.split(output_list)[:-1])

        with open(output_list,'r',encoding='utf8') as f,open(output_list.replace(".txt","_v1.txt"),'w',encoding='utf8') as s:
            for line in f.readlines()[2:]:
                line = line.split(";")[0].replace("INFO: ",'')
                if "audioList.txt" in line:

                    audioList ='/'.join([locals,line])
                    output_audioList = os.path.join(save_path,line.replace('/','\\'))

                    word1 = 'C:/Users/v-zhazhai/Toosl/code/Tool/merger_tar/azcopy.exe copy  "https://speechdatacrawlrgwusdiag.blob.core.windows.net/rawpublicdata/{}{}" "{}"'.format(audioList,self.token,output_audioList)
                    print(word1)
                    os.system(word1)

                    s.writelines(line+'\n')
    
    def run(self,inputdir,locals):
        # output_list = r"C:\Users\v-zhazhai\Desktop\TTS\pt-BR\YouTube\pt-BR.txt"
        output_list = self.step1_getaudioList(inputdir,locals)
        # self.step1_download(output_list)



WAVE_INPUT_STEP = None

def init():

    global WAVE_INPUT_STEP
    WAVE_INPUT_STEP = STEP1()

    WAVE_INPUT_STEP.prs_step_init()

def run(mini_batch):

    return WAVE_INPUT_STEP.prs_step_run(mini_batch)

if __name__ == "__main__":
    inputdir = r"C:\Users\v-zhazhai\Desktop\TTS\en-US\YouTube"
    locals =  "en-US"

    step1 = STEP1()
    step1.run(inputdir,locals)