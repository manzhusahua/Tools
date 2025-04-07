import os
import json
import pandas as pd
import codecs
import chardet
import shutil
import re


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



if __name__ == "__main__":
    inputdir = r"C:\Users\v-zhazhai\Desktop\data_aishell3\content.txt"
    outputdir = r"C:\Users\v-zhazhai\Desktop\data_aishell3\train"
    if not os.path.exists(outputdir):
        os.makedirs(outputdir, exist_ok=True)
    AISHELL_3.prepare_json(inputdir, outputdir)
