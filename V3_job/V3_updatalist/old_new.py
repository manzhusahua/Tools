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
    locals = "en-us"
    lines = [
        "/datablob/realisticttsdataset_v3/train/chunks/tier1/en-us/asr/short_form_R10/chunk_7e60aa895db6088fe6367a2ca7abbab5_0.json",
        "/datablob/realisticttsdataset_v3/train/chunks/tier1/en-us/asr/short_form_R10/chunk_910443bb1e784b44dc6fb3d7d8819fb7_0.json",
        "/datablob/realisticttsdataset_v3/train/chunks/tier1/en-us/asr/short_form_R12/chunk_09c79cc5019ecfb27513f8f3c1363f4a_0.json",
        "/datablob/realisticttsdataset_v3/train/chunks/tier1/en-us/asr/short_form_R12/chunk_5522ee0305098b35914a945d21aefbf3_0.json",
        "/datablob/realisticttsdataset_v3/train/chunks/tier1/en-us/asr/short_form_R12/chunk_596e4f2b366f55acbba07bae0840698e_0.json",
        "/datablob/realisticttsdataset_v3/train/chunks/tier1/en-us/asr/short_form_R12/chunk_6bd601427caf2b717c1e9d19825cfec2_0.json",
        "/datablob/realisticttsdataset_v3/train/chunks/tier1/en-us/asr/short_form_R12/chunk_821cc76d6fda660fa4ff0852be18855b_0.json",
        "/datablob/realisticttsdataset_v3/train/chunks/tier1/en-us/asr/short_form_R12/chunk_b70d7b8dfdf7650030a3f8d8c62bfafe_0.json.tmp",
        "/datablob/realisticttsdataset_v3/train/chunks/tier1/en-us/asr/short_form_R12/chunk_f14197847d6b12fd6a6cf9b855e7367b_0.json",
        "/datablob/realisticttsdataset_v3/train/chunks/tier1/en-us/asr/short_form_R8/chunk_15341308b48968bb3c17baea4cc5dc6e_0.json",
        "/datablob/realisticttsdataset_v3/train/chunks/tier1/en-us/asr/short_form_R8/chunk_3c1670023852497063f0a563a90c0b7b_0.json",
        "/datablob/realisticttsdataset_v3/train/chunks/tier1/en-us/asr/short_form_R8/chunk_3cc38cdecbf394fb45ad80f09c7d1323_0.json",
        "/datablob/realisticttsdataset_v3/train/chunks/tier1/en-us/asr/short_form_R8/chunk_404da3a0464ac91e69fb32773ecf1351_0.json",
        "/datablob/realisticttsdataset_v3/train/chunks/tier1/en-us/asr/short_form_R8/chunk_48b26bab427c9042bef51d95497f4476_0.json.tmp",
        "/datablob/realisticttsdataset_v3/train/chunks/tier1/en-us/asr/short_form_R8/chunk_638aa50d7d80872cf89e6665b62161c1_0.json",
        "/datablob/realisticttsdataset_v3/train/chunks/tier1/en-us/asr/short_form_R8/chunk_6f2f93d12f1f3d632226bad131778786_0.json.tmp",
        "/datablob/realisticttsdataset_v3/train/chunks/tier1/en-us/asr/short_form_R8/chunk_8a351532af3594fe1270590346fc03ef_0.json",
        "/datablob/realisticttsdataset_v3/train/chunks/tier1/en-us/asr/short_form_R8/chunk_a0c09f8f6820dbd50f188d26a101d82b_0.json",
        "/datablob/realisticttsdataset_v3/train/chunks/tier1/en-us/asr/short_form_R9_01/chunk_08fdca42b3561974d2f187b4fc55348b_0.json",
        "/datablob/realisticttsdataset_v3/train/chunks/tier1/en-us/asr/short_form_R9_01/chunk_2443f5b1ee11ce860f458684ddea0b30_0.json",
        "/datablob/realisticttsdataset_v3/train/chunks/tier1/en-us/asr/short_form_R9_01/chunk_28df4fdf402dad169855cd0d5cf37089_0.json",
        "/datablob/realisticttsdataset_v3/train/chunks/tier1/en-us/asr/short_form_R9_01/chunk_bdc1a3046ed8b53b7da16ade5121c898_0.json",
        "/datablob/realisticttsdataset_v3/train/chunks/tier1/en-us/asr/short_form_R9_01/chunk_f2aecba136a6c135d18dd3b02540f617_0.json",
        "/datablob/realisticttsdataset_v3/train/chunks/tier1/en-us/asr/short_form_R9_02/chunk_0e91fd2cc561f0ae05aa46133cf716ef_0.json",
        "/datablob/realisticttsdataset_v3/train/chunks/tier1/en-us/asr/short_form_R9_02/chunk_3ade458adc600d0b50d572e9baaa4ca3_0.json",
        "/datablob/realisticttsdataset_v3/train/chunks/tier1/en-us/asr/short_form_R9_02/chunk_5792be23d07a41bd65bd73d978b45db2_0.json",
        "/datablob/realisticttsdataset_v3/train/chunks/tier1/en-us/asr/short_form_R9_02/chunk_5e4f65432a363dfb2f6a98dca87eac93_0.json",
        "/datablob/realisticttsdataset_v3/train/chunks/tier1/en-us/asr/short_form_R9_02/chunk_66ec888a87894ea106387567b3681be0_0.json",
        "/datablob/realisticttsdataset_v3/train/chunks/tier1/en-us/asr/short_form_R9_02/chunk_6b92afc02fdf80e844e7f2f0a7c227ab_0.json",
        "/datablob/realisticttsdataset_v3/train/chunks/tier1/en-us/asr/short_form_R9_02/chunk_7fc70e75b3357e18e2cd8db7da493a79_0.json",
        "/datablob/realisticttsdataset_v3/train/chunks/tier1/en-us/asr/short_form_R9_02/chunk_97419ad603917ef81f84910ff623572b_0.json",
    ]
    dataset_name = r"C:\Users\v-zhazhai\Environment\CookingSpeech\RealisticTTSDatasets\dataset\tier1\en-us\asr\all.txt"

    for line in lines:
        print(line)
        delete_all(inputdir, line, tier, locals)
        delete_tier(inputdir, line, tier, locals)
        delete_locals(inputdir, line, tier, locals)
        delete_dataset(dataset_name, line, tier, locals)
