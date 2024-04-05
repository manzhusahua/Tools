import os,re,sys
import pandas as pd


def clean_metadata(metadata_path):
    save_data = pd.DataFrame()
    data1 = pd.read_csv(metadata_path,sep="|",encoding="utf8")
    for i in range(len(data1)):
        print(data1.iloc[i]['sid'])
        if (re.search(r'\[.*?\]',data1.iloc[i]['text'])) == None:
                save_data = save_data._append(data1.iloc[i])
    return save_data


def merger_metadata(metadata_path,save_path):
    # if not os.path.exists(metadata_path+"_v1"):
    #     os.mkdir(metadata_path+"_v1")
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    sve_data = pd.DataFrame()
    metadata_list = os.listdir(metadata_path)
    m=0
    for name in metadata_list:
         if "metadata_" not in name:
            data1 = clean_metadata(os.path.join(metadata_path,name))
            sve_data = sve_data._append(data1)
            if len(sve_data)>2000:
                sve_data.to_csv(os.path.join(save_path,"metadata_"+str(m)+".csv"), sep="|", index=False, header=True)
                m+=1
                sve_data = pd.DataFrame()
            if name == metadata_list[-1]:
                sve_data.to_csv(os.path.join(save_path,"metadata_"+str(m)+".csv"), sep="|", index=False, header=True)

if __name__ == "__main__":
     metadata_path = r"C:\Users\v-zhazhai\Downloads\1111"
     save_path =  r"C:\Users\v-zhazhai\Downloads\1112"
     merger_metadata(metadata_path,save_path)