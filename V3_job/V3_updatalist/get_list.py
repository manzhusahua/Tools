"""
Updata V3 chunk data list
"""
import os

class UPDATALIST():

    def __init__(self) -> None:
        super().__init__()

    def init(self, snapshot_dir="", resource_dir_dict={}, arg_list=[]):
        self.input_datas = "" if "--input_datas" not in arg_list else str(arg_list[arg_list.index("--input_datas") + 1])
        self.input_dataset = "" if "--input_dataset" not in arg_list else str(arg_list[arg_list.index("--input_dataset") + 1])
        self.input_locals = "" if "--input_locals" not in arg_list else str(arg_list[arg_list.index("--input_locals") + 1])
        self.input_Tier = "" if "--input_Tier" not in arg_list else str(arg_list[arg_list.index("--input_Tier") + 1])
        self.input_filter = [self.input_datas,
                             self.input_dataset,
                             self.input_locals,
                             self.input_Tier]

    def get_filelist(self,chunkpath,outputdir):
        if not os.path.exists(outputdir):
            os.makedirs(outputdir, exist_ok=True)
        with open(os.path.join(outputdir,"all.txt"),'w',encoding='utf8') as s:
            for home, dirs, files in os.walk(chunkpath):
                for filename in files:
                    if ".json" in filename and ".json.version" not in filename:
                        s.writelines(os.path.join(home, filename)+'\n')
        return os.path.join(outputdir,"all.txt")
    
    def split_datas(self,listfile,outputdir,tier,local,dataset):
        f = open(listfile,'r',encoding='utf8').readlines()
        datas = list(set([line.split("/")[line.split("/").index(dataset)+1] for line in f if dataset in line]))
        for data in datas:
            data_path = os.path.join(outputdir,tier,local,dataset,data)
            if not os.path.exists(data_path):
                os.makedirs(data_path, exist_ok=True)
            dataset_files = os.path.join(data_path,"filelist.txt")
            with open(dataset_files,'w',encoding='utf8') as s:
                for line in f:
                    if '/'.join([tier,local,dataset,data])+'/' in line:
                        s.writelines(line)
    
    def split_dataset(self,listfile,outputdir,tier,local):
        f = open(listfile,'r',encoding='utf8').readlines()
        datasets = list(set([line.split("/")[line.split("/").index(local)+1] for line in f]))
        for dataset in datasets:
            dataset_path = os.path.join(outputdir,tier,local,dataset)
            if not os.path.exists(dataset_path):
                os.makedirs(dataset_path, exist_ok=True)
            dataset_files = os.path.join(dataset_path,"all.txt")
            with open(dataset_files,'w',encoding='utf8') as s:
                for line in f:
                    if '/'.join([tier,local,dataset])+"/" in line :
                        s.writelines(line)
            try:
                self.split_datas(dataset_files,outputdir,tier,local,dataset)
            except Exception as e:
                errlocal = "_".join([tier,local])
                print(f"Failed to split {errlocal} dataset {e}")
                break
   
    def split_locals(self,listfile,outputdir,tier):
        f = open(listfile,'r',encoding='utf8').readlines()
        locals = list(set([line.split("/")[line.split("/").index(tier)+1] for line in f]))
        for local in locals:
            local_path = os.path.join(outputdir,tier,local)
            if not os.path.exists(local_path):
                os.makedirs(local_path, exist_ok=True)
            local_files = os.path.join(local_path,"all.txt")
            with open(local_files,'w',encoding='utf8') as s:
                for line in f:
                    if '/'.join([tier,local])+"/" in line:
                        s.writelines(line)
            self.split_dataset(local_files,outputdir,tier,local)

    def split_Tier(self,listfile,outputdir):
        f = open(listfile,'r',encoding='utf8').readlines()
        Tiers = list(set([line.split("/")[line.split("/").index("chunks")+1] for line in f]))
        for tier in Tiers:
            tier_path = os.path.join(outputdir,tier)
            if not os.path.exists(tier_path):
                os.makedirs(tier_path, exist_ok=True)
            tier_files = os.path.join(tier_path,str(tier)+".txt")
            with open(tier_files,'w',encoding='utf8') as s:
                for line in f:
                    if "/"+tier+"/" in line:
                        s.writelines(line)
            self.split_locals(tier_files,outputdir,tier)

    def run(self,inputdir,outputdir):
        # listfile = "/mnt/c/Users/v-zhazhai/Downloads/all.txt"
        listfile = self.get_filelist(inputdir,outputdir)
        self.split_Tier(listfile,outputdir)

    # def get_list(self,inputdir,outputdir):
    #     listfile = self.get_filelist(inputdir,outputdir)
    #     listword = open(listfile,'r',encoding='utf8').readlines()
    #     save_word = []
    #     for line in listword:
    #         for filter in self.input_filter:
    #             if "/"+filter+'/' in line:
    #                 if line


CHUNK_INPUT_STEP = None

def init():

    global CHUNK_INPUT_STEP
    CHUNK_INPUT_STEP = UPDATALIST()

    CHUNK_INPUT_STEP.prs_step_init()

def run(mini_batch):

    return CHUNK_INPUT_STEP.prs_step_run(mini_batch)

if __name__ == "__main__":

    inputdir = "/mnt/c/Users/v-zhazhai/Downloads/realisticttsdataset_v3_scu/train"
    outputdir = "/mnt/c/Users/v-zhazhai/Downloads/realisticttsdataset_v3/train"

    arg_list = ["--input_datas",'', "--input_dataset",'ttsdata', "--input_locals",'zh-cn', "--input_Tier",'']

    if not os.path.exists(outputdir):
        os.makedirs(outputdir, exist_ok=True)
    UpdataList = UPDATALIST()
    UpdataList.init("", "", arg_list)
    UpdataList.run(inputdir,outputdir)