import os,sys
import multiprocessing
import pandas as pd

def updat_sid(metadata_files):
    save_files = "\\".join(metadata_files.split("\\")[:-1])+"_finall\\"+metadata_files.split("\\")[-1]
    data1 = pd.read_csv(metadata_files,sep="|",encoding='utf8',low_memory=False)
    save_data = pd.DataFrame()
    audio_book_names=list(set(["_".join(x.split('_')[2:-2]) for x in data1['sid']]))
    audio_book_names.sort()
    audio_book_jie=list(set([int(x.split('_')[-2]) for x in data1['sid']]))
    audio_book_jie.sort()
    audio_book_chai = list(set([int(x.split('_')[-1]) for x in data1['sid']]))
    audio_book_jie.sort()
    for i in audio_book_names:
        for j in audio_book_jie:
            for m in audio_book_chai:
                for x in data1['sid']:
                    if "_".join([str(i),str(j).zfill(10),str(m)]) in x:
                        save_data = save_data._append(data1.iloc[int(list(data1['sid']).index(x))])
#    save_data['style'] = save_data.apply(lambda x: "FreeTalk" , axis=1)
    save_data.to_csv(save_files,sep="|",encoding='utf8',index=False)
    return save_files

def updat_metadata(metadata_files,speaker_name):
    save_file = metadata_files.replace(".csv","_v2.csv")
    data = pd.read_csv(metadata_files, sep='|', encoding='utf-8')
    index = list(range(data.shape[0]))
    id = []
    for i in index:
        line = data.iloc[i]
        sid = '_'.join(line['sid'].split("_")[-3:])
        if sid not in id:
            id.append(sid)
    for i in index:
        line = data.iloc[i]
        sid = line['sid']
        zhang = line['sid'].split("_")[-2]
        jie = line['sid'].split("_")[-1]
        if str(jie) == "0" and ('_'.join(line['sid'].split("_")[-3:-1])+"_1" in id):
            data.loc[i, 'has_right_context'] = 1
        elif str(jie) == "0" and ('_'.join(line['sid'].split("_")[-3:-2])+"_"+str(int(zhang)+1).zfill(10)+"_0" in id):
            data.loc[i, 'has_right_context'] = 1
        elif str(jie) != "0" and ('_'.join(line['sid'].split("_")[-3:-1])+"_"+str(int(jie)+1) in id):
            data.loc[i, 'has_right_context'] = 1
        elif str(jie) != "0" and ('_'.join(line['sid'].split("_")[-3:-2])+"_"+str(int(zhang)+1).zfill(10)+"_0" in id):
            data.loc[i, 'has_right_context'] = 1
        else:
            data.loc[i, 'has_right_context'] = 0
        
        word = '_'.join(line['sid'].split("_")[-3:-2])+"_"+str(int(zhang)-1).zfill(10)+"_"
        if str(jie) == "0" and (len([x for i,x in enumerate(id) if x.find(word) != -1])!=0):
            data.loc[i, 'has_left_context'] = 1
        elif str(jie) != "0" and ('_'.join(line['sid'].split("_")[-3:-1])+"_"+str(int(jie)-1) in id):
            data.loc[i, 'has_left_context'] = 1
        else:
            data.loc[i, 'has_left_context'] = 0
    data['speaker'] = data.apply(lambda x: speaker_name , axis=1)
    duration_total = [x for x in data['speech_length_in_s']]
    data.to_csv(save_file, sep='|', encoding='utf-8', index=False)
    return sum(duration_total)



def get_registry(metadata_files,speaker_name,locale_name):
    local_output_dir,metadata_name =os.path.split(metadata_files)
    rangeid = str(metadata_name.replace("metadata_",'').replace(".csv",'')).zfill(5)
    registry_path = os.path.join(local_output_dir, rangeid)
    if not os.path.exists(registry_path):
        os.makedirs(registry_path)
    registry_file = os.path.join(registry_path, "registry.csv")
    registrywriter = open(registry_file,'w', encoding='utf-8')
    registrywriter.write('speaker|locale|style|metadata_path\n')
    registrywriter.write("|".join([speaker_name,locale_name,"general","../"])+ metadata_name.replace(".csv","_v2.csv") + '\n')

if __name__ == "__main__":

    input_metadata_path = r"C:\Users\v-zhazhai\Downloads\749"
    speaker_name="XMLYAudiobook00587"
    locale_name="zh-cn"
    input_metadata_list = os.listdir(input_metadata_path)
    if not os.path.exists(input_metadata_path+"_finall"):
        os.makedirs(input_metadata_path+"_finall")
    duration_totals = 0
    for name in input_metadata_list:
        save_files =updat_sid(os.path.join(input_metadata_path,name))
        # duration_total = updat_metadata(save_files,speaker_name)
        # get_registry(save_files,speaker_name,locale_name)
        # duration_totals+=duration_total
    # print("duration1: " + str(round(duration_totals/3600, 2)))