<<<<<<< HEAD
import os, shutil
import tarfile
=======
import os
import tarfile
import shutil
>>>>>>> 105a3862ecb20291c98662288f3278bc0df5c50c


def mkdir_floder(inputdir, fodername):
    save_path = os.path.join(inputdir, fodername, "PlainText")
    if not os.path.exists(save_path):
        os.makedirs(save_path, exist_ok=True)
    with open(os.path.join(save_path, fodername + ".txt"), "w", encoding="utf8") as s:
        s.writelines("\n")


def prepare_wav(inputdir, local):
    print("run {} add ssml file".format(local))
    add_ssml_path = os.path.join(inputdir, local, "1_add_ssml.py")
    # print(add_ssml_path)
    with open(r"D:\users\voices\1_add_ssml.py", "r", encoding="utf8") as f, open(
        add_ssml_path, "w", encoding="utf8"
    ) as s:
        for line in f.readlines():
            if "INPUT_Locale" in line:
                line = line.replace("INPUT_Locale", "{}".format(local))
            s.writelines(line)
    os.system("C:/Users/v-zhazhai/.conda/envs/test/python.exe {}".format(add_ssml_path))


def un_tar(file_name):
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
    os.remove(file_name)


def xmly_prepare(inputdir, chunk_name, outputdir):
    if not os.path.exists(outputdir):
        os.makedirs(outputdir, exist_ok=True)
    for name in chunk_name:

        # audio file
        audio_name1 = os.path.join(inputdir, name + ".audio")
        audio_name2 = os.path.join(outputdir, name + ".audio" + ".tar")
        shutil.copyfile(audio_name1, audio_name2)
        un_tar(audio_name2)
        for line in os.listdir(audio_name2 + "_files"):
            wave = os.path.join(audio_name2 + "_files", line)
            rewave = os.path.join(outputdir, name + "_" + line + ".wav")
            os.renames(wave, rewave)
        if os.path.exists(audio_name2 + "_files"):
            shutil.rmtree(audio_name2 + "_files")

        # trans file
        trans_name1 = os.path.join(inputdir, name + ".pasco_result")
        trans_name2 = os.path.join(outputdir, name + ".pasco_result" + ".tar")
        shutil.copyfile(trans_name1, trans_name2)
        un_tar(trans_name2)
        for line in os.listdir(trans_name2 + "_files"):
            trans = os.path.join(trans_name2 + "_files", line)
            retrans = os.path.join(outputdir, name + "_" + line + ".txt")
            os.renames(trans, retrans)
        if os.path.exists(trans_name2 + "_files"):
            shutil.rmtree(trans_name2 + "_files")

<<<<<<< HEAD

if __name__ == "__main__":

    # inputdir = r"D:\users\voices"
    # locals_list = ["kk-KZ","km-KH","kn-IN","ko-KR","lo-LA","lt-LT","lv-LV","mk-MK","ml-IN","mn-MN","ms-MY","mt-MT","my-MM","nb-NO"]
    # for name in locals_list:

    #     prepare_wav(inputdir,name)

    inputdir = r"C:\Users\v-zhazhai\Downloads\test1"
    chunk_name = ["chunk_000a2d20dd2fd34a60ce57262c1a9f32_0"]
    outputdir = r"C:\Users\v-zhazhai\Downloads\test2"
    xmly_prepare(inputdir, chunk_name, outputdir)
=======
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
    
>>>>>>> 105a3862ecb20291c98662288f3278bc0df5c50c
