"""
用于更新V2.1 中xml_dump后sid与音频名字不对应的问题
"""

import pandas as pd
def updata_xml(metadatfile,xmlfile):
    data1 = ["pd.read_csv(metadatfile,sep="|",encoding='utf8',low_memory=False)"]
    n=0
    with open(xmlfile,'r',encoding='utf8') as f,open(xmlfile.replace(".xml","_V1.xml"),'w',encoding='utf8') as s:
        for line in f.readlines():
            if "  <si id=" in line:
                # print(line)
                line = f'  <si id="{str(data1["wav"][n])}">\n'
    # data1['sid']
                n+=1
            s.writelines(line)


if __name__ == "__main__":
    updata_xml(r"C:\Users\v-zhazhai\Desktop\input\metadata.csv",r"C:\Users\v-zhazhai\Desktop\input\script\input.xml")