"""
dele line in fileslist
"""

import os
import multiprocessing


def delete_all(inputdir, line, tier, locals):
    with open(os.path.join(inputdir, "all.txt"), "r", encoding="utf8") as f, open(
        os.path.join(inputdir, "all_1.txt"), "w", encoding="utf8"
    ) as s:
        for word in f.readlines():
            if line not in word:
                s.writelines(word)
    os.remove(os.path.join(inputdir, "all.txt"))
    os.renames(os.path.join(inputdir, "all_1.txt"), os.path.join(inputdir, "all.txt"))


def delete_tier(inputdir, line, tier, locals):
    with open(os.path.join(inputdir, tier, "all.txt"), "r", encoding="utf8") as f, open(
        os.path.join(inputdir, tier, "all_1.txt"), "w", encoding="utf8"
    ) as s:
        for word in f.readlines():
            if line not in word:
                s.writelines(word)
    os.remove(os.path.join(inputdir, tier, "all.txt"))
    os.renames(
        os.path.join(inputdir, tier, "all_1.txt"),
        os.path.join(inputdir, tier, "all.txt"),
    )


def delete_locals(inputdir, line, tier, locals):
    with open(
        os.path.join(inputdir, tier, locals, "all.txt"), "r", encoding="utf8"
    ) as f, open(
        os.path.join(inputdir, tier, locals, "all_1.txt"), "w", encoding="utf8"
    ) as s:
        for word in f.readlines():
            if line not in word:
                s.writelines(word)
    os.remove(os.path.join(inputdir, tier, locals, "all.txt"))
    os.renames(
        os.path.join(inputdir, tier, locals, "all_1.txt"),
        os.path.join(inputdir, tier, locals, "all.txt"),
    )


def delete_dataset(dataset_name, line, tier, locals):
    with open(
        dataset_name,
        "r",
        encoding="utf8",
    ) as f, open(
        dataset_name.replace(".txt", "_v1.txt"),
        "w",
        encoding="utf8",
    ) as s:
        for word in f.readlines():
            if line not in word:
                s.writelines(word)
    os.remove(dataset_name)
    os.renames(
        dataset_name.replace(".txt", "_v1.txt"),
        dataset_name,
    )


if __name__ == "__main__":

    inputdir = (
        r"C:\Users\v-zhazhai\Environment\CookingSpeech\RealisticTTSDatasets\dataset"
    )

    tier = "tier1"
    locals = "zh-cn"
    lines = [
        "/datablob/realisticttsdataset_v3/train/chunks/tier1/zh-cn/asr/Traindata140k_CTFMalign_Gen202307_01/chunk_c3e03617ee50d2d8c49d23acbe7c7560_0.json.tmp",
        "/datablob/realisticttsdataset_v3/train/chunks/tier1/zh-cn/asr/Traindata140k_CTFMalign_Gen202307_01/chunk_d46ec4a8e204f2743b3b75bd11d476d9_0.json",
        "/datablob/realisticttsdataset_v3/train/chunks/tier1/zh-cn/asr/Traindata140k_CTFMalign_Gen202307_01/chunk_d750442b1ac8fc9802ac7673a891d0a7_0.json",
    ]
    dataset_name = (
        r"C:\Users\v-zhazhai\Downloads\2024082701_clean\tier1\zh-cn\asr\all.txt"
    )

    for line in lines:
        print(line)
        delete_all(inputdir, line, tier, locals)
        delete_tier(inputdir, line, tier, locals)
        delete_locals(inputdir, line, tier, locals)
        delete_dataset(dataset_name, line, tier, locals)
