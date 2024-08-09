
import os

class step5:
    def __init__(self) -> None:
        super().__init__()
    def init(self, snapshot_dir="", resource_dir_dict={}, arg_list=[]):
        self.token1 = resource_dir_dict["--token1"] 
        self.token2 = resource_dir_dict["--token2"] 

    def step5_updata_tts_filelist(self,local,files_path,batch):
        input_path = "\\".join([files_path,"v3",'step3_extract_tts_filelist',batch+'.txt'])
        updata_tts_filelist = 'C:/Users/v-zhazhai/Toosl/Tools/azcopy.exe copy "{}" "https://speechdatacrawlrgwusdiag.blob.core.windows.net/rawpublicdata/TTS_filelist/{}/{}{}" --overwrite=false'.format(input_path,local,batch+'.txt',self.token1)
        print(updata_tts_filelist)
        os.system(updata_tts_filelist)
    
    def step5_updata_dump_json(self,local,files_path,batch):
        input_path = "\\".join([files_path,batch,'*'])
        updata_dump_json = 'C:/Users/v-zhazhai/Toosl/Tools/azcopy.exe copy {} "https://stdstoragettsdp01wus2.blob.core.windows.net/data/TTS_ChunkData/{}/YouTube/v3/YouTube_temp/{}/{}" --overwrite=false'.format(input_path,local,batch,self.token2)
        print(updata_dump_json)
        os.system(updata_dump_json)

if __name__ == "__main__":
    step5 = step5()
    locals = "fr-FR"
    files_path = r"C:\Users\v-zhazhai\Downloads"
    batch_count = 15
    # step5.step5_updata_tts_filelist(locals,files_path)
    step5.step5_updata_dump_json(locals,files_path,batch_count)