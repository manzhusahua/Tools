import os
import json
import pandas as pd
import codecs
import chardet
import shutil
import re
import glob
import requests

class CREMA_D:
    def get_other(name, csvfiles):
        data1 = pd.read_csv(csvfiles, sep=",", encoding="utf8", low_memory=False)
        index = list(range(data1.shape[0]))
        for i in index:
            line = data1.iloc[i]["ActorID"]
            if str(line) in name:
                Age = data1.iloc[i]["Age"]
                Gender = data1.iloc[i]["Sex"]
                Race = data1.iloc[i]["Race"]
                Ethnicity = data1.iloc[i]["Ethnicity"]
        return Age, Gender, Race, Ethnicity

    def prepare_json(inputdir, style_map):
        csvfiles = r"C:\Users\v-zhazhai\Downloads\VideoDemographics.csv"
        EmotionLevel_map = {
            "LO": "Low",
            "MD": "Medium",
            "HI": "High",
            "XX": "Unspecified",
        }
        names = [x for x in os.listdir(inputdir) if ".txt" in x]
        for name in names:
            try:
                word = open(
                    os.path.join(inputdir, name), "r", encoding="utf8"
                ).readlines()[0]
                json_name = name.replace(".txt", ".json")
                style = style_map[name.split("_")[-2]]
                Age, Gender, Race, Ethnicity = CREMA_D.get_other(name, csvfiles)
                row_values = {
                    "AudioFileName": "{}".format(name.replace(".txt", ".wav")),
                    "Transcription": "{}".format(word),
                    "Style": "{}".format(style),
                    "Age": "{}".format(Age),
                    "Gender": "{}".format(Gender),
                    "EmotionLevel": "{}".format(
                        EmotionLevel_map[name.split("_")[-1].replace(".txt", "")]
                    ),
                    "Race": "{}".format(Race),
                    "Ethnicity": "{}".format(Ethnicity),
                    "Source": "emotional",
                }
                with open(
                    os.path.join(inputdir, json_name),
                    "w",
                    encoding="utf8",
                ) as save_json:
                    json.dump(row_values, save_json, indent=4)
            except Exception as e:
                print(f"Failed due to {e}")
                print(f"name is {name}")
                continue

class Emo_DB:
    def prepare_json(inputdir, outputdir):
        Gender_map = {
            "03": "male",
            "08": "female",
            "09": "female",
            "10": "male",
            "11": "male",
            "12": "male",
            "13": "female",
            "14": "female",
            "15": "male",
            "16": "female",
        }
        Age_map = {
            "03": "31",
            "08": "34",
            "09": "21",
            "10": "32",
            "11": "26",
            "12": "30",
            "13": "32",
            "14": "35",
            "15": "25",
            "16": "31",
        }
        trans_map = {
            "a01": "Der Lappen liegt auf dem Eisschrank.",
            "a02": "Das will sie am Mittwoch abgeben.",
            "a04": "Heute abend könnte ich es ihm sagen.",
            "a05": "Das schwarze Stück Papier befindet sich da oben neben dem Holzstück.",
            "a07": "In sieben Stunden wird es soweit sein.",
            "b01": "Was sind denn das für Tüten, die da unter dem Tisch stehen?",
            "b02": "Sie haben es gerade hochgetragen und jetzt gehen sie wieder runter.",
            "b03": "An den Wochenenden bin ich jetzt immer nach Hause gefahren und habe Agnes besucht.",
            "b09": "Ich will das eben wegbringen und dann mit Karl was trinken gehen.",
            "b10": "Die wird auf dem Platz sein, wo wir sie immer hinlegen.",
        }
        EmotionLevel_map = {
            "A": "Angry",
            "B": "Boredom",
            "D": "Disgust",
            "F": "Scared",
            "H": "Happy",
            "S": "Sad",
            "N": "Calm",
        }
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
                with open(
                    os.path.join(outputdir, json_name),
                    "w",
                    encoding="utf8",
                ) as save_json:
                    json.dump(row_values, save_json, indent=4)
                with open(
                    os.path.join(outputdir, name.replace(".wav", ".txt")),
                    "w",
                    encoding="utf8",
                ) as save_text:
                    save_text.writelines(trans_map[name[2:5]] + "\n")
                shutil.copyfile(
                    os.path.join(inputdir, name), os.path.join(outputdir, name)
                )
            except Exception as e:
                print(f"Failed due to {e}")
                print(f"name is {name}")
                continue

