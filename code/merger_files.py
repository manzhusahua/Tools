import os
import codecs 
import chardet
import glob

class MERGERDIR():

    def __init__(self) -> None:
        super().__init__()

    def merger_files(self,inpudir):
        with open(inpudir+'.txt','w',encoding='utf8') as s:
            for name in os.listdir(inpudir):
                content=codecs.open(os.path.join(inpudir,name),'rb').read()
                f = open(os.path.join(inpudir,name),'r',encoding=chardet.detect(content)['encoding']).read()
                s.writelines(f+'\n') 
    def merge_files1(self,folder_path, output_file):
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                if os.path.isfile(file_path):
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        outfile.write(infile.read())
                        # outfile.write("\n")  # 添加换行符以分隔文件内容
    def merger_to_all(self,folder_path,output_file):
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for file in glob.glob(os.path.join(folder_path, "**", "*.txt"), recursive=True):
                content=codecs.open(file,'rb').read()
                f = open(file,'r',encoding=chardet.detect(content)['encoding']).read()
                outfile.writelines(f+'\n') 
INPUT_STEP = None

def init():

    global INPUT_STEP
    INPUT_STEP = MERGERDIR()

    INPUT_STEP.prs_step_init()

def run(mini_batch):

    return MERGERDIR.prs_step_run(mini_batch)

if __name__ == "__main__":
    merger_dir = MERGERDIR()

    inpudir = r"C:\Users\v-zhazhai\Downloads\dataset\tier4\uk-ua\podcast_rss"
    outputdir = r"C:\Users\v-zhazhai\Downloads\dataset\tier4\uk-ua\podcast_rss\all.txt"
    merger_dir.merger_to_all(inpudir,outputdir)