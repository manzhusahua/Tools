
import os

class step5:
    def __init__(self) -> None:
        super().__init__()

    def step5_updata_tts_filelist(self,local,files_path):
        input_path = "\\".join([files_path,local,"v3",'step3_extract_tts_filelist'])
        for name in os.listdir(input_path):
            token = r'?sv=2023-01-03&se=2024-05-17T03%3A16%3A56Z&sr=c&sp=rwl&sig=dl6TCBSIttrShrUPUtcCh%2FLKwrIJJR3BoqmRZ%2BOJPF0%3D'
            updata_tts_filelist = 'C:/Users/v-zhazhai/Toosl/Tools/azcopy.exe copy "{}" "https://speechdatacrawlrgwusdiag.blob.core.windows.net/rawpublicdata/TTS_filelist/{}/{}{}" --overwrite=false'.format(os.path.join(input_path,name),local,name,token)
            print(updata_tts_filelist)
            os.system(updata_tts_filelist)
    
    def step5_updata_dump_json(self,local,files_path,batch_count):
        count = 1
        while count<=batch_count:
            input_path = "\\".join([files_path,local,"batch"+str(count).zfill(2),'*'])
            token = r'?sv=2023-01-03&ss=btqf&srt=sco&st=2024-04-17T06%3A55%3A16Z&se=2024-04-30T06%3A55%3A00Z&sp=rwdxftlacup&sig=7SK%2FqdvoWleqdM8%2BYC8KzszO%2FyqCTfO%2FU6HetTDXUws%3D'
            updata_dump_json = 'C:/Users/v-zhazhai/Toosl/Tools/azcopy.exe copy {} "https://stdstoragettsdp01scus.blob.core.windows.net/data/TTS_ChunkData/{}/YouTube/v3/YouTube_temp/batch{}/{}" --overwrite=false'.format(input_path,local,str(count).zfill(2),token)
            print(updata_dump_json)
            os.system(updata_dump_json)
            count+=1

if __name__ == "__main__":
    step5 = step5()
    locals = "fr-FR"
    files_path = r"C:\Users\v-zhazhai\Downloads"
    batch_count = 15
    # step5.step5_updata_tts_filelist(locals,files_path)
    step5.step5_updata_dump_json(locals,files_path,batch_count)