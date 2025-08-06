"""
用于更新V2.1 中xml_dump后sid与音频名字不对应的问题
"""

import pandas as pd
import codecs
import chardet


def updata_xml(metadatfile,xmlfile):
    # data1 = pd.read_csv(metadatfile,sep="|",encoding='utf8',low_memory=False)
    content=codecs.open(metadatfile,'rb').read()
    data1 = [x.split("\t")[0] for x in open(metadatfile,'r',encoding=chardet.detect(content)['encoding']).readlines()]
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


if __name__ == "__main__":
    import os
    txt_path = r"C:\Users\v-zhazhai\Desktop\Vlasta\TextScripts"
    xml_path = r"C:\Users\v-zhazhai\Desktop\Vlasta\XmlScripts"
    for line in os.listdir(txt_path):
        updata_xml(os.path.join(txt_path,line),os.path.join(xml_path,line.replace(".txt",".xml")))