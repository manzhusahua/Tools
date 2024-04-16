import editdistance
import json,re
import numpy as np
import os

def compute_wer_editdistance(words, ref_words):
    n_SDI = editdistance.eval(words, ref_words)
    if len(ref_words) == 0:
        return 1
    return n_SDI / len(ref_words)

def read_json(json_file):
    with open(json_file, "rt") as f:
        result_json = json.load(f)
    print(result_json)

def remove_punctuation(line):
    punctuation = ",。“”，？！、："
    re_punctuation = "[{}]+".format(punctuation)
    line = re.sub(re_punctuation, "", line)
    return str(line)

def find_tran(transfiles,nameid):
    trans = ''
    for line in transfiles:
        # print(line)
        if nameid in line:
            trans = line.split('\t')[-1]
            break
    return trans

if __name__ == "__main__":

    Trans_path = r"C:\Users\v-zhazhai\debug\richland\F128\General\TextScripts.txt"
    chunk_path = r"C:\Users\v-zhazhai\debug\richland\F128\General\output\chunk"
    wer_save_path  = r"C:\Users\v-zhazhai\debug\richland\F128\General\output\wer1"
    for chun_name in os.listdir(chunk_path):
        if ".audio" in chun_name:
            name = chun_name.replace('.audio','')
            richland_path = os.path.join(chunk_path,name+'.txt')
            whisper_path = os.path.join(chunk_path,name+'.whisper_transcription.txt')
            wer_path = os.path.join(wer_save_path,name+'_wer.txt')
            info_path = os.path.join(chunk_path,name+'.info.txt')

            richland = [x.replace('\n','') for x in open(richland_path,'r',encoding='utf8').readlines()]
            Trans = [x.replace('\n','') for x in open(Trans_path,'r',encoding='utf8').readlines()]
            whisper = [x.replace('\n','') for x in open(whisper_path,'r',encoding='utf8').readlines()]
            info = [x.replace('\n','') for x in open(info_path,'r',encoding='utf8').readlines()]

            
            wers_richland = []
            wers_whisper = []
            print(name)
            n=0
            with open(wer_path,'w',encoding='utf8') as s:
                s.writelines("ID"+'\t'+"Trans"+'\t'+"richland_result"+'\t'+"richland_wer"+'\t'+"whisper_result"+'\t'+"whisper_wer"+'\n')
                while n<len(richland):
                    info_id = info[n].split('/')[-1].replace('.wav','')
                    trans = find_tran(Trans,info_id)
                    # print(trans)
                    Trans_re = remove_punctuation(trans)
                    whisper_re = remove_punctuation(whisper[n])
                    # print(Trans_re)
                    name = Trans[n].split('\t')[0]
                    # print(name)
                    wer_richland = compute_wer_editdistance(Trans_re,richland[n])
                    wers_richland.append(wer_richland)

                    wer_whisper = compute_wer_editdistance(Trans_re,whisper_re)
                    wers_whisper.append(wer_whisper)


                    s.writelines(info_id+'\t'+trans+"\t"+richland[n]+"\t"+str(wer_richland)+'\t'+whisper[n]+'\t'+str(wer_whisper)+'\n')
                    
                    n+=1
            print("wers_richland"+": "+str(np.average(wers_richland)))
            print("wers_whisper"+": "+str(np.average(wers_whisper)))
