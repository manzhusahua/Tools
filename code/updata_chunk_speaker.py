import os
import tarfile
import glob
import codecs
import chardet
import json
import shutil
import numpy as np

def un_tar(file_name):
    if os.path.isfile(file_name):
        shutil.copyfile(file_name,file_name+'.tar')
        # os.renames(file_name,file_name+'.tar')
        tar = tarfile.open(file_name)
        names = tar.getnames()
        if os.path.isdir(file_name + "_files"):
            pass
        else:
            os.mkdir(file_name + "_files")
        # 由于解压后是许多文件，预先建立同名文件夹
        for name in names:
            tar.extract(name, file_name + "_files/")
        tar.close()
        # os.remove(file_name)
        os.remove(file_name+'.tar')
        return file_name+"_files"
    

def updata_speaker(fine_segment_dir,info_dir):
    # print(len(os.listdir(fine_segment_dir)))
    for n in range(0,len(os.listdir(fine_segment_dir))):
        example_dir = os.path.join(fine_segment_dir,str(n))
        original_fname_file = os.path.join(info_dir,str(n),"original_fname")
        content=codecs.open(original_fname_file,'rb').read()
        word = open(original_fname_file,'r',encoding=chardet.detect(content)['encoding']).readlines()[0]
        for m in range(0,len(os.listdir(example_dir))):
            if len(os.listdir(example_dir)) ==1:
                row_values = {
                "currentspeaker": int(word.split("spk")[-1].replace(".wav","")),
                "nextspeaker":"null",
                "lastspeaker": "null",
                "totalspeakernumber": 2,}
            elif m==0:
                row_values = {
                "currentspeaker": int(word.split("spk")[-1].replace(".wav","")),
                "nextspeaker":int(word.split("spk")[-1].replace(".wav","")),
                "lastspeaker": "null",
                "totalspeakernumber": 2,}
            elif m==len(os.listdir(example_dir))-1:
                row_values = {
                "currentspeaker": int(word.split("spk")[-1].replace(".wav","")),
                "nextspeaker": "null",
                "lastspeaker":  int(word.split("spk")[-1].replace(".wav","")),
                "totalspeakernumber": 2,}

            
            
            else:
                row_values = {
                "currentspeaker": int(word.split("spk")[-1].replace(".wav","")),
                "nextspeaker": int(word.split("spk")[-1].replace(".wav","")),
                "lastspeaker": int(word.split("spk")[-1].replace(".wav","")),
                "totalspeakernumber": 2,}
            with open(os.path.join(example_dir, str(m),"speaker"),"w",encoding="utf8",) as save_json:
                json.dump(row_values, save_json)

def zip_tar(fine_segment_dir,fine_segment_name):
    if os.path.exists(fine_segment_name):
        os.remove(fine_segment_name)
    os.chdir(fine_segment_dir)
    print(len(os.listdir(fine_segment_dir)))
    count = ' '.join(str(n) for n in range(0,len(os.listdir(fine_segment_dir))))
    # count = ' '.join(str(n) for n in range(1102,2187))
    # count = ' '.join(str(n) for n in range(2187,len(os.listdir(fine_segment_dir))))
    os.system(f"tar -cvf {fine_segment_name} {count}")
    
def updata_spk(info_dir):
    names_list = ["00000_spk2","00001_spk1","00002_spk2","00003_spk1","00004_spk2","00005_spk1","00006_spk2","00007_spk1","00008_spk2","00009_spk1","00010_spk2","00011_spk1","00012_spk2","00013_spk1","00014_spk2","00015_spk1","00016_spk2","00017_spk1","00018_spk2","00019_spk1","00020_spk2","00021_spk1","00022_spk2","00023_spk1","00024_spk2","00025_spk1","00026_spk2","00027_spk1","00028_spk2","00029_spk1","00030_spk2","00031_spk1","00032_spk2","00033_spk1","00034_spk2","00035_spk1","00036_spk2","00037_spk1","00038_spk2","00039_spk1","00040_spk2","00041_spk1"]
    for file in glob.glob(os.path.join(info_dir, "**", "original_fname"), recursive=True):
        content=codecs.open(file,'rb').read()
        word = open(file,'r',encoding=chardet.detect(content)['encoding']).readlines()[0]
        names = os.path.basename(word)
        if names.split("_")[0] in names:
            re_name = [x for i,x in enumerate(names_list) if x.find(names.split("_")[0]) != -1][0]
        with open(file+"_1",'w',encoding=chardet.detect(content)['encoding']) as s:
            s.writelines("/".join([os.path.split(word)[0],re_name+".wav"]))
        os.remove(file)
        os.renames(file+"_1",file)

