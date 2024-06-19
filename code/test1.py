# import os
# import codecs
# import chardet

# file_path = r"C:\Users\v-zhazhai\Downloads\CaiQing\AMI_text"
# with open(file_path+".txt",'w',encoding='utf8') as s:
#     for name in os.listdir(file_path):
#         files_name = os.path.join(file_path,name)
#         if os.path.getsize(files_name) != 0:
#             word = open(files_name,'r',encoding='utf8').read()
#             # content=codecs.open(files_name,'rb').read()
#             # word = open(files_name,'r',encoding=chardet.detect(content)['encoding']).readlines()[0]
#             s.writelines(name.replace('.txt','.wav')+'\t'+word+'\n')


import pandas as pd
import os
import zipfile
import shutil

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
            zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zip.close()



wave_paths = r"C:\Users\v-zhazhai\Downloads\CaiQing\fisher_48k_wav"
saves_path = r"C:\Users\v-zhazhai\Downloads\CaiQing\fisher"
metadtas_path = r"C:\Users\v-zhazhai\Downloads\CaiQing\fisher_metadata"


files_list = []
for n in range(len(os.listdir(metadtas_path))):
    metadta_path = os.path.join(metadtas_path,"metadata_"+str(n)+".csv")
    save_path = os.path.join(saves_path,str(n).zfill(5),"waves")
    if not os.path.exists(save_path):
        os.makedirs(save_path, exist_ok=True)
    data = pd.read_csv(metadta_path, sep='|', encoding='utf-8')

    waves=[x for x in data['wav']]
    for name in waves:
        # print(name)
        # wave_path = os.path.join(wave_paths,name+".wav")
        # print(wave_path)
        # print("copy "+os.path.join(wave_path,name+".wav")+" "+os.path.join(save_path,name+'.wav')+'\n')
        os.system("copy "+os.path.join(wave_paths,name+".wav")+" "+os.path.join(save_path,name+'.wav'))

    os.system("copy "+metadta_path+" "+os.path.join(os.path.split(save_path)[0],"metadata.csv"))
    zipDir(save_path, save_path+'.zip')
    if os.path.exists(save_path):
        shutil.rmtree(save_path)
    files_list.append(os.path.join(str(n).zfill(5),"metadata.csv"))
with open(os.path.join(saves_path,"filenames.txt"),'w',encoding='utf8') as s:
    for line in files_list:
        s.writelines(line.replace('\\','/')+'\n')