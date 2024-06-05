
import json
import os,sys
import shutil
import wave
import csv
import pandas as pd
import zipfile
import xml.dom.minidom
from files_data_process.read_files import READFILE

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
            print(filename)
            zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zip.close()

    shutil.rmtree(dirpath, ignore_errors=True)

def word():
    inputfile=r"C:\Users\v-zhazhai\Downloads\Tier1.json"
    with open(inputfile,'r',encoding='utf-8') as f:
        content = json.loads(f.read().replace('\\', '\\\\'))

    outputfile=r"C:\Users\v-zhazhai\Downloads\Tier1_gender.json"
    w=open(outputfile,'w',encoding='utf-8')


    voices=content['speakers']
    for voice in voices:
        mykeys = list(voice.keys())
        k, v = "Gender", "Female"

        mykeys.insert(mykeys.index("Speaker")+1, k)
        voice[k] = v
        new_dict = {}
        for k in mykeys:
            new_dict.update({k: voice[k]})
        w.write(json.dumps(new_dict, indent=4).replace('\\\\', '\\'))

def wus2():
    with open(r"C:\Users\v-zhazhai\Desktop\wus2.sh",'r',encoding='utf8') as f:
        for line in f.readlines():
            line = str(line.replace('\n',''))
            os.system(line)
def scus():
    with open(r"C:\Users\v-zhazhai\Desktop\scus.sh",'r',encoding='utf8') as f:
        for line in f.readlines():
            line = str(line.replace('\n',''))
            os.system(line)

def blob(shfiles):
    with open(shfiles,'r',encoding='utf8') as f:
        for line in f.readlines():
            line = str(line.replace('\n',''))
            os.system(line)

def test(files_path,save_path):
    if not os.path.exists(save_path):
        os.makedirs(save_path, exist_ok=True)
    for name in os.listdir(files_path):
        file_name = os.path.join(files_path,name)
        save_file_path =  os.path.join(save_path,str(int(name.replace('.txt',''))).zfill(3)+".txt")

        word = READFILE().read_file(file_name)
        with open(save_file_path,'w',encoding='utf8') as s:
            for line in word:
                s.writelines(line.split('\t')[-1].replace('\n',''))
            s.writelines("\n")
        s.close


def merger_summary(summary_paths):
    for name in summary_paths:

        print(name)
    
def upload_data(dir_path, chunk_name):
    # list all the file that start with chunk_name
    file_list = os.listdir(dir_path)
    file_list = [os.path.join(dir_path, x) for x in file_list if x.startswith(chunk_name)]
    # upload to blob
    for file_path in file_list:
        # self.upload_to_blob_for_debug_file_singlethread(file_path)
        print(file_path)

def updata_blob(part):
    word = r'C:\Users/v-zhazhai/Toosl/code/Tool/merger_tar/azcopy.exe copy "C:\Users\v-zhazhai\Downloads\de-DE\{}\*" "https://stdstoragettsdp01eus.blob.core.windows.net/data/TTS_ChunkData/YouTube/v3/YouTube_temp/de-DE/{}/?sv=2023-01-03&se=2024-05-16T08%3A20%3A47Z&sr=c&sp=rwl&sig=PnvQUqQ2JxilMlyyxwB1PP4dHhR%2BxtjTPih5C7uwoFE%3D" --overwrite=false'.format(part,part)
    os.system(word)

def rename(filepath):
    for name in os.listdir(filepath):
        os.rename(os.path.join(filepath,name),os.path.join(filepath,name+".wav"))

def succeeded_duration(files_path):
    durations = []
    for name in os.listdir(files_path):
        f = str(open(os.path.join(files_path,name),'r',encoding='utf8').readlines()).split(',')
        duration = float([x.split(':')[1] for x in f if "succeeded_duration" in x][0])
        durations.append(duration)
    print(str(round(sum(durations)/3600, 5)))


def copy_files(list_path,files_path):
    with open(list_path,'r',encoding='utf8') as f:
        for line in f.readlines():
            line = line.replace('\n','')
            save_parth = os.path.join(files_path,line)
            if not os.path.exists(save_parth):
                os.makedirs(save_parth, exist_ok=True)
            # save text
            if not os.path.exists(os.path.join(save_parth,"text")):
                os.makedirs(os.path.join(save_parth,"text"), exist_ok=True)
            os.rename(os.path.join(files_path,"text",line+".txt"),os.path.join(save_parth,"text",line+".txt"))
            # save audio
            if not os.path.exists(os.path.join(save_parth,"audio")):
                os.makedirs(os.path.join(save_parth,"audio"), exist_ok=True)
            os.rename(os.path.join(files_path,"audio",line+".wav"),
                      os.path.join(save_parth,"audio",line+".wav"))
    