def updata_info(info_files,savefile,style):
    un_tar_path = un_tar(info_files)
    for file_path in glob.glob(os.path.join(un_tar_path, "**", "original_fname"), recursive=True):
        content=codecs.open(file_path,'rb').read()
        word = open(file_path,'r',encoding=chardet.detect(content)['encoding']).readlines()[0]
        
        
        # additional_info = {"AudioFileName": f"{os.path.basename(word)}", "Style": f"{os.path.basename(word).split('_')[1]}","Emotional intensity":f"{os.path.basename(word).split('_')[2]}", "Source": "emotional"}
        additional_info = {"AudioFileName": f"{os.path.basename(word)}", "speaker": "ZhCNM100","style":f"{style}"}
        save_additional_info = file_path.replace("original_fname","additional_info")
        with open(save_additional_info,'w',encoding='utf8') as s:
            s.writelines(str(additional_info).replace("'","\""))
    zip_tar(un_tar_path,savefile)
    # shutil.rmtree(un_tar_path)

def renames(inputdir):
    savedir = inputdir+"_renames"
    os.makedirs(savedir,exist_ok=True)
    n=0
    for line in os.listdir(inputdir):
        os.renames(os.path.join(inputdir,line),os.path.join(savedir,str(n)))
        n+=1
    os.renames(savedir,inputdir)

def get_times_count(info_dir):
    times = 0.0
    times1 = []
    n=0
    count = []
    for line in glob.glob(os.path.join(info_dir,"**\\*duration"), recursive=True):
        times+=float(np.fromfile(line)[0])
        if times>7200:
            count.append(n)
            times1.append(times)
            times = 0
        n+=1
    print(count,times1,n,times)
    
if __name__=="__main__":
    
    # maplist = ["audio_48k_denoised_files","audio_files","coarse_segment_files","fine_segment_files","info_files","richland_result_files"]
    inputdir = r"C:\Users\v-zhazhai\Desktop\ZhCNM100"
    savedir = r"C:\Users\v-zhazhai\Desktop\ZhCNM100_1"
    chunk_name = "chunk_ZhCNF128_customerservice_Reference_Customer_Weiwei_1"
    zip_tar(r"C:\Users\v-zhazhai\debug\Chat\chunk_090faaaffa02283259fa1ea2d809cff2_0.audio_48k_denoised_files",r"C:\Users\v-zhazhai\debug\Chat\chunk_090faaaffa02283259fa1ea2d809cff2_0.audio_48k_denoised")
    # os.makedirs(savedir,exist_ok=True)
    # for line in os.listdir(inputdir):
    #     if ".json" not in line:
    #         # un_tar(os.path.join(inputdir,line))
    #         style = line.split("_")[2]
    #         # print(style)
    #         updata_info(os.path.join(inputdir,line),os.path.join(savedir,line),style)
    # save_path = os.path.split(inputdir)[0]
    # for names in maplist:
    #     fine_segment_dir = os.path.join(inputdir,f"{chunk_name}."+names)
        
    #     fine_segment_name = os.path.join(save_path,f"{chunk_name}.{names.replace('_files','')}")
    #     renames(fine_segment_dir)
    #     zip_tar(fine_segment_dir,fine_segment_name)
    # get_times_count(os.path.join(inputdir,f"{chunk_name}.info_files"))