import sys,os

#拆分大文件
head = "sid|locale|speaker|style|text|phones|durations|speech_length_in_s|speech_path|textless|human_voice|multispeaker_detect_score|mel_path|sf_path|uv_path|stat_path|syl_phone_num|has_left_context|has_right_context"


# metadata_files = sys.argv[1]
metadata_files =  r"C:\Users\v-zhazhai\Desktop\r12\metadata_0_v1.csv"
# save_path = sys.argv[2]
save_path = r"C:\Users\v-zhazhai\Desktop\r12_1"
# os.mkdir(save_path)
# n = sys.argv[3]
n = 0

word=[]
with open(metadata_files,'r',encoding='utf8') as f:
    for line in f.readlines()[1:]:
        word.append(line)
count=int(len(word)/2000)
i=0
while i<=count:
    save_names = int(n)+i
    with open(os.path.join(os.path.join(save_path,"metadata_"+str(save_names)+'.csv')),'w',encoding='utf8') as s:
        s.writelines(head+'\n')
        if 2000*(i+1) < len(word):
            for line in word[2000*i:2000*(i+1)]:
                s.writelines(line)
        else:
            for line in word[2000*i:]:
                s.writelines(line)
    i+=1

