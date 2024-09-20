import os
import tarfile
import shutil

def mkdir_floder(inputdir,fodername):
    save_path = os.path.join(inputdir,fodername,"PlainText")
    if not os.path.exists(save_path):
        os.makedirs(save_path, exist_ok=True)
    with open(os.path.join(save_path,fodername+'.txt'),'w',encoding='utf8') as s:
        s.writelines('\n')

def prepare_wav(inputdir,local):
    print("run {} add ssml file".format(local))
    add_ssml_path = os.path.join(inputdir,local,"1_add_ssml.py")
    # print(add_ssml_path)
    with open(r"D:\users\voices\1_add_ssml.py",'r',encoding='utf8') as f,open(add_ssml_path,'w',encoding='utf8') as s:
        for line in f.readlines():
            if "INPUT_Locale" in line:
                line = line.replace("INPUT_Locale","{}".format(local))
            s.writelines(line)
    os.system('C:/Users/v-zhazhai/.conda/envs/test/python.exe {}'.format(add_ssml_path))

def un_tar(file_name):
    tar = tarfile.open(file_name)
    names = tar.getnames()
    if os.path.isdir(file_name + "_files"):
        pass
    else:
        os.mkdir(file_name + "_files")
    for name in names:
        tar.extract(name, file_name + "_files/")
    tar.close()
    os.remove(file_name)

if __name__ == "__main__":
    
    files1 = r"C:\Users\v-zhazhai\Downloads\filenames.txt"
    files2 = r"C:\Users\v-zhazhai\Downloads\filenames_FreeTalk.txt"

    word = []
    with open(files1,'r',encoding='utf8') as f,open(files2,'w',encoding='utf8') as s:
        for line in f.readlines():
            name = int(line.split('_')[0].replace("XMLYAudiobook",''))
            if name >= 583:
                word.append(line)
                s.writelines(line)
    s.close()
    f.close()
    # os.remove(files1)
    # os.renames(files2,files1)
    