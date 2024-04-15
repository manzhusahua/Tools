# from jsonpath import jsonpath
import json

def read_json(input_file):
    tmp = []
    file = open(input_file, 'r', encoding='utf-8').readlines()[0]
    file = str(file[file.index("{"):]).split('"Audio":')
    for line in file[1:]:
        # tmp.append('"Audio":')
        tmp.append(line.split(',')[0]+'\t')
        if '"FullTranscription":' in line:
            # tmp.append('"FullTranscription":')
            word = line.split('"FullTranscription":')[-1].split('}')[0]
            word = word.encode().decode("unicode_escape")
            tmp.append(word+'\n')

    with open(input_file.replace('richland_result','txt'),'w',encoding='utf8') as s:
        for line in tmp:
            s.writelines(line)

if __name__ == "__main__":
    input_file = r"C:\Users\v-zhazhai\Downloads\chunk_f44df0a7d14324431e1fd83408946072_0.richland_result"
    read_json(input_file)