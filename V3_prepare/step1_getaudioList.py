import os

class STEP1():
    def __init__(self) -> None:
        super().__init__()
    # def init(self, snapshot_dir="", resource_dir_dict={}, arg_list=[]):
        # self.inputdir = resource_dir_dict["--inputdir"]
        # self.locals = resource_dir_dict["--locals"]
    
    def step1_getaudioList(self,inputdir,locals):
        token = r'?sv=2023-01-03&st=2024-04-30T07%3A39%3A57Z&se=2024-05-01T07%3A39%3A57Z&sr=c&sp=racwdxltf&sig=UPyPx0KXJ4xUjQ3V2nMmXGTmbYh9Kn38Ng6D4N20%2BuA%3D'

        output_list = os.path.join(inputdir,locals+'.txt')
        word1 = 'C:/Users/v-zhazhai/Toosl/code/Tool/merger_tar/azcopy.exe list  "https://speechdatacrawlrgwusdiag.blob.core.windows.net/rawpublicdata/{}/{}" > "{}"'.format(locals,token,output_list)
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

                    token = r'?sv=2023-01-03&st=2024-04-29T02%3A12%3A52Z&se=2024-05-31T02%3A12%3A00Z&sr=c&sp=racwdxltf&sig=y4qplet74XqfhN9o46HzSMXj29clJcj6faAc%2B1L5fYI%3D'

                    audioList ='/'.join([locals,line])
                    output_audioList = os.path.join(save_path,line.replace('/','\\'))

                    word1 = 'C:/Users/v-zhazhai/Toosl/code/Tool/merger_tar/azcopy.exe copy  "https://speechdatacrawlrgwusdiag.blob.core.windows.net/rawpublicdata/{}{}" "{}"'.format(audioList,token,output_audioList)
                    print(word1)
                    os.system(word1)

                    s.writelines(line+'\n')
    
    def run(self,inputdir,locals):
        # output_list = r"C:\Users\v-zhazhai\Desktop\TTS\pt-BR\YouTube\pt-BR.txt"
        output_list = self.step1_getaudioList(inputdir,locals)
        self.step1_download(output_list)



WAVE_INPUT_STEP = None

def init():

    global WAVE_INPUT_STEP
    WAVE_INPUT_STEP = STEP1()

    WAVE_INPUT_STEP.prs_step_init()

def run(mini_batch):

    return WAVE_INPUT_STEP.prs_step_run(mini_batch)

if __name__ == "__main__":
    inputdir = r"C:\Users\v-zhazhai\Desktop\TTS\pt-BR\YouTube"
    locals =  "pt-BR"

    step1 = STEP1()
    step1.run(inputdir,locals)