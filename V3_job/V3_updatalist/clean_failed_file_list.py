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

def download_failed_file(locals,savedir):
    # download_word = fr'C:/Users/v-zhazhai/Toosl/code/Tool/merger_tar/azcopy.exe copy "https://stdstoragetts01eus.blob.core.windows.net/data/v-honzho/dataCheck/checkFilelist/{locals}/failed_file_list.txt?sv=2025-07-05&spr=https%2Chttp&st=2025-11-11T06%3A55%3A11Z&se=2025-11-12T06%3A55%3A11Z&skoid=c52a83f4-cefb-4d0c-a81d-a2747c46fd59&sktid=72f988bf-86f1-41af-91ab-2d7cd011db47&skt=2025-11-11T06%3A55%3A11Z&ske=2025-11-12T06%3A55%3A11Z&sks=b&skv=2025-07-05&sr=c&sp=racwdxltf&sig=C%2FFaOd49awtPr1VOKTgi4pblQnw22lfyneltl%2BKMlX0%3D" "{os.path.join(savedir,locals+".txt")}" --overwrite=false --check-md5 FailIfDifferent --from-to=BlobLocal  --recursive --trusted-microsoft-suffixes=stdstoragetts01eus.blob.core.windows.net --log-level=INFO'
    # download_word = fr'C:/Users/v-zhazhai/Toosl/code/Tool/merger_tar/azcopy.exe copy "https://stdstoragetts01wus2.blob.core.windows.net/data/v-honzho/dataCheck/checkFilelist/{locals}/failed_file_list.txt?sv=2025-07-05&spr=https%2Chttp&st=2025-11-11T07%3A01%3A42Z&se=2025-11-12T07%3A01%3A42Z&skoid=c52a83f4-cefb-4d0c-a81d-a2747c46fd59&sktid=72f988bf-86f1-41af-91ab-2d7cd011db47&skt=2025-11-11T07%3A01%3A42Z&ske=2025-11-12T07%3A01%3A42Z&sks=b&skv=2025-07-05&sr=c&sp=racwdxltf&sig=RB8NBlTYugNyTTO0%2F%2Fv4j6pENJjltevWdgSLuduMNPI%3D" "{os.path.join(savedir,locals+".txt")}" --overwrite=false --check-md5 FailIfDifferent --from-to=BlobLocal --recursive --trusted-microsoft-suffixes=stdstoragetts01wus2.blob.core.windows.net --log-level=INFO'
    download_word = fr'C:/Users/v-zhazhai/Toosl/code/Tool/merger_tar/azcopy.exe copy "https://stdstoragetts01wus3.blob.core.windows.net/data/v-honzho/dataCheck/checkFilelist/{locals}/failed_file_list.txt?sv=2025-07-05&st=2025-11-11T07%3A06%3A27Z&se=2025-11-18T07%3A21%3A27Z&skoid=c52a83f4-cefb-4d0c-a81d-a2747c46fd59&sktid=72f988bf-86f1-41af-91ab-2d7cd011db47&skt=2025-11-11T07%3A06%3A27Z&ske=2025-11-18T07%3A21%3A27Z&sks=b&skv=2025-07-05&sr=c&sp=rl&sig=%2FZ9tevFGVgzOM0Q1sgkxUFSVNg7AQuMmXoIwsYMvAzM%3D" "{os.path.join(savedir,locals+".txt")}" --overwrite=false --check-md5 FailIfDifferent --from-to=BlobLocal --recursive --log-level=INFO'
    os.system(download_word)

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