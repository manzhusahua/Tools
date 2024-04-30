import os
import pandas as pd
import sys

class step2:
    def __init__(self) -> None:
        super().__init__()
    
    def step2_extractvttlist(self,inputdir,locals):
        
        output = os.path.join(inputdir,locals+'_statistical.txt')
        
        list_file_name = "audioList.txt"
        FYdirs = os.listdir(inputdir)
        for FYdir in FYdirs:
            FYdirpath = os.path.join(inputdir, FYdir)
            
            if os.path.isdir(FYdirpath):
                Youtubedirs = os.listdir(FYdirpath)
                for Youtubedir in Youtubedirs:
                    Youtubedirpath = os.path.join(FYdirpath, Youtubedir)
                    domaindirs = os.listdir(Youtubedirpath)
                    for domaindir in domaindirs:
                        domaindirpath = os.path.join(Youtubedirpath, domaindir)
                        if not os.path.isdir(domaindirpath):
                            print("not dir:" + domaindirpath)
                            continue
                        sourceaudiolist = os.path.join(domaindirpath, list_file_name)
                        if not os.path.isfile(sourceaudiolist):
                            print("file not exist:" + sourceaudiolist)
                            continue
                        audio_information_list = open(sourceaudiolist, "r", encoding="utf-8").readlines()
                        
                        keys = "AudioFileName	AudioTitle	AudioUrl	Duration	BitRate	SampleRate	SpeechRatio	Snr	CaptionType	CaptionFileName"
                        keys = keys.split("\t")
                        taotalDuration = 0
                        for i, audio_information in enumerate(audio_information_list):
                            if i == 0:
                                continue
                        
                            audio_information = audio_information.strip()
                            audio_items = audio_information.split("\t")
                            if len(keys) == len(audio_items):
                                audio_dict = dict(zip(keys, audio_items))
                                #print(audio_dict["Duration"])
                                taotalDuration = taotalDuration + float(audio_dict["Duration"])
                        taotalDuration = taotalDuration / 3600
                        print(sourceaudiolist)
                        print(taotalDuration)
                        with open(output, "a", encoding="utf-8") as f:
                            f.write(sourceaudiolist + '\t' + str(taotalDuration))
                            f.write("\n")

            else:
                continue
        return output
    
    def step2_statistical(self,statistical_file):
        FY = []
        path1 = []
        domain = []
        path = []
        duration = []

        with open(statistical_file,'r',encoding='utf8') as f:
            for line in f.readlines():
                FY.append(line.split('\t')[-2].split('\\')[-4])
                path1.append(line.split('\t')[-2].split('\\')[-3])
                domain.append(line.split('\t')[-2].split('\\')[-2])
                path.append('\\'.join([line.split('\t')[-2].split('\\')[-4],line.split('\t')[-2].split('\\')[-3],line.split('\t')[-2].split('\\')[-2],"audioList.txt"]))
                duration.append(line.split('\t')[-1].replace('\n',''))
                # SaveData = SaveData._apped([FY,path1,domain,path,duration])
        word = {"FY":FY,"path1": path1,"domain":domain,"path": path,"duration":duration}
        SaveData = pd.DataFrame(word)
        SaveData.to_csv(statistical_file.replace('.txt',".csv"), sep="\t", index=False, header=True)

    def run(self,inputdir,locals):
        # output = r"C:\Users\v-zhazhai\Desktop\TTS\It-IT\YouTube\it-IT_statistical.txt"
        output = self.step2_extractvttlist(inputdir,locals)
        self.step2_statistical(output)
        return output.replace('.txt',".csv")


if __name__ == "__main__":
    inputdir = sys.argv[1]
    locals = sys.argv[2]
    # # step2().step2_statistical(r"C:\Users\v-zhazhai\Desktop\TTS\It-IT\YouTube\it-IT_statistical.txt")
    step2.run(inputdir,locals)