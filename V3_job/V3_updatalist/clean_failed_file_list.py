import os
import codecs
import chardet


def clean_failed_file_list(inputdir):
    with open(inputdir, 'r', encoding='utf8') as f, open(inputdir.replace('.txt', '_clean.txt'), 'w', encoding='utf8') as s:
        for line in f.readlines():
            if "No such file or directory" in line:
                # s.writelines(line)
                # s.writelines(line.split(', [Errno 2]')[0]+'\n')
                s.writelines(line.split("'")[1]+'\n')


def get_list(inputfile):
    with open(inputfile,'r',encoding="utf8") as f,open(inputfile.replace(".txt","_clean.txt"),'w',encoding="utf8") as s:
        for line in f.readlines():
            if ".json" in line and ".version" not in line:
                s.writelines("/datablob/realisticttsdataset_v3/train/chunks/tier2/"+line.split(";  ")[0].replace("INFO: ","")+'\n')

def clean_file(inputfile,allfile):
    content=codecs.open(inputfile,'rb').read()
    word = open(inputfile,'r',encoding=chardet.detect(content)['encoding']).readlines()
    with open(allfile,'r',encoding="utf8") as f,open(inputfile.replace(".txt","_error.txt"),'w',encoding="utf8") as s:
        for line in f.readlines():
            if line not in word:
                s.writelines(line)
if __name__ == "__main__":
    
    # locals_list = ["de-de","en-au","en-ca","en-gb","en-us","es-es","es-mx","filelist","fr-ca","fr-fr","it-it","ja-jp","ko-kr","pt-br","tier2","tier3","tier3","zh-cn"]
    savedir = r"C:\Users\v-zhazhai\Desktop\datacheck"
    # clean_failed_file_list(r"C:\Users\v-zhazhai\Desktop\checkFilelist\stdstoragetts01scus\failed_file_list.txt")
    # for line in locals_list:
    #     download_failed_file(line,savedir)
    for line in os.listdir(savedir):
        clean_failed_file_list(os.path.join(savedir,line))
    # get_list(r"C:\Users\v-zhazhai\Desktop\datacheck\tier3.txt")
    # clean_file(r"C:\Users\v-zhazhai\Desktop\tier2_clean.txt",r"C:\Users\v-zhazhai\Environment\RealisticTTSDatasets\dataset\tier2\all.txt")
    datasets = []
    # with open(r"C:\Users\v-zhazhai\Downloads\all.txt",'r',encoding="utf8") as f,open(r"C:\Users\v-zhazhai\Downloads\all_clean.txt",'w',encoding="utf8") as s:
    #     for line in f.readlines():
    #         dataset = line.split("/chunk_")[0]
    #         if dataset not in datasets:
    #             datasets.append(dataset)
    #             s.writelines(dataset+'\n')