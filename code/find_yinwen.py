import re
import os
import sys
import codecs 
import chardet
import csv


files = sys.argv[1]
name = os.path.split(files)[-1]

path = os.path.split(files)[0]

erhua_path1  = os.path.join(path,"erhua")
erhua_path2  = os.path.join(erhua_path1,"TextScripts")
if not os.path.exists(erhua_path1):
    os.makedirs(erhua_path1, exist_ok=True)
if not os.path.exists(erhua_path2):
    os.makedirs(erhua_path2, exist_ok=True)


mixligual_path1  = os.path.join(path,"mixligual")
mixligual_path2  = os.path.join(mixligual_path1,"TextScripts")
if not os.path.exists(mixligual_path1):
    os.makedirs(mixligual_path1, exist_ok=True)
if not os.path.exists(mixligual_path2):
    os.makedirs(mixligual_path2, exist_ok=True)

yinwen_files = os.path.join(mixligual_path2,name.replace(".txt","_yinwen.txt"))
zhongwen_files = os.path.join(erhua_path2,name.replace(".txt","_zongwen.txt"))
with open(yinwen_files,"w",encoding='utf8') as s1,open(zhongwen_files,'w',encoding='utf8') as s2:
    content=codecs.open(files,'rb').read()
    f = open(files,'r',encoding=chardet.detect(content)['encoding'])
    for line in f.readlines():
        my_re = re.compile(r'[A-Za-z]', re.S)
        res = re.findall(my_re, line)
        if len(res) !=0:
            s1.writelines(line)
        else:
            s2.writelines(line)
        