class yufei:
    def prepare_files(inputdir, outputdir):
        content = codecs.open(inputdir, "rb").read()
        word = open(
            inputdir, "r", encoding=chardet.detect(content)["encoding"]
        ).readlines()
        for line in word:
            name = line.split("\t")[0]
            trans = line.split("\t")[-1].replace("\n", "")
            row_values = {
                "AudioFileName": "{}".format(name + ".wav"),
                "Transcription": "{}".format(trans),
                "Style": "{}".format("FreeTalk"),
                # "Gender": "{}".format("Male"),
                "Source": "Brian",
            }
            with open(
                os.path.join(outputdir, name + ".json"),
                "w",
                encoding="utf8",
            ) as save_json:
                json.dump(row_values, save_json, indent=4)
            with open(
                os.path.join(outputdir, name + ".txt"), "w", encoding="utf8"
            ) as save_text:
                save_text.writelines(line.split("\t")[-1])

    def prepare_dir(inputdir, outputdir):
        for tran_name in os.listdir(inputdir):
            content = codecs.open(os.path.join(inputdir, tran_name), "rb").read()
            word = open(
                os.path.join(inputdir, tran_name),
                "r",
                encoding=chardet.detect(content)["encoding"],
            ).readlines()
            name = tran_name.replace(".txt", "")
            row_values = {
                "AudioFileName": "{}".format(name + ".wav"),
                "Transcription": "{}".format(word[0].replace("\n", "")),
                "Style": "{}".format("FreeTalk"),
                # "Gender": "{}".format("Male"),
                "Source": "Brian",
            }
            with open(
                os.path.join(outputdir, name + ".json"),
                "w",
                encoding="utf8",
            ) as save_json:
                json.dump(row_values, save_json, indent=4)
            shutil.copyfile(
                os.path.join(inputdir, tran_name), os.path.join(outputdir, tran_name)
            )

    def prepare_Emma(inputdir, outputdir):
        content = codecs.open(inputdir, "rb").read()
        word = open(
            inputdir, "r", encoding=chardet.detect(content)["encoding"]
        ).readlines()
        Styles_mapting = []
        for home, dirs, files in os.walk(r"C:\Users\v-zhazhai\Desktop\recording"):
            for filename in files:
                Styles_mapting.append(os.path.join(home, filename))

        for line in word:
            name = line.split("\t")[0]
            trans = line.split("\t")[1].replace("\n", "")
            try:
                Style = str(
                    [x.split("\\")[-2] for x in Styles_mapting if name in x]
                ).split("'")[1]
                row_values = {
                    "AudioFileName": "{}".format(name + ".wav"),
                    "Transcription": "{}".format(trans),
                    "Style": "{}".format(Style),
                    "Source": "Emma",
                }
                with open(
                    os.path.join(outputdir, name + ".json"),
                    "w",
                    encoding="utf8",
                ) as save_json:
                    json.dump(row_values, save_json, indent=4)
                with open(
                    os.path.join(outputdir, name + ".txt"), "w", encoding="utf8"
                ) as save_text:
                    save_text.writelines(line.split("\t")[-1])
            except Exception as e:
                print(name)
                continue

class MELD:
    def prepare_json(inputdir, outputdir):
        content = codecs.open(inputdir, "rb").read()
        word = open(
            inputdir, "r", encoding=chardet.detect(content)["encoding"]
        ).readlines()
        matched_elements = [item for item in word if re.search("dia", item)]
        for line in matched_elements:
            Transcription, Style, Speaker = "", "", ""
            try:
                for lines in word[word.index(line) : word.index(line) + 12]:
                    if "  Utterance: " in lines:
                        Transcription = lines.split(": ")[-1].replace("\n", "")
                        continue
                    if "  Emotion: " in lines:
                        Style = lines.split(": ")[-1].replace("\n", "")
                        continue
                    if "Speaker: " in lines:
                        Speaker = lines.split(": ")[-1].replace("\n", "")
                        continue
                row_values = {
                    "AudioFileName": "{}".format(line.split(":")[0] + ".wav"),
                    "Transcription": "{}".format(Transcription),
                    "Style": "{}".format(Style),
                    "Speaker": "{}".format(Speaker),
                    "Source": "emotional",
                }
                with open(
                    os.path.join(outputdir, line.split(":")[0] + ".json"),
                    "w",
                    encoding="utf8",
                ) as save_json:
                    json.dump(row_values, save_json, indent=4)
                with open(
                    os.path.join(outputdir, line.split(":")[0] + ".txt"),
                    "w",
                    encoding="utf8",
                ) as save_text:
                    save_text.writelines(Transcription + "\n")
                # print(word[word.index(line) + 2])
            except Exception as e:
                print(f"Failed due to {e}")
                print(f"name is {line}")
                continue

