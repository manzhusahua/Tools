import os
import glob
import codecs
import chardet
import shutil

def ChaiQing(inputdir):
    for file_path in glob.glob(os.path.join(inputdir, "**", "*.txt"), recursive=True):
        content=codecs.open(file_path,'rb').read()
        word = open(file_path,'r',encoding=chardet.detect(content)['encoding']).readlines()
        lianjiezu = False
        for line in word:
            if "-" in line:
                lianjiezu = True
                continue
                # print(file_path)
        if not lianjiezu:
            shutil.copyfile(file_path,file_path.replace("prepare","prepare_clean"))
            shutil.copyfile(file_path.replace("txt","wav"),file_path.replace("prepare","prepare_clean").replace("txt","wav"))
            shutil.copyfile(file_path.replace("txt","json"),file_path.replace("prepare","prepare_clean").replace("txt","json"))

def shaofei(transfile,savedir):
    os.makedirs(savedir, exist_ok=True)
    names = ["00001","00002","00003","00004","00005","00006","00007","00008","00009","00010","00011","00012","00013","00014","00015","00016","00017","00018","00019","00020","00021","00022","00023","00024","00025","00026","00027","00028","00029","00030","00031","00032","00033","00034","00035","00036","00037","00038","00039","00040","00041","00042","00043","00044","00045","00046","00047","00048","00049","00050","00051","00052","00053","00054","00055","00056","00057","00058","00059","00060","00061","00062","00063","00064","00065","00066","00067","00068","00069","00070","00071","00072","00073","00074","00075","00076","00077","00078","00079","00080","00081","00082","00083","00084","00085","00086","00087","00088","00089","00090","00091","00092","00093","00094","00095","00096","00097","00098","00099","00100"]
    content=codecs.open(transfile,'rb').read()
    word = open(transfile,'r',encoding=chardet.detect(content)['encoding']).readlines()
    n=0
    for line in word:
        with open(os.path.join(savedir,str(names[n])+".txt"),'w',encoding='utf8') as s:
            s.writelines(line)
        n+=1

def WenningWei(transfile,savedir):
    os.makedirs(savedir, exist_ok=True)
    content=codecs.open(transfile,'rb').read()
    word = open(transfile,'r',encoding=chardet.detect(content)['encoding']).readlines()
    for line in word:
        with open(os.path.join(savedir,line.split('\t')[0]+".txt"),'w',encoding='utf8') as s:
            s.writelines(line.split('\t')[-1])

if __name__ == "__main__":
    WenningWei(r"C:\Users\v-zhazhai\Desktop\001600020800001-001600024100004.txt",r"C:\Users\v-zhazhai\Desktop\Scripts\001600020800001-001600024100004")
    # ChaiQing(r"C:\Users\v-zhazhai\Desktop\prepare")