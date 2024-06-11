import os,sys


class MERGER_CHUNK():
    def __init__(self) -> None:
        super().__init__()
    
    def init(self, snapshot_dir="", resource_dir_dict={}, arg_list=[]):
        self.input_tier = str(arg_list[arg_list.index("--input_tier") + 1])
        self.input_local = str(arg_list[arg_list.index("--input_local") + 1])
        self.input_dataset = str(arg_list[arg_list.index("--input_dataset") + 1])
        self.input_domain = ""
        if arg_list and "--input_domain" in arg_list:
            self.input_domain = arg_list[arg_list.index("--input_domain") + 1]
    
    def process_a_chunk(self, chunk_dir, output_dir):
        try:
            if self.input_domain != "":
                save_path = os.path.join(output_dir,self.input_tier,self.input_local,self.input_dataset,self.input_domain)
            else:
                save_path = os.path.join(output_dir,self.input_tier,self.input_local,self.input_dataset)
        except Exception as e:
            self.logger.info(f"Failed to mkdir floder {save_path} due to {e}")
        
        if not os.path.exists(save_path):
            os.makedirs(save_path, exist_ok=True)
        # print(save_path)
        os.system("copy {} {}".format(chunk_dir,save_path))
        

CHUNK_INPUT_STEP = None

def init():

    global CHUNK_INPUT_STEP
    CHUNK_INPUT_STEP = MERGER_CHUNK()

    CHUNK_INPUT_STEP.prs_step_init()

def run(mini_batch):

    return CHUNK_INPUT_STEP.prs_step_run(mini_batch)

if __name__ == "__main__":
    merger_chunk = MERGER_CHUNK()
    arg_list = [
        "--input_tier", "tier1",
        "--input_local", "zh-cn",
        "--input_dataset", "XMLY",
        "--input_domain", ""
    ]

    merger_chunk.init(arg_list=arg_list)

    chunk_dir = sys.argv[1]
    output_dir = sys.argv[2]

    # chunk_dir = r"C:\Users\v-zhazhai\debug\ASR\data"
    # output_dir = r"C:\Users\v-zhazhai\debug\ASR"
    merger_chunk.process_a_chunk(chunk_dir,output_dir)