
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

def test():
    my_keys = ['key_1', 'key_2', 'key_3']
    source_dict = {'key_1': 'li', 'key_2': "wg", 'key_3': 'zh'}
    outputfile=r"C:\Users\v-zhazhai\Downloads\Tier1_gender.json"
    w=open(outputfile,'w',encoding='utf-8')
    k, v = 'key_4', 'hello'
    my_keys.insert(my_keys.index('key_1') + 1, k)
    source_dict[k] = v
    
    w.write(json.dumps(voice, indent=4).replace('\\\\', '\\'))
    new_dict = {}
    for k in my_keys:
        new_dict.update({k: source_dict[k]})

def find_audioList(filelist_path,save_path,local):
    print()
#     token = "?sv=2023-01-03&ss=btqf&srt=sco&st=2024-04-12T06%3A43%3A38Z&se=2024-04-13T06%3A43%3A38Z&sp=rl&sig=8UfQr%2B6H4SmmVuhx9sFbH6ROikUvAKBvCZHvRJpgXWM%3D"
#     word2 = 'C:\Users\v-zhazhai\Toosl\code\Tool\merger_tar\azcopy.exe list "https://speechdatacrawlrgwusdiag.blob.core.windows.net/rawpublicdata/{}/{}" > "{}\{}.txt"'.format(local,token,filelist_path,local)
#     os.system(word2)
#     if not os.path.exists(save_path):
#         os.makedirs(save_path, exist_ok=True)
#     with open(filelist_path,'r',encoding='utf8') as f:
#         for line in f.readlines():
#             if "audioList.txt" in line:
#                 line = line.split(";")[0].replace('INFO: ','')
#                 word1 = 'C:/Users/v-zhazhai/Toosl/Tools/azcopy.exe copy "https://speechdatacrawlrgwusdiag.blob.core.windows.net/rawpublicdata/{}/{}{}" "C:/Users/v-zhazhai/Downloads/{}/{}" --overwrite="false"'.format(local,line,token,local,line)
#                 os.system(word1)

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


if __name__ == "__main__":
    # file_path = r"C:\Users\v-zhazhai\Downloads\de-DE.txt"
    # # file_path = sys.argv[1]
    # save_path = r"C:\Users\v-zhazhai\Downloads\de-DE"
    # # save_path = sys.argv[2]
    # summary_paths = find_audioList(file_path,save_path)
    # merger_summary(summary_paths)

    # dir_path = r"C:\Users\v-zhazhai\debug\richland\ttschunk_out2"
    # chunk_name = "chunk_9b4105557f469b239a8deecd2af1ef91_0"
    # upload_data(dir_path, chunk_name)
    rename(r"C:\Users\v-zhazhai\debug\richland\chunks\chunk_en-au_EnAU2581MSMIVO_0")