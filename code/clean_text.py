import os

def clean(files):
    with open(files,'r',encoding='utf8') as f,open(files.replace(".txt","_v1.txt"),'w',encoding='utf8') as s:
        word = "😉😊🤔❤😥🤩😆☕️🐒🥰😫🐻‍❄✨😣🤗😄🌈🎉💪🐱🌷💐🌺🎁💖🐰🙌🎶📸✌⚽🏆🙋🦌😍😋💕🐾😢😃🦋🐐😟🎵😏😭🌞🌱😎👍😜🌼🌸😡"
        for line in f.readlines():
            for i in word:
                if i in line:
                    line = line.replace(i,"")
            s.writelines(line)
    os.remove(files)
    os.renames(files.replace(".txt","_v1.txt"),files)

def find(files):
    with open(files,'r',encoding='utf8') as f,open(files.replace(".txt","_word.txt"),'w',encoding='utf8') as s:
        word=[]
        for line in f.readlines():
            for i in line.split('\t')[-1].replace('\n',''):
                if i not in word:
                    word.append(i)
                    s.writelines(i)

def clean_list(inputdir,savedir,word):
    
    with open(inputdir,'r',encoding='utf8') as f:
        for line in f.readlines():
            if ".wav;" in line:
                batchname = line.split("/")[0].replace("INFO: ","")
                wav_name = line.split(";")[0].replace("INFO: ","")
                with open(os.path.join(savedir,batchname+'.txt'),'a',encoding='utf8') as s:
                    s.writelines("/".join([word,wav_name])+"\n")
    
if __name__ == "__main__":
    # files = r"D:\users\v-zhazhai\TTS\zh-CN\OPOP\xiaobu\batch_4_repeat_prompt\batch_4_repeat_prompt_clean.txt"
    # clean(files)
    # find(files)
    clean_list(r"C:\Users\v-zhazhai\Downloads\filelist\te-IN.txt",r"C:\Users\v-zhazhai\Downloads\filelist\filelist","/datablob/TTS_ChunkData/Youtube/v3/Youtube_temp/te-IN")
        