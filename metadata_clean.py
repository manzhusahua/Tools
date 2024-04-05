import os,sys
metadta_path = sys.argv[1]
list_path = os.listdir(metadta_path)
head = r"sid|locale|speaker|style|text|phones|durations|speech_length_in_s|speech_path|textless|human_voice|mel_path|sf_path|uv_path|stat_path|syl_phone_num|has_left_context|has_right_context"
i=int(sys.argv[2])
end = int(sys.argv[3])
while i<=end:
    line = "metadata_"+str(i).zfill(5)+".csv"
    metadta = os.path.join(metadta_path,line)
    with open(metadta,'r',encoding='utf8') as f,open(metadta.replace(".csv","_v1.csv"),'w',encoding='utf8') as s:
        s.write(head+"\n")
        for line in f.readlines()[1:]:
            text = line.split("|")[4]
            if (", , , , , , , , , , " in text):
                s.writelines('')
            elif ("………………………" in text):
                s.writelines('')
            elif ("� � � � � � � � " in text):
                s.writelines("")
            elif("---------------" in text):
                s.writelines("")
            elif ("＀＀＀＀＀＀＀＀＀＀＀＀＀＀＀＀＀＀＀" in text):
                s.writelines("")
            elif ("————————" in text):
                s.writelines("")
            else:
                s.writelines(line)
    i+=1
