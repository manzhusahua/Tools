import sys

from get_list import UPDATALIST

UpdataList = UPDATALIST()


inputdir = sys.argv[1]
outputdir = sys.argv[2]
UpdataList.run(inputdir,outputdir)