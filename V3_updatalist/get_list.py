"""
Updata V3 chunk data list
"""
import os

class UPDATALIST():

    def __init__(self) -> None:
        super().__init__()

    def get_filelist(self,chunkpath,outputdir):
        list_path = outputdir
        with open(os.path.join(list_path,"allfilelist.txt"),'w',encoding='utf8') as s:
            for home, dirs, files in os.walk(chunkpath):
                for filename in files:
                    if ".json" in filename and ".json.version" not in filename:
                        s.writelines(os.path.join(home, filename)+'\n')
        return os.path.join(list_path,"allfilelist.txt")
    
    def split_locals(self,tierlist,Tier_path):
        locals = []
        for line in tierlist:
            n = [x for x in line.replace("\\",'/').split('/') if "tier" in x][0]
            local = line.replace("\\",'/').split('/')[line.replace("\\",'/').split('/').index(n)+1]
            if local not in locals:
                locals.append(local)
        for line in locals:
            local_path = os.path.join(Tier_path,line)
            local_word = [x for x in tierlist if line in x]
            # print(local_path)
            if not os.path.exists(local_path):
                os.makedirs(local_path, exist_ok=True)
            with open(os.path.join(local_path,"allfilelist.txt"),'w',encoding='utf8') as s:
                for line in local_word:
                    line = line.replace('\n','')
                    s.writelines(line+'\n')
            s.close()

    def split_Tier(self,listfile):
        save_path = os.path.split(listfile)[0]
        f = open(listfile,'r',encoding='utf8')
        word = f.readlines()

        n= 1
        while n<=3:
            tier = [x for x in word if "tier{}".format(str(n)) in x]
            Tier_path = os.path.join(save_path,"tier{}".format(str(n)))
            if not os.path.exists(Tier_path):
                os.makedirs(Tier_path, exist_ok=True)
            with open(os.path.join(Tier_path,"allfilelist.txt"),'w',encoding='utf8') as s:
                s.writelines(tier)
            s.close()
            self.split_locals(tier,Tier_path)
            n+=1
                

    def run(self,chunkpath,outputdir):
        listfile = self.get_filelist(chunkpath,outputdir)
        self.split_Tier(listfile)


CHUNK_INPUT_STEP = None

def init():

    global CHUNK_INPUT_STEP
    CHUNK_INPUT_STEP = UPDATALIST()

    CHUNK_INPUT_STEP.prs_step_init()

def run(mini_batch):

    return CHUNK_INPUT_STEP.prs_step_run(mini_batch)

if __name__ == "__main__":
    # inputdir = r"C:\Users\v-zhazhai\Toosl\updata_list\realisticttsdataset_v3\train\chunks"
    # outputdir = r"C:\Users\v-zhazhai\Toosl\updata_list\realisticttsdataset_v3\train"
    # tierlist = [r"C:\Users\v-zhazhai\Toosl\updata_list\realisticttsdataset_v3\train\chunks\tier2\ar-eg\ttsdata\ArEGHoda\chunk_ar-eg_ArEGHoda_0.json\n",r"C:\Users\v-zhazhai\Toosl\updata_list\realisticttsdataset_v3\train\chunks\tier2\ar-eg\ttsdata\ArEGHoda\chunk_ar-eg_ArEGHoda_1.json\n"]

    # Tier_path = r"C:\Users\v-zhazhai\Toosl\updata_list\realisticttsdataset_v3\train\dataset\tier2"
    UpdataList = UPDATALIST()
    # UpdataList.run(inputdir,outputdir)