import re,os

def replace_word_and_phonemes(text,add_tags_trans):
    phonemes = list(set([x.replace('/','') for x in re.findall(r'/[^/]+/', text)])) 
    # 替换每个音标为 <phoneme> 包裹形式
    for phoneme in phonemes:
        add_tags_trans = add_tags_trans.replace(f"/{phoneme}/", f"<lang xml:lang='en-US'><phoneme alphabet='ipa' ph='{phoneme.replace(':','')}'>/{phoneme}/</phoneme></lang>")
    
    # return text
    result = "<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xmlns:mstts='https://www.w3.org/2001/mstts' xml:lang='zh-CN'><voice name='Microsoft Server Speech Text to Speech Voice (zh-CN, YunyangNeural)'>{}</voice></speak>".format(add_tags_trans)
    # print(result)
    return result

def add_lang_tags(sentence):
    add_tags = ''
    for line in re.findall( r'[a-zA-Z]+', sentence):
        add_tags = re.sub(r'([a-zA-Z&;]+)', r"<lang xml:lang='en-US'>\1</lang>", sentence)
    yinbiao = list(set(re.findall(r"/<lang xml:lang='en-US'>[^/]+</lang>*./", add_tags)))    
    print(yinbiao)
    yinbiao1 = list(set(re.findall(r"/<lang xml:lang='en-US'>[^/]+</lang>:/", add_tags)))    
    
    for line in yinbiao:
        add_tags = re.sub(line, line.replace("<lang xml:lang='en-US'>",'').replace("</lang>",""), add_tags)
    # print(add_tags)
    if len(yinbiao1) > 0:
        for line in yinbiao1:
            add_tags = re.sub(line, line.replace("<lang xml:lang='en-US'>",'').replace("</lang>",""), add_tags)
    return add_tags


# 示例句子
scripts_file = r"C:\Users\v-zhazhai\Downloads\scripts.txt"
save_dir = r"C:\Users\v-zhazhai\Downloads\trans"
os.makedirs(save_dir, exist_ok=True)

with open(scripts_file,'r',encoding='utf8') as f:
    for line in f:
        name = line.split('\t')[0]
        sentence = line.split('\t')[-1].replace('\n','')
        add_tags_trans = add_lang_tags(sentence)
        result = replace_word_and_phonemes(sentence, add_tags_trans)
        with open(os.path.join(save_dir,name+".txt"),'w',encoding='utf8') as s:
            
            s.writelines(result + '\n')
# sentence = '/ʊ/。/ʊ/。/ʊ/。单词“book”中，/ʊ/的发音听起来像/u:/。'
# add_tags_trans = add_lang_tags(sentence)
# print(add_tags_trans)
# result = replace_word_and_phonemes(sentence, add_tags_trans)
# print(result)