import os,sys

class step3:
    def __init__(self) -> None:
        super().__init__()
    
    def step3_extractvttlist(self,list_file_name,inputdir,batch):
        batch = batch+".txt"
        outputdir = os.path.join(inputdir,os.path.join("v3","step3_extract_tts_filelist"))
        tts_audiolist_file = os.path.join(outputdir, batch)
        if not os.path.exists(outputdir):
            os.makedirs(outputdir)
        for item in list_file_name:
            audiolist_file = os.path.join(inputdir, item, "audioList.txt")
            print(audiolist_file)
            vttfile_column_name = "CaptionFileName"

            audiolist = open(audiolist_file, "r", encoding="utf-8").readlines()
            prefix = item + '\\'
            tts_audio_list = []
            vttindex = -1
            for i, line in enumerate(audiolist):
                if i == 0:
                    if vttfile_column_name not in line:
                        raise Exception("First line should contain 'CaptionFileName' but it does not")
                    ls = line.strip().split("\t")
                    for index, item in enumerate(ls):
                        if item == vttfile_column_name:
                            vttindex = ls.index(item)
                            break
                    if vttindex == -1:
                        raise Exception("CaptionFileName not found in the first line")
                    continue
                line = line.strip()
                lines = line.split("\t")
                if len(lines) > vttindex:
                    vttfile = lines[vttindex]
                    if vttfile != "":
                        tts_audio_list.append(vttfile)
            
            if len(tts_audio_list) > 0:
                for item in tts_audio_list:
                    #print(item)
                    resultstr = prefix + item + '\t' + prefix
                    resultstr1 = resultstr.replace("\\", "/")
                    with open(tts_audiolist_file, "a", encoding="utf-8") as f:
                        f.write(resultstr1)
                        f.write("\n")



if __name__ == "__main__":
    list_file_name = sys.argv[1]
    # list_file_name = [r"FY23Q2\BingYouTube\Education",r"FY23Q2\YouTube\Education",r"FY23Q4-1\YouTube\Education",r"FY23Q4-2\YouTube\Education",r"FY23Q4-3\YouTube\Education",r"FY24Q1-1\YouTube\Education",r"FY24Q1-2\YouTube\Education",r"FY24Q1-3\YouTube\Education",r"FY24Q2-1\YouTube\Education",r"FY24Q2-2\YouTube\Education",r"FY24Q2-3\YouTube\Education",r"FY24Q3-1\YouTube\Education"]
    inputdir = sys.argv[2]
    # inputdir = r"C:\Users\v-zhazhai\Downloads\fr-FR"
    # outputdir = r"C:\Users\v-zhazhai\Downloads\fr-FR\v3\step3_extract_tts_filelist"
    batch = sys.argv[3]
    # batch = "batch03.txt"

    step3.step3_extractvttlist(list_file_name,inputdir,batch)