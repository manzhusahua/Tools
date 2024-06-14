import os


"""
准备audio_text_segmetation 的输入文件
input: *.wav *.txt
output: ID/audio/ID.wav
        ID/text/ID.txt
"""

class PREPARINPUDIR():
    def __init__(self) -> None:
        super().__init__()


    def audio_dir(self, input_audio_file):
        for audio_file in input_audio_file:
            name = os.path.basename(audio_file).replace('.wav','')
            
            audio_path = os.path.join(os.path.split(audio_file)[0], name, 'audio')
            
            if not os.path.exists(audio_path):
                os.makedirs(audio_path, exist_ok=True)
            
            os.renames(audio_file,
                       os.path.join(audio_path,os.path.basename(audio_file)))
    
    def text_dir(self,input_txt_file):
        for text_file in input_txt_file:
            name = os.path.basename(text_file).replace('.txt','')
            
            audio_path = os.path.join(os.path.split(text_file)[0], name, 'text')
            
            if not os.path.exists(audio_path):
                os.makedirs(audio_path, exist_ok=True)
            
            os.renames(text_file,
                       os.path.join(audio_path,os.path.basename(text_file)))
            
    def process_a_filelist(self, input_dir,output_dir):
        input_audio_file = []
        input_txt_file = []
        files_list = []
        for input_file in os.listdir(input_dir):
            if ".wav" in input_file:
                input_audio_file.append(os.path.join(input_dir,input_file))
            if ".txt" in input_file:
                input_txt_file.append(os.path.join(input_dir,input_file))
                files_list.append("/".join([input_file.replace('.txt',''),'text',input_file]))

        self.audio_dir(input_audio_file)
        self.text_dir(input_txt_file)
        with open(os.path.join(output_dir,"filenames.txt"),'w',encoding='utf8') as s:
            for line in files_list:
                s.writelines(line+'\n')



INPUT_STEP = None

def init():

    global INPUT_STEP
    INPUT_STEP = PREPARINPUDIR()

    INPUT_STEP.prs_step_init()

def run(mini_batch):

    return INPUT_STEP.prs_step_run(mini_batch)

if __name__ == "__main__":
    prepare_dir = PREPARINPUDIR()

    input_dir = r"C:\Users\v-zhazhai\Desktop\audio_conversion_16k\speech"
    output_dir = r"C:\Users\v-zhazhai\Desktop\audio_conversion_16k"
    prepare_dir.process_a_filelist(input_dir,output_dir)