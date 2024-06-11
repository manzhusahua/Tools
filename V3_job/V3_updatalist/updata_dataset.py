import os
import glob



class UPDATADDATEDET():
    def __init__(self) -> None:
        super().__init__()
    def run(self,inputdir,outputdir):
        file_extension = '.json'
        tiers = os.listdir(inputdir)
        for eachtier in tiers:
            eachtierpath = os.path.join(inputdir, eachtier)
            locales = os.listdir(eachtierpath)
            for eachlocale in locales:
                eachlocalepath = os.path.join(eachtierpath, eachlocale)
                datasets = os.listdir(eachlocalepath)
                for eachdataset in datasets:
                    eachdatasetpath = os.path.join(eachlocalepath, eachdataset)
                    domains = os.listdir(eachdatasetpath)
                    for eachdomain in domains:
                        eachdomainpath = os.path.join(eachdatasetpath, eachdomain)
                        outputpath = os.path.join(outputdir, eachtier, eachlocale, eachdataset, eachdomain)
                        if not os.path.isdir(outputpath):
                            os.makedirs(outputpath)
                        outputfile = os.path.join(outputpath, "filelist.txt")
                        for file in glob.glob(os.path.join(eachdomainpath, '*' + file_extension)):
                            with open(outputfile, 'a', encoding='UTF-8') as writer:
                                writer.write(file + "\n")

CHUNK_INPUT_STEP = None

def init():

    global CHUNK_INPUT_STEP
    CHUNK_INPUT_STEP = UPDATADDATEDET()

    CHUNK_INPUT_STEP.prs_step_init()

def run(mini_batch):

    return CHUNK_INPUT_STEP.prs_step_run(mini_batch)

if __name__ == "__main__":
    # inputdir = r"/datablob/realisticttsdataset_v3/train/chunks"
    #inputdir = r"D:\Work\unified_data_platform\v3\v3_filelist\generate_v3_filelist_wus2\root"
    # outputdir = r"/datablob/v-litfen/unified_dataplatform_v3/filelist/2024042901"
    #outputdir = r"D:\Work\unified_data_platform\v3\v3_filelist\generate_v3_filelist_wus2\root_out"
    # updata_dataset = UPDATADDATEDET()
    # updata_dataset.run()
    print()