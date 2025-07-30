"""
use check FastTranscription result time
"""

import json
import os

def check_fasttranscription_result(input_file):
    sum_yime = 0
    for line in os.listdir(input_file):
        if ".json" in line:
            with open(os.path.join(input_file,line),'r',encoding='utf8') as f:
                data = json.load(f)
            sum_yime += data["fasttranscription_result"]["durationMilliseconds"]
            # print(data["fasttranscription_result"]["durationMilliseconds"])
            # for segment in data["fasttranscription_result"]["phrases"]:
            #     print(segment["offsetMilliseconds"]+)
    print("Total duration in milliseconds: %s hours" % str(round(sum_yime/3600000, 5)))

def check_fasttranscription_segment(input_file):
    """
    用于check fasttranscription 中 short segment
    """
    for line in os.listdir(input_file):
        if ".json" in line:
            with open(os.path.join(input_file,line),'r',encoding='utf8') as f:
                data = json.load(f)
        for segment in data["fasttranscription_result"]["phrases"]:
            offsetMilliseconds = segment["offsetMilliseconds"]
            durationMilliseconds = segment["durationMilliseconds"]
            text = segment["text"]
            # print(segment["offsetMilliseconds"])
            if durationMilliseconds<100:

                print(f"{line}\t{offsetMilliseconds}\t{durationMilliseconds}\t{text}")
                # print()


if __name__ == "__main__":
    input_file = r"C:\Users\v-zhazhai\Downloads\1"
    check_fasttranscription_segment(input_file)
    # fasttranscription_ratio(sys.argv[1], sys.argv[2])
    # fasttranscription_ratio(r"C:\Users\v-zhazhai\Downloads\1.txt", r"C:\Users\v-zhazhai\Downloads\1")