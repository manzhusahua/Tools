import os, sys, json
import shutil
import pandas as pd


"""
use zh-CN bilibili data prepare json files and statistical data
"""


class PREPAREFILES:
    def __init__(self) -> None:
        super().__init__()

    def dump_json(self, inputdir, outputdir):
        Durations = 0.0

        for filename in os.listdir(inputdir):
            with open(os.path.join(inputdir, filename), "r", encoding="utf8") as f:
                for line in f.readlines()[1:]:
                    line = line.replace("\n", "")
                    json_name = line.split("\t")[0].replace(".wav", ".json")
                    row_values = {
                        "AudioFileName": "{}".format(line.split("\t")[0]),
                        "Transcription": "{}".format(line.split("\t")[1]),
                        "Recognition": "{}".format(line.split("\t")[2]),
                        "Wer": "{}".format(line.split("\t")[3]),
                        "Duration": "{}".format(line.split("\t")[-1]),
                        "source": "bilibili",
                    }

                    if len(line.split("\t")[2]) != 0:

                        # write json files
                        with open(
                            os.path.join(outputdir, json_name), "w", encoding="utf8"
                        ) as save_json:
                            json.dump(row_values, save_json, indent=4)

                        # write trans files
                        with open(
                            os.path.join(outputdir, json_name.replace(".json", ".txt")),
                            "w",
                            encoding="utf8",
                        ) as save_txt:
                            save_txt.writelines(line.split("\t")[2] + "\n")

                    Durations += float(line.split("\t")[-1])
        print("{} Durations :".format(os.path.basename(inputdir)), Durations)


TXT_INPUT_STEP = None


def init():

    global TXT_INPUT_STEP
    TXT_INPUT_STEP = PREPAREFILES()

    TXT_INPUT_STEP.prs_step_init()


def run(mini_batch):

    return TXT_INPUT_STEP.prs_step_run(mini_batch)


if __name__ == "__main__":

    PrepareFiles = PREPAREFILES()

    dataset_path = r"C:\Users\v-zhazhai\Desktop\zh-CN_Bilii\zh-CN\FY23Q4\AcFun"
    output_path = r"C:\Users\v-zhazhai\Desktop\zh-CN_Bilii\zh-CN\FY23Q4\prepare\AcFun"

    for name in os.listdir(dataset_path):
        if not os.path.exists(os.path.join(output_path, name)):
            os.system("mkdir {}".format(os.path.join(output_path, name)))

        PrepareFiles.dump_json(
            os.path.join(dataset_path, name), os.path.join(output_path, name)
        )