class RAVDESS:
    def prepare_json(inputdir, outputdir):
        Emotion = {"01":"neutral", "02":"calm", "03":"happy", "04":"sad", "05":"angry", "06":"fearful", "07":"disgust", "08":"surprised"}
        Transcription = {"01":"Kids are talking by the door", "02":"Dogs are sitting by the door"}
        Emotional_intensity = {"01":"normal", "02":"strong"}
        for home, dirs, files in os.walk(inputdir):
            for filename in files:
                try:
                    filenames = filename.replace(".wav","").split("-")
                    Gender = ''
                    if int(filenames[-1])%2==0:
                        Gender = "male"
                    else:
                        Gender = "female"
                    row_values = {
                        "AudioFileName": "{}".format(filename),
                        "Transcription": "{}".format(Transcription[filenames[4]]),
                        "Style": "{}".format(Emotion[filenames[2]]),
                        "Emotional_intensity": "{}".format(Emotional_intensity[filenames[3]]),
                        "Gender": "{}".format(Gender),
                        "Source": "emotional",
                        }
                    with open(os.path.join(outputdir, filename.replace(".wav",".json")), "w",encoding="utf8",) as save_json:
                        json.dump(row_values, save_json, indent=4)
                    with open(os.path.join(outputdir, filename.replace(".wav",".txt")),"w",encoding="utf8",) as save_text:
                        save_text.writelines(Transcription[filenames[4]] + "\n")
                except Exception as e:
                    print(f"Failed due to {e}")
                    print(f"name is {filename}")
                    continue

class EMNS:
    def prepare_json(inputmetadata, outputdir):
        data = pd.read_csv(inputmetadata,sep="|",encoding='utf8',low_memory=False)
        index = list(range(data.shape[0]))
        for i in index:
            try:
                line = data.iloc[i]
                name = line["audio_recording"].split('/')[-1].replace('.webm','')
                row_values = {
                        "AudioFileName": "{}".format(name+'.wav'),
                        "Transcription": "{}".format(line["utterance"]),
                        "Style": "{}".format(line["emotion"]),
                        "Gender": "{}".format(line["gender"]),
                        "Source": "emotional",
                        }
                with open(os.path.join(outputdir, name+".json"), "w",encoding="utf8",) as save_json:
                        json.dump(row_values, save_json, indent=4)
                with open(os.path.join(outputdir,  name+".txt"),"w",encoding="utf8",) as save_text:
                    save_text.writelines(line["utterance"] + "\n")
            except Exception as e:
                print(f"Failed due to {e}")

class AISHELL_3:
    def find_values(names):
        map = pd.read_csv(r"C:\Users\v-zhazhai\Desktop\data_aishell3\spk-info.csv",sep="|",encoding='utf8',low_memory=False)
        index = list(range(map.shape[0]))
        age_group,gender,accent = "","",""
        for i in index:
            line = map.iloc[i]
            if line['Names'] == names:
                age_group = map.iloc[i]["age group"]
                gender = map.iloc[i]["gender"]
                accent = map.iloc[i]["accent"]
        return age_group,gender,accent

    def prepare_json(inputdir, outputdir):
        content = codecs.open(inputdir, "rb").read()
        word = open(inputdir, "r", encoding=chardet.detect(content)["encoding"]).readlines()
        for line in word:
            try:
                AudioFileName = line.split('\t')[0]
                Transcription = ''
                for n in range(0,len(line.split('\t')[-1].split(" ")),2):
                    Transcription+=line.split('\t')[-1].split(" ")[n]

                age_group,gender,accent = AISHELL_3.find_values(AudioFileName[:7])
                row_values = {
                                    "AudioFileName": "{}".format(AudioFileName),
                                    "Transcription": "{}".format(Transcription),
                                    "AgeRroup": "{}".format(age_group),
                                    "Gender": "{}".format(gender),
                                    "Accent": "{}".format(accent),
                                    "DataName": "{}".format("AISHELL-3"),
                                    "Source": "emotional",
                                }
                with open(os.path.join(outputdir, AudioFileName.replace(".wav",".json")),"w",encoding="utf8",) as save_json:
                    json.dump(row_values, save_json, indent=4)
                with open(os.path.join(outputdir, AudioFileName.replace(".wav",".txt")),"w",encoding="utf8",) as save_text:
                    save_text.writelines(Transcription)
                # print(word[word.index(line) + 2])
            except Exception as e:
                print(f"Failed due to {e}")
                print(f"name is {line}")
                continue

