import os

"""
用于文件内容去重
"""


def FilesWeightRemoval(inputfile):
    word = []
    with open(inputfile, "r", encoding="utf8") as f, open(
        inputfile.replace(".txt", "_v1.txt"), "w", encoding="utf8"
    ) as s:
        for line in f.readlines():
            if line not in word:
                s.writelines(line)
                word.append(line)
    os.remove(inputfile)
    os.renames(inputfile.replace(".txt", "_v1.txt"), inputfile)


if __name__ == "__main__":
    FilesWeightRemoval(r"C:\Users\v-zhazhai\Downloads\filenames.txt")
