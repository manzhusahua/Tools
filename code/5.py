import os
import glob
import shutil
import codecs
import chardet
import tarfile
import numpy as np
import pandas as pd
import json
def renames(loaca1,loaca2):
    stdstoragetts01eus = f'C:/Users/v-zhazhai/Toosl/code/Tool/merger_tar/azcopy.exe copy "https://stdstoragettsdp01wus2.blob.core.windows.net/data/TTS_ChunkData/Dict/v1/chunk_output/{loaca1}/*?sv=2025-07-05&st=2025-11-07T03%3A02%3A52Z&se=2025-11-14T03%3A17%3A52Z&skoid=c52a83f4-cefb-4d0c-a81d-a2747c46fd59&sktid=72f988bf-86f1-41af-91ab-2d7cd011db47&skt=2025-11-07T03%3A02%3A52Z&ske=2025-11-14T03%3A17%3A52Z&sks=b&skv=2025-07-05&sr=c&sp=rlt&sig=qOtWs%2BvMXCryk6IFwe2iESXHKqfQZwXkrJUExB1xWe4%3D" "https://stdstoragetts01eus.blob.core.windows.net/data/realisticttsdataset_v3/train/chunks/{loaca2}/dictionary/Wiki_dictionary/?sv=2025-07-05&st=2025-11-07T03%3A02%3A55Z&se=2025-11-14T03%3A17%3A55Z&skoid=c52a83f4-cefb-4d0c-a81d-a2747c46fd59&sktid=72f988bf-86f1-41af-91ab-2d7cd011db47&skt=2025-11-07T03%3A02%3A55Z&ske=2025-11-14T03%3A17%3A55Z&sks=b&skv=2025-07-05&sr=c&sp=rwlt&sig=5QT4DHYHMKRXU31npwzkjTczW2CINkHkLpz%2F5sLYcH4%3D" --overwrite=false --from-to=BlobBlob --s2s-preserve-access-tier=false --check-length=true --include-directory-stub=false --s2s-preserve-blob-tags=false --recursive --log-level=INFO'
    # os.system(stdstoragetts01eus)


    # stdstoragetts01scus = f'C:/Users/v-zhazhai/Toosl/code/Tool/merger_tar/azcopy.exe copy "https://stdstoragettsdp01wus2.blob.core.windows.net/data/TTS_ChunkData/Dict/v1/chunk_output/{loaca1}/*?sv=2025-07-05&st=2025-11-07T03%3A03%3A09Z&se=2025-11-14T03%3A18%3A09Z&skoid=c52a83f4-cefb-4d0c-a81d-a2747c46fd59&sktid=72f988bf-86f1-41af-91ab-2d7cd011db47&skt=2025-11-07T03%3A03%3A09Z&ske=2025-11-14T03%3A18%3A09Z&sks=b&skv=2025-07-05&sr=c&sp=rlt&sig=PFdMXlQ9JJkNALHj3K8UmUlnc0xBqhr7q4Cj76UaA%2BQ%3D" "https://stdstoragetts01scus.blob.core.windows.net/data/realisticttsdataset_v3/train/chunks/{loaca2}/dictionary/Wiki_dictionary/?sv=2025-07-05&st=2025-11-07T03%3A03%3A10Z&se=2025-11-14T03%3A18%3A10Z&skoid=c52a83f4-cefb-4d0c-a81d-a2747c46fd59&sktid=72f988bf-86f1-41af-91ab-2d7cd011db47&skt=2025-11-07T03%3A03%3A10Z&ske=2025-11-14T03%3A18%3A10Z&sks=b&skv=2025-07-05&sr=c&sp=rwlt&sig=DSogmE6zHq9C2WDqoLmPOowaRS5JYDHRGG8QuAsXs%2BI%3D" --overwrite=false --from-to=BlobBlob --s2s-preserve-access-tier=false --check-length=true --include-directory-stub=false --s2s-preserve-blob-tags=false  --recursive --log-level=INFO'
    # os.system(stdstoragetts01scus)


    # stdstoragetts01wus2 = f'C:/Users/v-zhazhai/Toosl/code/Tool/merger_tar/azcopy.exe copy "https://stdstoragettsdp01wus2.blob.core.windows.net/data/TTS_ChunkData/Dict/v1/chunk_output/{loaca1}/*?sv=2025-07-05&st=2025-11-07T03%3A03%3A21Z&se=2025-11-14T03%3A18%3A21Z&skoid=c52a83f4-cefb-4d0c-a81d-a2747c46fd59&sktid=72f988bf-86f1-41af-91ab-2d7cd011db47&skt=2025-11-07T03%3A03%3A21Z&ske=2025-11-14T03%3A18%3A21Z&sks=b&skv=2025-07-05&sr=c&sp=rlt&sig=c94Nlrio2TaNtCFlVlzoF1R5ApHSHM4CwaELqe%2BHkYE%3D" "https://stdstoragetts01wus2.blob.core.windows.net/data/realisticttsdataset_v3/train/chunks/{loaca2}/dictionary/Wiki_dictionary/?sv=2025-07-05&st=2025-11-07T03%3A03%3A23Z&se=2025-11-14T03%3A18%3A23Z&skoid=c52a83f4-cefb-4d0c-a81d-a2747c46fd59&sktid=72f988bf-86f1-41af-91ab-2d7cd011db47&skt=2025-11-07T03%3A03%3A23Z&ske=2025-11-14T03%3A18%3A23Z&sks=b&skv=2025-07-05&sr=c&sp=rwlt&sig=Yyf%2F6hZ20r2xK%2Fe363LQPh4smvgkZPtmbzXTkn39zgM%3D" --overwrite=false --from-to=BlobBlob --s2s-preserve-access-tier=false --check-length=true --include-directory-stub=false --s2s-preserve-blob-tags=false  --recursive --log-level=INFO'
    # os.system(stdstoragetts01wus2)


    # stdstoragetts01wus3 = f'C:/Users/v-zhazhai/Toosl/code/Tool/merger_tar/azcopy.exe copy "https://stdstoragettsdp01wus2.blob.core.windows.net/data/TTS_ChunkData/Dict/v1/chunk_output/{loaca1}/*?sv=2025-07-05&st=2025-11-07T03%3A03%3A38Z&se=2025-11-14T03%3A18%3A38Z&skoid=c52a83f4-cefb-4d0c-a81d-a2747c46fd59&sktid=72f988bf-86f1-41af-91ab-2d7cd011db47&skt=2025-11-07T03%3A03%3A38Z&ske=2025-11-14T03%3A18%3A38Z&sks=b&skv=2025-07-05&sr=c&sp=rlt&sig=90uGzzihH5pK4KB4ho4ROREmpkwdGA6JoKyNgQFh4bU%3D" "https://stdstoragetts01wus3.blob.core.windows.net/data/realisticttsdataset_v3/train/chunks/{loaca2}/dictionary/Wiki_dictionary/?sv=2025-07-05&st=2025-11-07T03%3A03%3A40Z&se=2025-11-14T03%3A18%3A40Z&skoid=c52a83f4-cefb-4d0c-a81d-a2747c46fd59&sktid=72f988bf-86f1-41af-91ab-2d7cd011db47&skt=2025-11-07T03%3A03%3A40Z&ske=2025-11-14T03%3A18%3A40Z&sks=b&skv=2025-07-05&sr=c&sp=rwlt&sig=%2B%2BmeEbmIXpL9dejgk%2BRaZn1DkD7HII744dP7kb7sfDA%3D" --overwrite=false --from-to=BlobBlob --s2s-preserve-access-tier=false --check-length=true --include-directory-stub=false --s2s-preserve-blob-tags=false  --recursive --log-level=INFO'
    # os.system(stdstoragetts01wus2)

