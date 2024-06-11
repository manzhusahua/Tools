import os,sys
import pandas as pandasForSortingCSV
import multiprocessing
import difflib

def updata_context(metadta_path,output_metadata_file):
    data = pandasForSortingCSV.read_csv(metadta_path, sep='|', encoding='utf-8',low_memory=False)
    index = list(range(data.shape[0]))
    id = []
    for i in index:
        line = data.iloc[i]
        sid = '_'.join(line['sid'].split("_")[-3:])
        if sid not in id:
            id.append(sid)
    for i in index:
        line = data.iloc[i]
        # duration_total = duration_total + line['speech_length_in_s']
        sid = line['sid']
        zhang = sid.split("_")[-2]
        jie = sid.split("_")[-1]
        if str(jie) == "0" and (sid.split("_")[-3]+"_"+sid.split("_")[-2]+"_1" in id):
            data.loc[i, 'has_right_context'] = 1
        elif str(jie) == "0" and (sid.split("_")[-3]+"_"+str(int(zhang)+1).zfill(10)+"_0" in id):
            data.loc[i, 'has_right_context'] = 1
        elif str(jie) != "0" and (sid.split("_")[-3]+"_"+sid.split("_")[-2]+"_"+str(int(jie)+1) in id):
            data.loc[i, 'has_right_context'] = 1
        elif str(jie) != "0" and (sid.split("_")[-3]+"_"+str(int(zhang)+1).zfill(10)+"_0" in id):
            data.loc[i, 'has_right_context'] = 1
        else:
            data.loc[i, 'has_right_context'] = 0
        
        word = sid.split("_")[-3]+"_"+str(int(zhang)-1).zfill(10)+"_"
        # chunk6624ee2cb51911ee97f5000d3ae5703a_000004_00000_0000400000_0
        # chunk421235dab51911ee97f5000d3ae5703a_000001_00000_0000400001_0
        if str(jie) == "0" and (len([x for i,x in enumerate(id) if x.find(word) != -1]) !=0):
            # print(len([x for i,x in enumerate(id) if x.find(word) != -1]))
            data.loc[i, 'has_left_context'] = 1
        elif str(jie) != "0" and (sid.split("_")[-2]+"_"+str(int(jie)-1) in id):
            data.loc[i, 'has_left_context'] = 1
        else:
            data.loc[i, 'has_left_context'] = 0
    # data['speaker'] = data.apply(lambda x: "enUSLibrilight", axis=1)
    
    data.to_csv(output_metadata_file, sep='|', encoding='utf-8', index=False)

def run_word(metadta_path_list,metadta_path):
    for line in metadta_path_list:
        updata_context(os.path.join(metadta_path,line),os.path.join(metadta_path+"_updata_context",line))

if __name__ == "__main__":
    # updata_context(r"C:\Users\v-zhazhai\Downloads\metadata_0 (1)_v1.csv",r"C:\Users\v-zhazhai\Downloads\metadata_0 (1)_v2.csv")
    # input_metadata_path = sys.argv[1]
    input_metadata_path = r"C:\Users\v-zhazhai\Downloads\749_finall"
    input_metadata_list = os.listdir(input_metadata_path)
    if not os.path.exists(input_metadata_path+"_updata_context"):
        os.makedirs(input_metadata_path+"_updata_context", exist_ok=True)
    # updata_context(r"C:\Users\v-zhazhai\Downloads\metadata_0_v2.csv",r"C:\Users\v-zhazhai\Downloads\metadata_0_v3.csv")
    # os.remove(r"C:\Users\v-zhazhai\Downloads\metadata_0_v2.csv")
    # os.remove(r"C:\Users\v-zhazhai\Downloads\metadata_0.csv")
    # os.remove(r"C:\Users\v-zhazhai\Downloads\metadata_0_v1.csv")
    # os.rename(r"C:\Users\v-zhazhai\Downloads\metadata_0_v3.csv",r"C:\Users\v-zhazhai\Downloads\metadata_0_v2.csv")
    n=int(len(input_metadata_list)/5)
    path1 = multiprocessing.Process(target=run_word,args=(input_metadata_list[n*0:n*1],input_metadata_path))
    path1.start()

    path2 = multiprocessing.Process(target=run_word,args=(input_metadata_list[n*1:n*2],input_metadata_path))
    path2.start()

    path3 = multiprocessing.Process(target=run_word,args=(input_metadata_list[n*2:n*3],input_metadata_path))
    path3.start()

    path4 = multiprocessing.Process(target=run_word,args=(input_metadata_list[n*3:n*4],input_metadata_path))
    path4.start()

    path5 = multiprocessing.Process(target=run_word,args=(input_metadata_list[n*4:],input_metadata_path))
    path5.start()