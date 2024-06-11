"""
获取json list 用于下一步的job
"""
import os,sys

class Get_Jon_List():

    def __init__(self) -> None:
        super().__init__()

    def get_filelist(self,chunkpath,outputdir):
        if not os.path.exists(outputdir):
            os.makedirs(outputdir, exist_ok=True)
        with open(os.path.join(outputdir,"filenames.txt"),'w',encoding='utf8') as s:
            for home, dirs, files in os.walk(chunkpath):
                for filename in files:
                    if ".json" in filename and ".json.version" not in filename:
                        s.writelines(filename+'\n')
        return os.path.join(outputdir,"filenames.txt")
    
    CHUNK_INPUT_STEP = None

def init():

    global CHUNK_INPUT_STEP
    CHUNK_INPUT_STEP = Get_Jon_List()

    CHUNK_INPUT_STEP.prs_step_init()

def run(mini_batch):

    return CHUNK_INPUT_STEP.prs_step_run(mini_batch)

if __name__ == "__main__":
    get_json_list = Get_Jon_List()
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    get_json_list.get_filelist(input_dir,output_dir)