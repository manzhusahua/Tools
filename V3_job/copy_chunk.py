"""
use copy chunk files
"""


import os,sys
import shutil
import multiprocessing


class CopyChunk():
    def __init__(self) -> None:
        super().__init__()
    
    def process_a_chunk(self, chunkpath, output_dir):
        """
        Args:
            chunk (str): input chunk
            output_dir (str): copy to path
        """
        chunk_names = []
        for home, dirs, files in os.walk(chunkpath):
                for filename in files:
                    if ".json" in filename and ".json.version" not in filename:
                        if filename.split('.')[0] not in chunk_names:
                            chunk_names.append(filename.split('.')[0])
        for line in chunk_names:
            print("copy \""+os.path.join(chunkpath,line+".*")+"\" \""+output_dir+"\"")
            os.system("copy \""+os.path.join(chunkpath,line+".*")+"\" \""+output_dir+"\"")

    def base_list(self, filelist,savepath,st,et):
        allowed_suffix = [".audio",".audio_48k_denoised",".coarse_segment",".fine_segment",".info",".json",".richland_result",".transcription"]
        word = open(filelist,'r',encoding='utf8').readlines()
        
        for line in word[st:et]:
            chunk_name = os.path.basename(line).split(".json")[0]
            print("start : ",line)
            for suffix in allowed_suffix:
                save_path = os.path.join(savepath,os.path.split(line)[0].replace("realisticttsdataset_v3/train/chunks/tier1/zh-cn/youtube/",''))
                if os.path.exists(os.path.join(os.path.split(line)[0],chunk_name+suffix)):
                    shutil.copyfile(os.path.join(os.path.split(line)[0],chunk_name+suffix),os.path.join(save_path,chunk_name+suffix))
     
INPUT_STEP = None

def init():

    global INPUT_STEP
    INPUT_STEP = CopyChunk()

    INPUT_STEP.prs_step_init()

def run(mini_batch):

    return INPUT_STEP.prs_step_run(mini_batch)

if __name__ == "__main__":
    copy_chunk = CopyChunk()

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    # input_dir = "/mnt/c/Users/v-zhazhai/Desktop/YouTube_list_20250126.txt"
    # output_dir = "realisticttsdataset_v3/train/chunks/tier1/zh-cn/youtube/"
    # copy_chunk.base_list(input_dir,output_dir,0,10)
    
    count = int(91068/5)
    path1 = multiprocessing.Process(target=copy_chunk.base_list,args=(count*0,count*1))
    path1.start()

    path2 = multiprocessing.Process(target=copy_chunk.base_list,args=(count*1,count*2))
    path2.start()

    path3 = multiprocessing.Process(target=copy_chunk.base_list,args=(count*2,count*3))
    path3.start()

    path4 = multiprocessing.Process(target=copy_chunk.base_list,args=(count*3,count*4))
    path4.start()

    path5 = multiprocessing.Process(target=copy_chunk.base_list,args=(count*4,count*5))
    path5.start()