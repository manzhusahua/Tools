import os,multiprocessing
import sys
import shutil

def process_file_list(input_file):
    """
    Args:
        input_file_list (list): The list of floder have script and wave
        local_output_dir (str): The output directory
    """
    try:
        xml_files = os.path.join(input_file,"script",os.path.basename(input_file)+'.xml')
        wavs_files = [x.replace('.wav','') for x in os.listdir(os.path.join(input_file,"wave"))]
        wavs_files.sort()
        print("Start dump to xml for file %s." % xml_files)
        if not os.path.exists(xml_files):
            print("Skipped %s due to file non-exist or not xml file." % xml_files)
        n=0
        with open(xml_files,'r',encoding='utf8') as f,open(xml_files.replace('.xml',"_v1.xml"),'w',encoding='utf8') as s:
            for line in f.readlines():
                if '  <si id="' in line:
                    line = f'  <si id="{wavs_files[n]}">\n'
                    n+=1
                if 'br="5"' in line:
                    line = line.replace('br="5"','br="4"')
                s.writelines(line)
        return 1
    except Exception as e:
        print("Failed updataxml due to %s" % e)
        return 2

def  run(savepath,fileslistpath,start,endcount):    
    fileslsit = []
    with open(fileslistpath,'r',encoding='utf8') as f:
        for line in f.readlines():
            fileslsit.append(line)
    for line in fileslsit[start:endcount]:
        print(line)
        lines = line.replace("\n", "")
        word = 'C:/Users/v-zhazhai/Toosl/Tools/azcopy.exe copy "https://stdstoragettsdp01wus2.blob.core.windows.net/data/run_output/33dbcf7f-b683-4b58-9f16-bbaa552e226c/files_process_output/{}/" "{}" --overwrite=True --check-md5 FailIfDifferent --from-to=BlobLocal --recursive --trusted-microsoft-suffixes=stdstoragettsdp02wus2.blob.core.windows.net --log-level=INFO'.format(lines, savepath)
        print(word)
        os.system(word)
        

        if process_file_list(os.path.join(savepath, lines)) == 1:
            print("done")
            save_word = 'C:/Users/v-zhazhai/Toosl/Tools/azcopy.exe copy "{}" "https://stdstoragettsdp01wus2.blob.core.windows.net/data/run_output/33dbcf7f-b683-4b58-9f16-bbaa552e226c/files_process_output/{}" --overwrite=True --from-to=LocalBlob --blob-type Detect --follow-symlinks --check-length=true --put-md5 --follow-symlinks --disable-auto-decoding=false --recursive --trusted-microsoft-suffixes=stdstoragettsdp02wus2.blob.core.windows.net --log-level=INFO'.format(os.path.join(savepath, lines, "script", lines + "_v1.xml"),"/".join([lines, "script", lines + "_v1.xml"]))
            os.system(save_word)
            if os.path.exists(os.path.join(savepath, lines)):
                shutil.rmtree(os.path.join(savepath, lines))


if __name__ == "__main__":

    # dataset_path = sys.argv[1]
    # filelist = sys.argv[2]
    # with open(filelist,'r',encoding='utf8') as f:
    #     for line in f.readlines():
    #         process_file_list(os.path.join(dataset_path,line))
    savepath = r"C:\Users\v-zhazhai\Downloads\xmly_VIp"
    fileslistpath = r"C:\Users\v-zhazhai\Downloads\xmly_VIp\filenames.txt"
    # run(savepath,fileslistpath,0,1)
    fileslsit = []
    with open(fileslistpath,'r',encoding='utf8') as f:
        for line in f.readlines():
            fileslsit.append(line)
    
    count = int(len(fileslsit)/5)
    
    path1 = multiprocessing.Process(target=run,args=(savepath,fileslistpath,count*0,count*1))
    path1.start()
    
    path2 = multiprocessing.Process(target=run,args=(savepath,fileslistpath,count*1,count*2))
    path2.start()
    
    path3 = multiprocessing.Process(target=run,args=(savepath,fileslistpath,count*2,count*3))
    path3.start()
    
    path4 = multiprocessing.Process(target=run,args=(savepath,fileslistpath,count*3,count*4))
    path4.start()
    
    path5 = multiprocessing.Process(target=run,args=(savepath,fileslistpath,count*4,count*5))
    path5.start()