def get_json_file(metadatafile,savefile):
    data = pd.read_csv(metadatafile, sep=",", encoding="utf-8", low_memory=False)
    with open(savefile, 'w', encoding='utf-8') as s:
        for line in data["Filename"]:
            if ".json" in line:
                s.writelines(line+'\n')
def split_metatda(metadatafile,savedir):
    data1 = pd.read_csv(metadatafile, sep="|", encoding="utf-8")
    save_data = pd.DataFrame()

    for line in data1["sid"]:
        if "XMLYAudiobook01027" in line:
            save_data = save_data._append(data1.iloc[int(list(data1['sid']).index(line))])
    save_files = os.path.join(savedir,"XMLYAudiobook01027.csv")
    save_data.to_csv(save_files,sep="|",encoding='utf8',index=False)

def copy_chunk(filelist):
    with open(filelist,'r',encoding='utf8') as f:
        for line in f.readlines():
            stdstoragetts01wus3_key = '?sv=2025-07-05&st=2025-11-12T07%3A03%3A20Z&se=2025-11-19T07%3A18%3A20Z&skoid=c52a83f4-cefb-4d0c-a81d-a2747c46fd59&sktid=72f988bf-86f1-41af-91ab-2d7cd011db47&skt=2025-11-12T07%3A03%3A20Z&ske=2025-11-19T07%3A18%3A20Z&sks=b&skv=2025-07-05&sr=c&sp=rlt&sig=mX5nYJl3m9pTf0e4LdM1ezVXzDnD5vjN5jTFcVmA54I%3D'
            stdstoragetts01scus_key = '?sv=2025-07-05&st=2025-11-12T07%3A03%3A22Z&se=2025-11-19T07%3A18%3A22Z&skoid=c52a83f4-cefb-4d0c-a81d-a2747c46fd59&sktid=72f988bf-86f1-41af-91ab-2d7cd011db47&skt=2025-11-12T07%3A03%3A22Z&ske=2025-11-19T07%3A18%3A22Z&sks=b&skv=2025-07-05&sr=c&sp=rwlt&sig=7wf82m%2B2aNtenYirY5ZFLE09mkKSbYOdLxXHNXw%2FdSs%3D'
            chunk_name = line.replace("\n","")
            copy_word = f'C:/Users/v-zhazhai/Toosl/code/Tool/merger_tar/azcopy.exe copy "https://stdstoragetts01wus3.blob.core.windows.net/data/realisticttsdataset_v3/train/chunks/tier1/zh-cn/xmly_resize/audiobook_v2/*{stdstoragetts01wus3_key}" "https://stdstoragetts01scus.blob.core.windows.net/data/realisticttsdataset_v3/train/chunks/tier1/zh-cn/xmly_resize/audiobook_v2/{stdstoragetts01scus_key}" --overwrite=false --from-to=BlobBlob --s2s-preserve-access-tier=false --check-length=true --include-directory-stub=false --s2s-preserve-blob-tags=false --recursive --log-level=INFO --include-pattern="{chunk_name}.*"'
            os.system(copy_word)

