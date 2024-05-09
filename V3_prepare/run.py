import os
from step1_getaudioList import STEP1
from step2_extractvttlist import step2
from step3_extractvttlist import step3
from step4_dump_json import step4
from step5_UpdataBlob import step5
import pandas as pd

locals = "ja-JP"
inputdir = r"C:\Users\v-zhazhai\Desktop\TTS\ja-JP\YouTube"
if not os.path.exists(inputdir):
    os.makedirs(inputdir, exist_ok=True)

step1 = STEP1()
step2 = step2()
step3 = step3()
step4 = step4()
step5 = step5()

print("step1_getaudioList start")
step1.run(inputdir,locals)
print("step2_extractvttlist start")
statistical_file = step2.run(inputdir,locals)
# statistical_file = r"C:\Users\v-zhazhai\Desktop\TTS\It-IT\YouTube\it-IT_statistical.csv"
data = pd.read_csv(statistical_file,sep="\t",encoding='utf8',low_memory=False)
path_list = [str(x.replace('\\audioList.txt','')) for x in data["path"]]
domain_list = list(set([x for x in data["domain"]]))
domain_list.sort()
mapelist = []
n = 1
for line in domain_list:
    batch = "batch"+str(n).zfill(2)
    list_file_name = [x for i,x in enumerate(path_list) if x.find(line) != -1]
    mapelist.append(line+'  '+batch)

    print("step3_extractvttlist {} start".format(line))
    step3.step3_extractvttlist(list_file_name,inputdir,batch)
    print("step4_dump_json {} start".format(line))
    step4.step4_dump_json(list_file_name,inputdir,batch)

    # print("step5_updata_tts_filelist start")
    # step5.step5_updata_tts_filelist(locals,inputdir,batch)
    # print("step5_updata_dump_json start")
    # step5.step5_updata_dump_json(locals,inputdir,batch)

    n+=1
print(mapelist)