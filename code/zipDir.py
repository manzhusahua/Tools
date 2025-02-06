import os
import zipfile
import glob
import shutil
import codecs
import chardet

def zipDir(dirpath, outFullName):
    """
    压缩指定文件夹
    :param dirpath: 目标文件夹路径
    :param outFullName: 压缩文件保存路径+xxxx.zip
    :return: 无
    """
    zip = zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(dirpath):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dirpath, '')
 
        for filename in filenames:
            if ".wav" in filename:
                zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zip.close()
 
def unzipDir(zippath,folder_abs):
    zip_file = zipfile.ZipFile(zippath)
    zip_list = zip_file.namelist()
    for f in zip_list:
        zip_file.extract(f, folder_abs)
    zip_file.close()
    for line in glob.glob(os.path.join(folder_abs, "**", "*.wav"), recursive=True):
        os.renames(line,os.path.join(folder_abs,os.path.basename(line)))
    shutil.rmtree(os.path.join(folder_abs,"__MACOSX"))
    content=codecs.open(zippath.replace(".zip",".txt"),'rb').read()
    word = open(zippath.replace(".zip",".txt"),'r',encoding=chardet.detect(content)['encoding']).readlines()
    for line in word:
        with open(os.path.join(folder_abs,line.split('\t')[0]+".txt"), 'w',encoding='utf8') as s:
            s.writelines(line.split('\t')[1])
if __name__ == "__main__":
    # input_path = "./origin_file_001"
    # output_path = "./test.zip"
 
    zipDir(r"C:\Users\v-zhazhai\Downloads\input\xiaoxin_yukuai_zhcn_80", r"C:\Users\v-zhazhai\Downloads\input\xiaoxin_yukuai_zhcn_80\waves.zip")
    # for line in os.listdir(r"C:\Users\v-zhazhai\Downloads\rawdata"):
    #     if line.endswith(".zip"):
    #         unzipDir(os.path.join(r"C:\Users\v-zhazhai\Downloads\rawdata",line),os.path.join(r"C:\Users\v-zhazhai\Downloads\xdf_xiaoxin",line.replace(".zip","")))
    # unzipDir(r"C:\Users\v-zhazhai\Downloads\rawdata\xiaoxin_beishang_zhcn_70.zip",r"C:\Users\v-zhazhai\Downloads\xdf_xiaoxin")