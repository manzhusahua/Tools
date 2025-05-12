import os
import codecs
import chardet
import sys

def V3_filelist_check(file_path,output_folder):
    os.makedirs(output_folder, exist_ok=True)
    feature_list_check_file_size = ["fine_segment", "coarse_segment", "audio", "audio_48k_denoised"]
    content=codecs.open(file_path,'rb').read()
    word = open(file_path,'r',encoding=chardet.detect(content)['encoding']).readlines()
    with open(os.path.join(output_folder,"field.txt"),"w",encoding='utf8') as s:
        for line in file_path:
            chunk_path = os.listdir(os.path.split(line)[0]) 
            for feature in feature_list_check_file_size:
                if line.replace('.json\n',feature) not in chunk_path:
                    # print(f"The {line.replace('.json\n',feature)} is not in the chunk path")
                    s.write(line.replace('.json',feature))


if __name__ == "__main__":
    V3_filelist_check(sys.argv[1],sys.argv[2])