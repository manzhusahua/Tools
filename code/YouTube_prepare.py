"""
txt and json files for YouTube data preparation
"""

import numpy as np
import os
import sys
from os.path import dirname, realpath, sep, pardir
import shutil
import json


class YouTubePrpare:
    def __init__(self) -> None:
        super().__init__()

    def init(self, snapshot_dir="", resource_dir_dict={}, arg_list=[]):
        self.transFileList = arg_list[arg_list.index("--transFileList") + 1]

    def process_file_list(self, input_file_list, local_output_dir):
        """
        Args:
            input_file_list (list of str): input audioList.txt file list
            local output_dir (str): local output directory path
        """
        os.makedirs(local_output_dir, exist_ok=True)
        for list_file in input_file_list:
            if not os.path.exists(list_file):
                print("Skipped %s due to file non-exist." % list_file)
                continue

            try:
                if "audioList.txt" in list_file:
                    audio_information_list = open(
                        list_file, "r", encoding="utf-8"
                    ).readlines()
                    keys = "AudioFileName	AudioTitle	AudioUrl	Duration	BitRate	SampleRate	SpeechRatio	Snr	CaptionType	CaptionFileName"
                    keys = keys.split("\t")
                    for i, audio_information in enumerate(audio_information_list):
                        if i == 0:
                            continue
                        audio_information = audio_information.strip()
                        audio_items = audio_information.split("\t")
                        if len(keys) == len(audio_items):
                            audio_dict = dict(zip(keys, audio_items))
                            audio_dict.update({"source": "Youtube"})
                            audio_filename = os.path.basename(
                                audio_dict["AudioFileName"]
                            )
                            audio_filename = os.path.splitext(audio_filename)[0]
                            audio_additional_filename = f"{audio_filename}.json"
                            audio_additional_filename_path = os.path.join(
                                local_output_dir, audio_additional_filename
                            )
                            print(audio_additional_filename_path)
                            with open(
                                audio_additional_filename_path, "w", encoding="utf-8"
                            ) as f:
                                json.dump(audio_dict, f, indent=4)

                                float(audio_items[3])

                            vtt_path = (
                                os.path.join(
                                    "/".join(list_file.split("/")[-4:-1]),
                                    audio_items[-1],
                                )
                                + "\t"
                                + "/".join(list_file.split("/")[-4:-1])
                                + "/"
                            )

                            self.output_file_list_all.append(f"{vtt_path}")
                        else:
                            print("error")

            except Exception as e:
                self.logger.info(f"Skipped {list_file} due to exception {e}\n.")
                continue


TXT_INPUT_STEP = None


def init():

    global TXT_INPUT_STEP
    TXT_INPUT_STEP = YouTubePrpare()

    TXT_INPUT_STEP.prs_step_init()


def run(mini_batch):
    return TXT_INPUT_STEP.prs_step_run(mini_batch)


# This function can contain main func so we can quickly local dev and debug this file
if __name__ == "__main__":

    dataset_path = "/mnt/c/Users/v-zhazhai/Desktop/TTS/en-US/YouTube/FY23Q2/BingYouTube/News_Politics"
    output_path = "/mnt/c/Users/v-zhazhai/Desktop/TTS/en-US/YouTube/output"

    Bilibili_Prpare = YouTubePrpare()
    Bilibili_Prpare.add_succeeded_duration_with_gen_dist = 0.0
    Bilibili_Prpare.output_file_list_all = []

    arg_list = ["--transFileList", "/mnt/c/Users/v-zhazhai/debug/"]
    Bilibili_Prpare.init(arg_list=arg_list)

    # from cookingspeech.modules.data_utils import step_stats_info

    txt_file_list = [
        "/mnt/c/Users/v-zhazhai/Desktop/TTS/en-US/YouTube/FY23Q2/BingYouTube/News_Politics/audioList.txt"
    ]
    # word = open(
    #     "/mnt/c/Users/v-zhazhai/Desktop/TTS/en-US/YouTube/FY23Q2/BingYouTube/News_Politics/audioList.txt",
    #     "r",
    #     encoding="utf8",
    # ).readlines()
    # for line in word:
    #     txt_file_list.append(os.path.join(dataset_path, line.replace("\n", "")))
    Bilibili_Prpare.process_file_list(txt_file_list, output_path)
    with open(output_path + ".txt", "w") as f:
        for output_entry in Bilibili_Prpare.output_file_list_all:
            f.write(output_entry + "\n")
    print(Bilibili_Prpare.add_succeeded_duration_with_gen_dist)