class URDU:
    def prepare_json(inputdir, outputdir):
        Gender_map = {"M":"Male","F":"Female"}
        Emotion_map = {"A":"Angery","H":"Happy","N":"Neutral","S":"Sad"}
        for file_path in glob.glob(os.path.join(inputdir, "**", "*.wav"), recursive=True):
            AudioFileName = os.path.basename(file_path)
            Gender = AudioFileName.split("_")[0][1]
            Emotion = AudioFileName.split("_")[0][0]
            row_values = {
                "AudioFileName": "{}".format(AudioFileName),
                "Gender": "{}".format(Gender_map[Gender]),
                "Emotion": "{}".format(Emotion_map[Emotion]),
                "DataName": "{}".format("URDU-Dataset"),
                "Source": "emotional",
                }
            with open(os.path.join(outputdir, AudioFileName.replace(".wav",".json")),"w",encoding="utf8",) as save_json:
                json.dump(row_values, save_json, indent=4)

class TurEVDB:
    def prepare_json(inputdir, outputdir):
        for file_path in glob.glob(os.path.join(inputdir, "**", "*.wav"), recursive=True):
            AudioFileName = os.path.basename(file_path)
            Emotion = os.path.split(file_path)[0].split('\\')[-1]
            # print(Emotion)
            row_values = {
                "AudioFileName": "{}".format(AudioFileName),
                "Emotion": "{}".format(Emotion),
                "DataName": "{}".format("TurEV-DB"),
                "Source": "emotional",
                }
            with open(os.path.join(outputdir, AudioFileName.replace(".wav",".json")),"w",encoding="utf8",) as save_json:
                json.dump(row_values, save_json, indent=4)

class Thorsten:
    def prepare_json(inputdir):
        data = pd.read_csv(r"C:\Users\v-zhazhai\Downloads\thorsten-emotional_v02\thorsten-emotional_v02\thorsten-emotional-metadata.csv", sep="|", encoding="utf-8", low_memory=False)
        for file_path in glob.glob(os.path.join(inputdir, "**", "*.wav"), recursive=True):
            AudioFileName = os.path.basename(file_path)
            Emotion = os.path.split(file_path)[0].split('\\')[-1]
            Trans = data.iloc[int(list(data['sid']).index(AudioFileName.replace(".wav","")))]["trans"]
            row_values = {
                "AudioFileName": "{}".format(AudioFileName),
                "Trans": "{}".format(Trans),
                "Emotion": "{}".format(Emotion),
                "DataName": "{}".format("thorsten-emotional_v02"),
                "Source": "emotional",
                }
            with open(file_path.replace(".wav",".json"),"w",encoding="utf8",) as save_json:
                json.dump(row_values, save_json, indent=4)
            with open(file_path.replace(".wav",".txt"),"w",encoding="utf8",) as save_txt:
                save_txt.writelines(Trans+'\n')

class SyntAct:
    def prepare_json(inputdir,outputdir):
        maplist = {"de1":"male","de2":"female","de3":"male","de4":"female","de6":"male","de7":"female"}
        for file_path in glob.glob(os.path.join(inputdir, "**", "*.wav"), recursive=True):
            AudioFileName = os.path.basename(file_path)            
            row_values = {
                "AudioFileName": "{}".format(AudioFileName),
                "Emotion": "{}".format(AudioFileName.split("_")[1]),
                "Gender": "{}".format(maplist[AudioFileName.split("_")[0]]),
                "DataName": "{}".format("SyntAct"),
                "Source": "emotional",
                }
            with open(os.path.join(outputdir, AudioFileName.replace(".wav",".json")),"w",encoding="utf8",) as save_json:
                json.dump(row_values, save_json, indent=4)

