import os,sys
import glob
import shutil

class Tools:
    def renames(inputdir,outputdir):
        os.makedirs(outputdir, exist_ok=True)
        n=0
        with open(os.path.join(os.path.split(outputdir)[0],"map.txt"),'w',encoding='utf8') as s:
            for file in glob.glob(os.path.join(inputdir,"**\\*.*"), recursive=True):
                name = os.path.basename(file)
                rename = str(n).zfill(8)+"."+file.split(".")[-1]
                shutil.copyfile(file,os.path.join(outputdir,rename))
                s.writelines(file+'\t'+os.path.join(outputdir,rename)+'\n')
                n+=1

if __name__ == "__main__":
    inputdir = r"C:\Users\v-zhazhai\Downloads\kn-IN"
    outputdir = r"C:\Users\v-zhazhai\Downloads\renames\podcast\kn-IN\rawdata"
    Tools.renames(inputdir,outputdir)