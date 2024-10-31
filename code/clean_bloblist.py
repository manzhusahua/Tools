import os
import sys


# files = sys.argv[1]
def clean(files):
    # files = r"C:\Users\v-zhazhai\Desktop\en-US_short_form_fix_r8_filenames.txt"
    with open(files, "r", encoding="utf8") as f, open(
        files.replace(".txt", "_v1.txt"), "w", encoding="utf8"
    ) as s:
        chunk_ids = []
        chunk_id = []
        for line in f.readlines()[2:]:
            lines = line.split(";")[0].replace("INFO: ", "")
            # if ".info\n" in line and ".json.version_" not in line:
            if ".info" in lines:
                s.writelines(lines + "\n")

                # chunk_ids.append(line)
            # line_id = line.split(".")[0]
            # if line_id not in chunk_id :
        #     #     chunk_id.append(line_id)
        # for id in chunk_id:
        #     if len([i for i,x in enumerate(chunk_ids) if x.find(id)!=-1]) == 7:
        # s.writelines(line+'\n')


def replace(files):
    word = list(set(open(files, "r", encoding="utf8").readlines()))
    with open(files.replace(".txt", "_clean.txt"), "w", encoding="utf8") as s:
        for line in word:
            s.writelines(line)


def clean_job_list(input, output):
    with open(input, "r", encoding="utf8") as f, open(
        output, "w", encoding="utf8"
    ) as s:
        for line in f.readlines():
            if "\t" in line:
                s.writelines(line)
    os.remove(input)


if __name__ == "__main__":
    clean_job_list(
        r"C:\Users\v-zhazhai\Downloads\filenames.txt",
        r"C:\Users\v-zhazhai\Downloads\batch23_part7.txt",
    )