def download(filename):
    download_word = fr'C:/Users/v-zhazhai/Toosl/code/Tool/merger_tar/azcopy.exe copy "https://stdstoragettsdp01eus.blob.core.windows.net/data/v-honzho/data/podcast/Solo/fr_result/es-ES/1_renamed/audioPath/{filename}?sv=2025-07-05&st=2025-11-24T02%3A14%3A23Z&se=2025-12-01T02%3A29%3A23Z&skoid=c52a83f4-cefb-4d0c-a81d-a2747c46fd59&sktid=72f988bf-86f1-41af-91ab-2d7cd011db47&skt=2025-11-24T02%3A14%3A23Z&ske=2025-12-01T02%3A29%3A23Z&sks=b&skv=2025-07-05&sr=c&sp=rl&sig=XzUDg%2BMcyQ1hvF5p8T60Tvj3lTLLfRmQuiQ1vMrCWQk%3D" "C:\Users\v-zhazhai\Downloads\log\audioPath\{filename}" --overwrite=prompt --check-md5 FailIfDifferent --from-to=BlobLocal --recursive --log-level=INFO'
    os.system(download_word)
def Result_viewing(jsonfile):
    with open(jsonfile, "r",encoding="utf8") as file:
        data = json.load(file)
    duration = data["durationMilliseconds"]
    offset = data["phrases"][0]["offsetMilliseconds"]
    for line in data["phrases"]:
        offset+=line["durationMilliseconds"]
    ratio =  str(round(offset/duration, 3))
    print(ratio)
if __name__ == "__main__":
    # renames("zh","tier1/zh-cn")
    # split_metatda(r"C:\Users\v-zhazhai\Desktop\ZhCNMixiaoquan\metadata_ZhCNMixiaoquan_general.csv",r"C:\Users\v-zhazhai\Desktop\ZhCNMixiaoquan")
    # inputdir = r"C:\Users\v-zhazhai\debug\Chat\chunk_090faaaffa02283259fa1ea2d809cff2_0.audio_48k_denoised_files"
    # for line in os.listdir(inputdir):
    #     os.renames(os.path.join(inputdir,line),
    #                os.path.join(inputdir,line.replace(".wav","")))
    # transdir = r"C:\Users\v-zhazhai\Environment\RealisticTTSDatasets\dataset"
    # for file_path in glob.glob(os.path.join(transdir, "**", "all.txt"), recursive=True):
    #     if "tier2\\zh-hk\\all.txt" in file_path:
    #         with open(file_path,'r',encoding='utf8') as f,open(file_path.replace(".txt","_clean.txt"),'w',encoding="utf8") as s:
    #             for line in f.readlines():
    #                 if "/datablob/realisticttsdataset_v3/train/chunks/tier2/zh-hk/podcast_rss" not in line:
    #                     # print(file_path)
    #                     # break
    #                     s.writelines(line)
    # with open(r"C:\Users\v-zhazhai\Downloads\all.txt",'r',encoding='utf8') as f,open(r"C:\Users\v-zhazhai\Downloads\all_datatset.txt",'w',encoding='utf8') as s:
    #     dataset = []
    #     for line in f.readlines():
    #         if os.path.split(line)[0] not in dataset:
    #             dataset.append(os.path.split(line)[0])
    #             s.writelines(os.path.split(line)[0]+'\n')
    #         # print(os.path.split(line)[0])
    inputdir = r"C:\Users\v-zhazhai\debug\chunk_1498c1d728222abaffb09f43996f310a_0.coarse_segment"
    for file_path in glob.glob(os.path.join(inputdir, "**\\*"), recursive=True):
        # print(file_path)
        if "\et" in file_path:
            save_path = file_path.replace(".coarse_segment","")
            print(save_path)
            os.makedirs(os.path.split(save_path)[0],exist_ok=True)
            # shutil.move(file_path)
            shutil.copyfile(file_path,save_path)