class RESD:
    def download(url,filename):
        # 发起请求并保存文件
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"音频已保存为 {filename}")
        else:
            print(f"下载失败，状态码: {response.status_code}")
    def prepare_json(inputdir,outputdir):
        jsonfile = r"C:\Users\v-zhazhai\Downloads\RESD.json"
        with open(jsonfile, "r",encoding='utf8') as file:
            data = json.load(file)
        for line in data["rows"]:
            wave_name = line["row"]["name"]
            speech  = line["row"]["speech"][0]["src"]
            # print(speech)
            RESD.download(speech,os.path.join(inputdir,wave_name+".wav"))
            
            row_values = {
                "AudioFileName": "{}".format(wave_name),
                "Emotion": "{}".format(line["row"]["emotion"]),
                "Trans": "{}".format(line["row"]["text"]),
                "DataName": "{}".format("RESD"),
                "Source": "emotional",
                }
            with open(os.path.join(outputdir, wave_name+".json"),"w",encoding="utf8",) as save_json:
                json.dump(row_values, save_json, indent=4)
            with open(os.path.join(outputdir,wave_name+".txt"),'w',encoding='utf8') as s:
                s.writelines(line["row"]["text"])

class SUBESCO:
    def prepare_json(inputdir,outputdir):
        Gender_map = {"M":"Male","F":"Female"}
        content=codecs.open(r"C:\Users\v-zhazhai\Downloads\SUBESCO1.txt",'rb').read()
        word = open(r"C:\Users\v-zhazhai\Downloads\SUBESCO1.txt",'r',encoding=chardet.detect(content)['encoding']).readlines()
        with open(inputdir,'r',encoding='utf8') as f:
            for line in f.readlines():
                # print(line)
                wave_name = line.replace("\n","")
                # print(wave_name.split("_")[-3])
                row_values = {
                "AudioFileName": "{}".format(wave_name),
                "Gender": "{}".format(Gender_map[wave_name.split("_")[0]]),
                "Emotion": "{}".format(wave_name.split("_")[-2]),
                "Trans": "{}".format(word[int(wave_name.split("_")[-3])-1].replace("\n","")),
                "DataName": "{}".format("SUBESCO"),
                "Source": "emotional",
                }
                with open(os.path.join(outputdir, wave_name+".json"),"w",encoding="utf8",) as save_json:
                    json.dump(row_values, save_json, indent=4)
                with open(os.path.join(outputdir,wave_name+".txt"),'w',encoding='utf8') as s:
                    s.writelines(word[int(wave_name.split("_")[-3])-1])
    
class nEMO:
     def prepare_json(inputdir,outputdir):
         data1 = pd.read_csv(inputdir, sep="\t", encoding="utf8", low_memory=False)
         index = list(range(data1.shape[0]))
         for i in index:
            row_values = {
                "AudioFileName": "{}".format(data1.iloc[i]["file_id"]),
                "Gender": "{}".format(data1.iloc[i]["gender"]),
                "Age": "{}".format(data1.iloc[i]["age"]),
                "Emotion": "{}".format(data1.iloc[i]["emotion_expressed"]),
                "Raw_text": "{}".format(data1.iloc[i]["raw_text"]),
                "Normalized_text": "{}".format(data1.iloc[i]["normalized_text"]),
                "DataName": "{}".format("nEMO"),
                "Source": "emotional",
                }
            with open(os.path.join(outputdir, data1.iloc[i]["file_id"].replace(".wav",".json")),"w",encoding="utf8",) as save_json:
                json.dump(row_values, save_json, indent=4)
            with open(os.path.join(outputdir,data1.iloc[i]["file_id"].replace(".wav",".txt")),'w',encoding='utf8') as s:
                s.writelines(data1.iloc[i]["raw_text"]+'\n')

class emozionalmente_dataset:
    def prepare_json(inputdir,outputdir):
         data1 = pd.read_csv(inputdir, sep="\t", encoding="utf8", low_memory=False)
         index = list(range(data1.shape[0]))
         for i in index:
            row_values = {
                "AudioFileName": "{}".format(data1.iloc[i]["file_name"]),
                "Gender": "{}".format(data1.iloc[i]["gender"]),
                "Age": "{}".format(data1.iloc[i]["age"]),
                "Emotion": "{}".format(data1.iloc[i]["emotion_recognized"]),
                "Trans": "{}".format(data1.iloc[i]["sentence"]),
                "audio_quality": "{}".format(data1.iloc[i]["audio_quality"]),
                "DataName": "{}".format("emozionalmente_dataset"),
                "Source": "emotional",
                }
            with open(os.path.join(outputdir, data1.iloc[i]["file_name"].replace(".wav",".json")),"w",encoding="utf8",) as save_json:
                json.dump(row_values, save_json, indent=4)
            with open(os.path.join(outputdir,data1.iloc[i]["file_name"].replace(".wav",".txt")),'w',encoding='utf8') as s:
                s.writelines(data1.iloc[i]["sentence"]+'\n')