def copy_files1(files_path):
    files_list = [x.replace('.wav','') for x in os.listdir(files_path) if ".wav" in x]
    for line in files_list:
        save_parth = os.path.join(files_path,line)
        if not os.path.exists(save_parth):
            os.makedirs(save_parth, exist_ok=True)
            os.renames(os.path.join(files_path,line+".txt"),os.path.join(save_parth,line+".txt"))
            os.renames(os.path.join(files_path,line+".wav"),os.path.join(save_parth,line+".wav"))

def get_vtt(files_path):
    word = "WEBVTT\nKind: captions\nLanguage: en\n\n"
    files_list = [x for x in os.listdir(files_path)]
    for name in files_list:
        wav_name = os.path.join(files_path,name,name+'.wav')
        trans_name = os.path.join(files_path,name,name+'.txt')
        vtt = os.path.join(files_path,name,name+'.vtt')
        trans = open(trans_name,'r',encoding='utf8').readlines()[0]
        f = wave.open(wav_name, 'rb')
        time_count = f.getparams().nframes/f.getparams().framerate
        m = time_count//60%60
        h = time_count//3600
        s = time_count-h*3600-m*60
        end_time = "{:0>2}:{:0>2}:{:0>2}".format(h,m,'%.3f'%s)
        with open(vtt,'w',encoding='utf8') as s:
            s.writelines(word)
            s.writelines("00:00:00.000 --> "+str(end_time)+'\n')
            s.writelines(trans)

def prepare_csv(files_path,output):
    data_frame = None
    for name in os.listdir(files_path):
        text = open(os.path.join(files_path,name,"text",name+".txt"),'r',encoding='utf8').readlines()[0].replace('\n','')
        row_values = {"wav": [name.replace('.txt','')],
                    "text": [text],
                    "textless": ["false"],
                    "human_voice": ["true"],
                    "multispeaker_detect_score": ["-9999"],
                        }
        if data_frame is None:
            data_frame = pd.DataFrame(row_values)
        else:
            newdata = pd.DataFrame(row_values)
            data_frame = pd.concat([data_frame, newdata], axis=0, ignore_index=True)
    data_frame.to_csv(
                os.path.join(output,"metadata.csv"), sep="|", encoding="utf-8", index=False, quoting=csv.QUOTE_NONE,escapechar='|'
            )
def prepare_audio(files_path):
    if not os.path.exists(files_path+"_audio"):
        os.makedirs(files_path+"_audio", exist_ok=True)
    for name in os.listdir(files_path):
        audio = os.path.join(files_path,name,"audio",name+".wav")
        
        os.renames(os.path.join(files_path,name,"audio",name+".wav"),os.path.join(files_path+"_audio",name+".wav"))
def prepare_text(files_path):
    if not os.path.exists(files_path+"_audio"):
        os.makedirs(files_path+"_audio", exist_ok=True)
    for name in os.listdir(files_path):
        READFILE().read_file(os.path.join(files_path,name))
        for line in word:
            filename = line.split('\t')[0]
            with open(os.path.join(files_path+"_audio",filename+'.txt'),'w',encoding='utf8') as s:
                s.writelines(line.split('\t')[-1])

# def get_fielwave(files,xmlfiles):
#     f = open(files,'r',encoding='utf-16-le').readlines()
#     i = [x for i,x in enumerate(f) if x.find("3070000953") != -1]
#     # 打开XML文档
#     dom = xml.dom.minidom.parse(xmlfiles)

#     # 得到文档元素对象
#     root = dom.documentElement
#     # # 获取子标签名字
#     bb = root.getElementsByTagName('si')
#     with open(files.replace('.txt',"_v1.txt"),'w',encoding='utf-16-le') as s:
#         for id in [x.split('\t')[0] for x in f]:
#             if id not in [str(x.getAttribute("id")) for x in bb]:
#                 print(id)
        
        # for line in bb:
        #     iline.getAttribute("id")
        #     if len([x for i,x in enumerate(f) if x.find(str(i)) != -1]) !=1:
        #         s.writelines()

def get_fielwave(files1,files2):

    id1 = [x for x in open(files1,'r',encoding='utf8').readlines()]

if __name__ == "__main__":
    wus2()
    scus()
