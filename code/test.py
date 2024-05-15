
import json
import os,sys
import shutil
import wave
import csv
import pandas as pd

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

def test(files_path):
    with open(files_path,'r',encoding='utf8') as f:
        for line in f.readlines():
            os.system(line.replace("\n",''))

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

def prepare(files_path):
    data_frame = None
    for name in os.listdir(files_path):
        text = open(os.path.join(files_path,name),'r',encoding='utf8').readlines()[0].replace('\n','')
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
                files_path+'.csv', sep="|", encoding="utf-8", index=False, quoting=csv.QUOTE_NONE
            )



if __name__ == "__main__":
    # get_vtt(r"C:\Users\v-zhazhai\debug\audio_text_segnment\wave")
    wus2()
    scus()
    # test(r"C:\Users\v-zhazhai\Desktop\11.sh")
    # succeeded_duration(r"C:\Users\v-zhazhai\Desktop\stats_set_output")
    # prepare(r"C:\Users\v-zhazhai\debug\audio_text_segnment\test")
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