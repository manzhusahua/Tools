

import os
import json
import pandas as pd
import codecs
import chardet
import shutil


class CREMA_D:
    def get_other(name,csvfiles):
        data1 = pd.read_csv(csvfiles,sep=",",encoding='utf8',low_memory=False)
        index = list(range(data1.shape[0]))
        for i in index:
            line = data1.iloc[i]["ActorID"]
            if str(line) in name:
                Age = data1.iloc[i]["Age"]
                Gender = data1.iloc[i]["Sex"]
                Race = data1.iloc[i]["Race"]
                Ethnicity = data1.iloc[i]["Ethnicity"]
        return Age,Gender,Race,Ethnicity 

    def prepare_json(inputdir,style_map):
        csvfiles = r"C:\Users\v-zhazhai\Downloads\VideoDemographics.csv"
        EmotionLevel_map = {"LO":"Low","MD":"Medium","HI":"High","XX":"Unspecified",}
        names = [x for x in os.listdir(inputdir) if ".txt" in x]
        for name in names:
            try:
                word = open(os.path.join(inputdir,name), "r", encoding="utf8").readlines()[0]
                json_name = name.replace(".txt", ".json")
                style = style_map[name.split('_')[-2]]
                Age,Gender,Race,Ethnicity  = CREMA_D.get_other(name,csvfiles)
                row_values = {
                    "AudioFileName": "{}".format(name.replace(".txt", ".wav")),
                    "Transcription": "{}".format(word),
                    "Style": "{}".format(style),
                    "Age": "{}".format(Age),
                    "Gender": "{}".format(Gender),
                    "EmotionLevel": "{}".format(EmotionLevel_map[name.split("_")[-1].replace('.txt','')]),
                    "Race": "{}".format(Race),
                    "Ethnicity": "{}".format(Ethnicity),
                    "Source": "emotional",
                    }
                with open(os.path.join(inputdir, json_name),"w",encoding="utf8",) as save_json:
                            json.dump(row_values, save_json, indent=4)
            except Exception as e:
                print(f"Failed due to {e}")
                print(f"name is {name}")
                continue

class Emo_DB:
    def prepare_json(inputdir,outputdir):
            Gender_map = {"03":"male", "08":"female", "09":"female", "10":"male",  "11":"male", "12":"male", "13":"female", "14":"female", "15":"male", "16":"female"}
            Age_map = {"03":"31", "08":"34", "09":"21", "10":"32",  "11":"26", "12":"30", "13":"32", "14":"35", "15":"25", "16":"31"}
            trans_map = {"a01":"Der Lappen liegt auf dem Eisschrank.", "a02":"Das will sie am Mittwoch abgeben.", "a04":"Heute abend könnte ich es ihm sagen.", "a05":"Das schwarze Stück Papier befindet sich da oben neben dem Holzstück.", "a07":"In sieben Stunden wird es soweit sein.", "b01":"Was sind denn das für Tüten, die da unter dem Tisch stehen?", "b02":"Sie haben es gerade hochgetragen und jetzt gehen sie wieder runter.",  "b03":"An den Wochenenden bin ich jetzt immer nach Hause gefahren und habe Agnes besucht.", "b09":"Ich will das eben wegbringen und dann mit Karl was trinken gehen.", "b10":"Die wird auf dem Platz sein, wo wir sie immer hinlegen."}
            EmotionLevel_map = {"A":"Angry","B":"Boredom","D":"Disgust","F":"Scared","H":"Happy","S":"Sad","N":"Calm"}
            # EmotionLevel_map = {"W":"Angry","L":"Langeweile","E":"Disgust","A":"Terrified","F":"Happy","T":"Sad"}
            
            names = [x for x in os.listdir(inputdir) if ".wav" in x]
            for name in names:
                try:
                    json_name = name.replace(".wav", ".json")
                    row_values = {
                        "AudioFileName": "{}".format(name.replace(".txt", ".wav")),
                        "Transcription": "{}".format(trans_map[name[2:5]]),
                        "Style": "{}".format(EmotionLevel_map[name[5]]),
                        "Age": "{}".format(Age_map[name[:2]]),
                        "Gender": "{}".format(Gender_map[name[:2]]),
                        "Source": "emotional",
                        }
                    with open(os.path.join(outputdir, json_name),"w",encoding="utf8",) as save_json:
                                json.dump(row_values, save_json, indent=4)
                    with open(os.path.join(outputdir,name.replace(".wav", ".txt")),'w',encoding='utf8') as save_text:
                          save_text.writelines(trans_map[name[2:5]]+'\n')
                    shutil.copyfile(os.path.join(inputdir,name),os.path.join(outputdir,name))
                except Exception as e:
                    print(f"Failed due to {e}")
                    print(f"name is {name}")
                    continue

