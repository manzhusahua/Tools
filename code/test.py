
import json
import os,sys
import shutil

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

def find_audioList(filelist_path,save_path,local):
    print()


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
    

if __name__ == "__main__":
    wus2()
    scus()
    # test()
    # succeeded_duration(r"C:\Users\v-zhazhai\Desktop\stats_set_output")
    # copy_files(r"C:\Users\v-zhazhai\Downloads\test\1.txt",r"C:\Users\v-zhazhai\Downloads\test")
    # file_path = r"C:\Users\v-zhazhai\Downloads\de-DE.txt"
    # # file_path = sys.argv[1]
    # save_path = r"C:\Users\v-zhazhai\Downloads\de-DE"
    # # save_path = sys.argv[2]
    # summary_paths = find_audioList(file_path,save_path)
    # merger_summary(summary_paths)

    # dir_path = r"C:\Users\v-zhazhai\debug\richland\ttschunk_out2"
    # chunk_name = "chunk_9b4105557f469b239a8deecd2af1ef91_0"
    # upload_data(dir_path, chunk_name)
    # rename(r"C:\Users\v-zhazhai\debug\richland\chunks\chunk_en-au_EnAU2581MSMIVO_0")