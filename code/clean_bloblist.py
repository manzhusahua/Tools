import os
import sys
# files = sys.argv[1]
def clean():
    files = r"C:\Users\v-zhazhai\Downloads\all_v1.txt"
    with open(files,'r',encoding='utf8') as f,open(files.replace(".txt","_v1.txt"),'w',encoding='utf8') as s:
        chunk_ids = []
        chunk_id = []
        for line in f.readlines()[2:]:
            line = line.split(";")[0].replace("INFO: ",'')
            if ".json\n" in line and ".json.version_" not in line:
                s.writelines(line+'\n')
                
                # chunk_ids.append(line)
        #     line_id = line.split(".")[0]
        #     # if line_id not in chunk_id :
        #     #     chunk_id.append(line_id)
        # for id in chunk_id:
        #     if len([i for i,x in enumerate(chunk_ids) if x.find(id)!=-1]) == 7:
            s.writelines(line+'\n')

def replace(files):
    word = list(set(open(files,'r',encoding='utf8').readlines()))
    with open(files.replace('.txt',"_clean.txt"),'w',encoding='utf8') as s:
        for line in word:
            s.writelines(line)

if __name__ == "__main__":
    replace(r"C:\Users\v-zhazhai\Downloads\all_v1_v1.txt")