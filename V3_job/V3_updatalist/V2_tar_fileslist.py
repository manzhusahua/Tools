"""
Updata V3 chunk data list
"""
import os,sys

class UPDATALIST():

    def __init__(self) -> None:
        super().__init__()

    def get_filelist(self,chunkpath,outputdir):
        if not os.path.exists(outputdir):
            os.makedirs(outputdir, exist_ok=True)
        with open(os.path.join(outputdir,"all.txt"),'w',encoding='utf8') as s:
            for home, dirs, files in os.walk(chunkpath):
                for filename in files:
                    s.writelines(os.path.join(home, filename)+'\n')
        return os.path.join(outputdir,"all.txt")

CHUNK_INPUT_STEP = None

def init():

    global CHUNK_INPUT_STEP
    CHUNK_INPUT_STEP = UPDATALIST()

    CHUNK_INPUT_STEP.prs_step_init()

def run(mini_batch):

    return CHUNK_INPUT_STEP.prs_step_run(mini_batch)

if __name__ == "__main__":
    inputdir = sys.argv[1]
    outputdir = sys.argv[2]
    # inputdir = "/mnt/c/Users/v-zhazhai/Downloads/realisticttsdataset_v3_scu/train"
    # outputdir = "/mnt/c/Users/v-zhazhai/Downloads/realisticttsdataset_v3/train"
    UpdataList = UPDATALIST()
    UpdataList.get_filelist(inputdir,outputdir)