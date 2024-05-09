import os,sys
import glob

from updata_dataset import UPDATADDATEDET
from get_list import UPDATALIST

updata_dataset = UPDATADDATEDET()
UpdataList = UPDATALIST()


inputdir = sys.argv[1]
outputdir = sys.argv[2]
updata_dataset.run(inputdir,outputdir)
UpdataList.run(inputdir,outputdir)