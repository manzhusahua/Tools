import os
import sys
files = sys.argv[1]
with open(files,'r',encoding='utf8') as f,open(files.replace(".txt","_v1.txt"),'w',encoding='utf8') as s:
    chunk_ids = []
    chunk_id = []
    for line in f.readlines()[2:]:
        line = line.split(";")[0].replace("INFO: ",'')
        chunk_ids.append(line)
        line_id = line.split(".")[0]
        if line_id not in chunk_id:
            chunk_id.append(line_id)
    for id in chunk_id:
        if len([i for i,x in enumerate(chunk_ids) if x.find(id)!=-1]) == 7:
            s.writelines(id+'\n')
