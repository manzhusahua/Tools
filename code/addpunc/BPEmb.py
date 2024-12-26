import sys
sys.path.append("./lib")

import re
from bpemb import BPEmb
# from addpunc.bpemb import BPEmb
import argparse

# parser=argparse.ArgumentParser('''
#                                Byte pair encoding (BPEmb)
#                                commands:
#                                    BPEmain.py -i input.tsv -o output.tsv
#                                    ''')
# parser.add_argument("-inputFile","-i",required=True)
# parser.add_argument("-outputFile","-o",required=True)

# args=parser.parse_args()

# inpath=args.inputFile
# outpath=args.outputFile

multibpemb=BPEmb(lang="zh",vs=100000,dim=300,cache_dir="model")

def BPEencode(text):
    text=text.strip()
    text=re.sub(r"(\S)。",r"\1",text)
    text=re.sub(r"(\S)，",r"\1",text)
    text=re.sub(r"(\S)？",r"\1",text)
    subwords=multibpemb.encode(text)
    bpe_sent=" ".join(subwords)
    bpe_sent=re.sub(r"\s+▁(，)",r'\1',bpe_sent)
    bpe_sent=re.sub(r"\s+▁(。)",r'\1',bpe_sent)
    bpe_sent=re.sub(r"\s+▁(？)",r'\1',bpe_sent)
    bpe_sent=bpe_sent.replace("▁","")
    bpe_sent=re.sub(r"\s+(')",r'\1',bpe_sent)
    bpe_sent=re.sub(r"\s{2,}"," ",bpe_sent)
    return bpe_sent

def BPEmain(inpath, outpath):
    with open(inpath,'r',encoding='utf-8') as fi, open(outpath,'w',encoding='utf-8') as fo:
        for line in fi:
            line = line.replace("\n", "")
            bpe_sent=BPEencode(line)
            fo.write(bpe_sent.strip()+'\n')