# from jsonpath import jsonpath
import json
import os
import tarfile
import shutil

def read_richland_result_json(input_file):
    tmp = []
    file = open(input_file, 'r', encoding='utf-8').readlines()[0]
    file = str(file[file.index("{"):]).split('"Audio":')
    for line in file[1:]:
        # tmp.append('"Audio":')
        # tmp.append(line.split(',')[0]+'\t')
        if '"FullTranscription":' in line:
            # tmp.append('"FullTranscription":')
            word = line.split('"FullTranscription": ')[-1].split('}')[0]
            word = word.encode().decode("unicode_escape").replace('"','')
            tmp.append(word+'\n')

    with open(input_file.replace('richland_result','txt'),'w',encoding='utf8') as s:
        for line in tmp:
            s.writelines(line)

def read_whisper_transcription_json(input_file):
    file_name = input_file+'.tar'
    shutil.copy(input_file, file_name)

    words = []
    tar = tarfile.open(file_name)  
    names = tar.getnames()  
    if os.path.isdir(file_name + "_files"):
         pass  
    else:
         os.mkdir(file_name + "_files")  
    #由于解压后是许多文件，预先建立同名文件夹  
    for name in names:
        tar.extract(name, file_name + "_files/")  
    tar.close()
    n = 0
    while n<len(os.listdir(file_name + "_files/")):
        with open(os.path.join(file_name+ "_files",str(n)),'r',encoding='utf8') as f:
            for line in f.readlines():
                words.append(line)
        n+=1
        
    with open(file_name.replace(".tar",'.txt'),'w',encoding='utf8') as s:
        for line in words:
            s.writelines(line+'\n')
    shutil.rmtree(file_name+ "_files")
    os.remove(input_file+'.tar')

def read_info_transcription_json(input_file):
    file_name = input_file+'.tar'
    shutil.copy(input_file, file_name)

    words = []
    tar = tarfile.open(file_name)  
    names = tar.getnames()  
    if os.path.isdir(file_name + "_files"):
         pass  
    else:
         os.mkdir(file_name + "_files")  
    #由于解压后是许多文件，预先建立同名文件夹  
    for name in names:
        tar.extract(name, file_name + "_files/")  
    tar.close()
    n = 0
    while n<len(os.listdir(file_name + "_files/")):
        folders = os.path.join(file_name+ "_files",str(n))
        with open(os.path.join(folders,"original_fname"),'r',encoding='utf8') as f:
            for line in f.readlines():
                words.append(line.replace('/mnt/c/Users/v-zhazhai/debug/richland/F128/FreeTalk/Wave16kNormalized/',''))
        n+=1
        
    with open(file_name.replace(".tar",'.txt'),'w',encoding='utf8') as s:
        for line in words:
            s.writelines(line+'\n')
    shutil.rmtree(file_name+ "_files")
    os.remove(input_file+'.tar')



if __name__ == "__main__":

    read_info_transcription_json(r"C:\Users\v-zhazhai\debug\richland\F128\General\output\chunk\chunk_5f6318b14acc9b4ef84c5d5447b2ec48_0.info")
    # input_path = r'C:\Users\v-zhazhai\debug\richland\F128\General\output\chunk'
    # for name in os.listdir(input_path):
    #     if ".richland_result" in name:
    #         input_file = os.path.join(input_path,name)
    #         read_richland_result_json(input_file)
    #     if ".whisper_transcription" in name:
    #         input_file = os.path.join(input_path,name)
    #         # print(input_file)
    #         read_whisper_transcription_json(input_file)
    #     if ".info" in name:
    #         input_file = os.path.join(input_path,name)
    #         # print(input_file)
    #         read_info_transcription_json(input_file)