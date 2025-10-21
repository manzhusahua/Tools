import os
import tarfile
import glob
import codecs
import chardet
import json
import shutil

def un_tar(file_name):
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
    count = ' '.join(str(n) for n in range(0,len(os.listdir(fine_segment_dir))))
    # with open(r"C:\Users\v-zhazhai\Desktop\1.sh",'w',encoding='utf8') as s:
    #     s.writelines(f"tar -cvf {fine_segment_name} {count}")
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


def updata_info(info_files,savefile):
    un_tar_path = un_tar(info_files)
    # for file_path in glob.glob(os.path.join(un_tar_path, "**", "original_fname"), recursive=True):
    #     # print(file)
    #     content=codecs.open(file_path,'rb').read()
    #     word = open(file_path,'r',encoding=chardet.detect(content)['encoding']).readlines()[0]
    #     # print(word)
        
        
    #     additional_info = {"AudioFileName": f"{os.path.basename(word)}", "Style": f"{os.path.basename(word).split('_')[1]}","Emotional intensity":f"{os.path.basename(word).split('_')[2]}", "Source": "emotional"}
    #     save_additional_info = file_path.replace("original_fname","additional_info")
    #     with open(save_additional_info,'w',encoding='utf8') as s:
    #         s.writelines(str(additional_info))
    # zip_tar(un_tar_path,savefile)
    # shutil.rmtree(un_tar_path)

if __name__=="__main__":
    # fine_segment_file = r"C:\Users\v-zhazhai\Downloads\chunkoutput1\huangzhizhong\chunk_huangzhizhong_0.fine_segment"
    # info_file = r"C:\Users\v-zhazhai\Downloads\chunkoutput1\huangzhizhong\chunk_huangzhizhong_0.info"
    # fine_segment_name = r"C:\Users\v-zhazhai\Downloads\chunkoutput1\nezha\chunk_nezha_0.fine_segment"
    # fine_segment_dir =un_tar(fine_segment_file)
    # info_dir = un_tar(info_file)
    # updata_speaker(fine_segment_dir,info_dir)
    # zip_tar(fine_segment_dir,fine_segment_file)
    # updata_spk(r"C:\Users\v-zhazhai\Downloads\chunkoutput1\huangzhizhong\chunk_huangzhizhong_0 - 副本.info")
    # transmlplist = ["segment_transcription","segment_transcription_beforeTN","segment_sr_transcription"]
    # coarse_segment_dir = un_tar(r"C:\Users\v-zhazhai\Downloads\ZhCNF128_ttschunk_finesegment_5\chunk_ZhCNF128_Emotion_Aegis_0.fine_segment")
    # coarse_segment_dir = r"C:\Users\v-zhazhai\Downloads\ZhCNF128_ttschunk_finesegment_5\chunk_ZhCNF128_Emotion_Aegis_0.fine_segment_files"
    # # save_coarse_segment = r"C:\Users\v-zhazhai\Downloads\ZhCNF128_ttschunk_finesegment_5_output\chunk_ZhCNF128_Emotion_Aegis_0"
    # for trans in transmlplist:
    #     for file in glob.glob(os.path.join(coarse_segment_dir, "**", f"{trans}"), recursive=True):
    #         print(file)
            # print(file.split("\\")[-3].zfill(5))
    #         save_file = os.path.join(save_coarse_segment,file.split("\\")[-3].zfill(5),"coarse_segment","coarse_"+file.split("\\")[-2]+f"_{trans}")
    #         shutil.copyfile(file,save_file)
    # updata_info(r"C:\Users\v-zhazhai\Downloads\emotional\chunk_a0ab6d9cb9ca94755fae4c2cc67f5a4c_0.info",r"C:\Users\v-zhazhai\Downloads\emotional\updata\chunk_a0ab6d9cb9ca94755fae4c2cc67f5a4c_0.info")
    inputdir = r"C:\Users\v-zhazhai\Downloads\batch02"
    for line in os.listdir(inputdir):
        un_tar(os.path.join(inputdir,line))
    # zip_tar(r"C:\Users\v-zhazhai\Downloads\emotional\chunk_c8e9f3f1875ad6389e6131e78c41097e_0.info_files",r"C:\Users\v-zhazhai\Downloads\emotional\updata\chunk_c8e9f3f1875ad6389e6131e78c41097e_0.info")
    # 03-01-01-01-01-116-02-02-02-05