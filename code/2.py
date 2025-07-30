import os


inputdir  = r"C:\Users\v-zhazhai\Downloads\std_log.txt"
words = []
with open(inputdir,'r',encoding='utf8') as f:
    for line in f.readlines():
        if "error in processing " in line:
            # print(line)
            word = line.split(":")[0].replace("error in processing ","")
            word1 = "/".join(word.split("/")[:-1])
            # print(word1)
            if word1 not in words:
                words.append(word1)
for line in words:
    print(line)