"""
用于更新V2.1 中xml_dump后sid与音频名字不对应的问题
"""

import pandas as pd
import codecs
import chardet
import os
import html
import re

def updata_xml(metadatfile,xmlfile):
    # data1 = pd.read_csv(metadatfile,sep="|",encoding='utf8',low_memory=False)
    content=codecs.open(metadatfile,'rb').read()
    data1 = [x.split("\t")[0] for x in open(metadatfile,'r',encoding=chardet.detect(content)['encoding']).readlines()]
    # data1 = [x.split("|")[0] for x in open(metadatfile,'r',encoding=chardet.detect(content)['encoding']).readlines()[1:]]
    # print(data1)
    n=0
    with open(xmlfile,'r',encoding='utf8') as f,open(xmlfile.replace(".xml","_V1.xml"),'w',encoding='utf8') as s:
        for line in f.readlines():
            if "  <si id=" in line:
                # print(line)
                # line = f'  <si id="{str(data1["wav"][n])}">\n'
                line = f'  <si id="{str(data1[n])}">\n'
    # data1['sid']
                n+=1
            s.writelines(line)

def add_lang_tags(text, chunk_locale):
    if chunk_locale == "zh-cn":
        text_new = html.escape(text.replace('\n','')).replace('&#x27;',"\'")
        if re.compile(r'[a-zA-Z]+').search(text_new):
                add_tags = re.sub(r'([a-zA-Z&;]+)', r"<lang xml:lang='en-US'>\1</lang>", text_new)
                result = "<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xmlns:mstts='https://www.w3.org/2001/mstts' xml:lang='zh-CN'><voice name='Microsoft Server Speech Text to Speech Voice (zh-CN, YunyangNeural)'>{}</voice></speak>".format(add_tags).replace("</lang>'<lang xml:lang='en-US'>","\'")
        else:
                result = text_new
    else:
        result = text
    return result
    
if __name__ == "__main__":
    # txt_path = r"C:\Users\v-zhazhai\Downloads\xml_dump\input\script"
    # xml_path = r"C:\Users\v-zhazhai\Desktop\Vlasta\XmlScripts"
    # for line in os.listdir(txt_path):
    #     updata_xml(os.path.join(txt_path,line),os.path.join(xml_path,line.replace(".txt",".xml")))
    
    updata_xml(r"C:\Users\v-zhazhai\Downloads\xpboy\0000000501-0000001000.txt",r"C:\Users\v-zhazhai\Downloads\xpboy\0000000501-0000001000.xml")


    # inputfile = r"C:\Users\v-zhazhai\Downloads\xpboy\shao4.txt"
    # savefile = r"C:\Users\v-zhazhai\Downloads\xpboy\shao4_1.txt"
    # chunk_locale = "zh-cn"
    # with open(inputfile,'r',encoding='utf8') as f,open(savefile,'w',encoding='utf8') as s:
    #     for line in f.readlines():
    #         isd = line.split("\t")[0]
    #         trans = line.split("\t")[-1].replace("\n","")
    #         text = add_lang_tags(trans,chunk_locale)
    #         s.writelines(f"{isd}\t{trans}\n")