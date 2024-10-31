import os
import time
import pandas as pandasForSortingCSV
from decimal import Decimal
from distutils.util import strtobool
import os
import sys

input_dir = sys.argv[1]
output_dir = sys.argv[2]
speaker = sys.argv[3]
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
duration_total=0
files=os.listdir(input_dir)
Num=len(files)
for i in range(0,int(Num)):
    input=os.path.join(input_dir,'metadata_'+str(i)+'.csv')
    output=os.path.join(output_dir,'metadata_'+str(i).zfill(5)+'_v1.csv')
    try:
        csvData = pandasForSortingCSV.read_csv(input,sep='|')
        csvData['speaker'] = csvData.apply(lambda x: speaker, axis=1)
        # csvData1= csvData[(csvData.multispeaker_detect_score < 0.9) & (csvData.human_voice)]
        csvData.to_csv(output, sep='|', index=False, header=True)


        csvData2 = pandasForSortingCSV.read_csv(output,sep='|')
        for index, row in csvData2.iterrows():
            duration_total = duration_total + row['speech_length_in_s']
    except Exception as e:
        print(e, type(e))
        print("empty: " + input)
        continue

duration_total = round(duration_total/3600, 2)
print("duration1: " + str(duration_total))