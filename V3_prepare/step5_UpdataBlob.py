
import os

class step5:
    def __init__(self) -> None:
        super().__init__()

    def step5_updata_tts_filelist(self,local,files_path,batch):
        input_path = "\\".join([files_path,"v3",'step3_extract_tts_filelist',batch+'.txt'])
        token = r'?sv=2023-01-03&se=2024-05-17T03%3A16%3A56Z&sr=c&sp=rwl&sig=dl6TCBSIttrShrUPUtcCh%2FLKwrIJJR3BoqmRZ%2BOJPF0%3D'
        updata_tts_filelist = 'C:/Users/v-zhazhai/Toosl/Tools/azcopy.exe copy "{}" "https://speechdatacrawlrgwusdiag.blob.core.windows.net/rawpublicdata/TTS_filelist/{}/{}{}" --overwrite=false'.format(input_path,local,batch+'.txt',token)
        print(updata_tts_filelist)
        os.system(updata_tts_filelist)
    
    def step5_updata_dump_json(self,local,files_path,batch):
        input_path = "\\".join([files_path,batch,'*'])
        token = r'?sv=2023-01-03&ss=btqf&srt=sco&st=2024-04-19T07%3A41%3A52Z&se=2024-04-20T07%3A41%3A52Z&sp=rwdxftlacup&sig=Cs8b89cF%2F7p4A%2FLq%2FJOm7Gi0oj1fAg6gX3Xe3BlRhvw%3D'
        updata_dump_json = 'C:/Users/v-zhazhai/Toosl/Tools/azcopy.exe copy {} "https://stdstoragettsdp01wus2.blob.core.windows.net/data/TTS_ChunkData/{}/YouTube/v3/YouTube_temp/{}/{}" --overwrite=false'.format(input_path,local,batch,token)
        print(updata_dump_json)
        os.system(updata_dump_json)

if __name__ == "__main__":
    step5 = step5()
    locals = "fr-FR"
    files_path = r"C:\Users\v-zhazhai\Downloads"
    batch_count = 15
    # step5.step5_updata_tts_filelist(locals,files_path)
    step5.step5_updata_dump_json(locals,files_path,batch_count)