class ASVP_ESD:
    def prepare_json(self,infofile,savefile):
        for file_path in glob.glob(os.path.join(infofile, "**", "original_fname"), recursive=True):
            # 03-01-01-01-01-116-02-02-02-05
            content=codecs.open(file_path,'rb').read()
            word = open(file_path,'r',encoding=chardet.detect(content)['encoding']).readlines()[0]
            names = os.path.basename(word)
            save_additional_info = file_path.replace("original_fname","additional_info")
            # if names.split("-")[-1] == "66.wav":
                # print(names)
            additional_info = {}
            additional_info["AudioFileName"] = names
                
            # Modality
            if names.split("-")[0] == "03":
                additional_info["Modality"] = "audio-only"
                
            # Vocal channel
            if names.split("-")[1] == "01":
                additional_info["Vocal channel"] = "speech"
            elif names.split("-")[1] == "02":
                additional_info["Vocal channel"] = "non speech"
            else:
                additional_info["Vocal channel"] = "Unknown"            
            # Gender
            if int(names.split("-")[5])%2==0:
                additional_info["Gender"] = "male"
            else:                
                additional_info["Gender"] = "female"            
            if names.split("-")[-1] == "66.wav":
                additional_info["Audio type"] = "Mixed voice"   
                with open(save_additional_info,'w',encoding='utf8') as s:
                    s.writelines(str(additional_info))
                continue
            try:
                # Style
                stylemap = {"01":"boredom","02":"neutral","03":"happy","04":"sad","05":"angry","06":"fearful","07":"disgust","08":"surprised","09":"excited","10":"pleasure","11":"pain","12":"disappointmen","13":"breath"}
                additional_info["Style"] = stylemap[names.split("-")[2]]
                
                # Emotional intensity
                Emotional_intensitymap = {"01":"normal","02":"high"}
                additional_info["Emotional intensity"] = Emotional_intensitymap[names.split("-")[3]]
                
   

                # Age
                Agemplist = {"01":"above 65", "02":"between 20~64", "03":"under 20","04":"baby"}
                try:
                    additional_info["Age"] = Agemplist[names.split("-")[6]]
                except Exception as e:
                    additional_info["Age"] = "Unknown"
            except Exception as e:
                print(word)
            with open(save_additional_info,'w',encoding='utf8') as s:
                s.writelines(str(additional_info))


class EmotionPerceptionInSchizophrenia:
    def prepare_json(self,infofile,savefile):
        for file_path in glob.glob(os.path.join(infofile, "**", "original_fname"), recursive=True):
            content=codecs.open(file_path,'rb').read()
            word = open(file_path,'r',encoding=chardet.detect(content)['encoding']).readlines()[0]
            additional_info = {}
            additional_info["AudioFileName"] = os.path.basename(word)
            stylemap = {"S_assignmentA":"angry","S_assignmentH":"happy","S_assignmentN":"neutral","S_ferryA":"angry","S_ferryH":"happy","S_ferryN":"neutral"}
            additional_info["Style"] = stylemap[os.path.basename(word).replace(".wav","")]
            with open(file_path.replace("original_fname","additional_info"),'w',encoding='utf8') as s:
                s.writelines(str(additional_info))
                
if __name__ == "__main__":
    inputdir = r"C:\Users\v-zhazhai\Downloads\emotional\chunk_c8e9f3f1875ad6389e6131e78c41097e_0.info_files"
    outputdir = r"C:\Users\v-zhazhai\Downloads\emotional\updata\chunk_a0ab6d9cb9ca94755fae4c2cc67f5a4c_2.info"
    # if not os.path.exists(outputdir):
    #     os.makedirs(outputdir, exist_ok=True)
    EmotionPerceptionInSchizophrenia().prepare_json(inputdir, outputdir)
    # Thorsten.prepare_json(inputdir)
