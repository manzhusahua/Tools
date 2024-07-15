"""
use copy chunk files
"""


import os,sys
import json

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
    copy_chunk.process_a_chunk(input_dir,output_dir)