class yufei:
    def prepare_files(inputdir,outputdir):
            content=codecs.open(inputdir,'rb').read()
            word = open(inputdir,'r',encoding=chardet.detect(content)['encoding']).readlines()
            for line in word:
                name = line.split('\t')[0]
                trans = line.split('\t')[-1].replace('\n','')
                row_values = {
                    "AudioFileName": "{}".format(name+".wav"),
                    "Transcription": "{}".format(trans),
                    "Style": "{}".format("FreeTalk"),
                    # "Gender": "{}".format("Male"),
                    "Source": "Brian",
                    }
                with open(os.path.join(outputdir, name+".json"),"w",encoding="utf8",) as save_json:
                    json.dump(row_values, save_json, indent=4)
                with open(os.path.join(outputdir, name+".txt"),'w',encoding='utf8') as save_text:
                    save_text.writelines(line.split('\t')[-1])
    def prepare_dir(inputdir,outputdir):
            for tran_name in os.listdir(inputdir):
                content=codecs.open(os.path.join(inputdir,tran_name),'rb').read()
                word = open(os.path.join(inputdir,tran_name),'r',encoding=chardet.detect(content)['encoding']).readlines()
                name = tran_name.replace('.txt','')
                row_values = {
                        "AudioFileName": "{}".format(name+".wav"),
                        "Transcription": "{}".format(word[0].replace('\n','')),
                        "Style": "{}".format("FreeTalk"),
                        # "Gender": "{}".format("Male"),
                        "Source": "Brian",
                        }
                with open(os.path.join(outputdir, name+".json"),"w",encoding="utf8",) as save_json:
                        json.dump(row_values, save_json, indent=4)
                shutil.copyfile(os.path.join(inputdir,tran_name),os.path.join(outputdir,tran_name))
    def prepare_Emma(inputdir,outputdir):
            content=codecs.open(inputdir,'rb').read()
            word = open(inputdir,'r',encoding=chardet.detect(content)['encoding']).readlines()
            Styles_mapting = []
            for home, dirs, files in os.walk(r"C:\Users\v-zhazhai\Desktop\recording"):
                 for filename in files:
                      Styles_mapting.append(os.path.join(home, filename))
            
            for line in word:
                name = line.split('\t')[0]
                trans = line.split('\t')[1].replace('\n','')
                try:
                    Style = str([x.split('\\')[-2] for x in Styles_mapting if name in x]).split("'")[1]
                    row_values = {
                        "AudioFileName": "{}".format(name+".wav"),
                        "Transcription": "{}".format(trans),
                        "Style": "{}".format(Style),
                        "Source": "Emma",
                        }
                    with open(os.path.join(outputdir, name+".json"),"w",encoding="utf8",) as save_json:
                        json.dump(row_values, save_json, indent=4)
                    with open(os.path.join(outputdir, name+".txt"),'w',encoding='utf8') as save_text:
                        save_text.writelines(line.split('\t')[-1])
                except Exception as e:
                     print(name)
                     continue
      

if __name__ == "__main__":
        inputdir = r"C:\Users\v-zhazhai\Downloads\Emo-DB\AudioWAV"
        outputdir = r"C:\Users\v-zhazhai\Downloads\Emo-DB\english_prepare"
        if not os.path.exists(outputdir):
            os.makedirs(outputdir, exist_ok=True)
        Emo_DB.prepare_json(inputdir,outputdir)