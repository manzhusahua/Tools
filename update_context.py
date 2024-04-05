import pandas as pd
import argparse
import os
import csv, json
import pandas as pandasForSortingCSV
import shutil

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_metadata', default=None)
    args, _ = parser.parse_known_args()
    return args


def extract_all_sid(metadata_path):
    """
    Extract all sid from metadata and return dict, which key is sid prefix and value is sorted sid list
    Args:
        metadata_path: metadata path
    """
    metadata = pd.read_csv(metadata_path, dtype=str, sep='|', quoting=3)
    all_sid_dict = {}
    for sid in metadata["sid"]:
        sid_prefix = sid.strip().rsplit("_", 1)[0]
        if sid_prefix not in all_sid_dict.keys():
            all_sid_dict[sid_prefix] = [sid]
        else:
            all_sid_dict[sid_prefix].append(sid)
    for sid_prefix, sid_list in all_sid_dict.items():
        sid_list.sort(key=lambda x: int(x.strip().rsplit("_", 1)[-1]))
    return all_sid_dict


def has_context(sid, all_sid_dict):
    """
    Check whether the sid has left or right context
    Args:
        sid: sentence id
        all_sid_dict: all sid dict, key is sid prefix, value is sorted sid list
    """
    has_left_context = False
    has_right_context = False
    # if sid is the first part of the sentence, find previous sentence to confirm whether has left context
    # if sid isn't the first part of the sentence, find previous part of the sentence to confirm whether has left context
    if sid.strip().rsplit("_", 1)[-1] == "0":
        if sid.strip().rsplit("_", 2)[-2][5:] == "00000":
            has_left_context = False
        else:
            try:
                sid_split = sid.strip().rsplit("_", 2)
                if len(sid_split) > 2:
                    left_context_sidprefix = "%s_%010d" % (sid_split[0], int(sid_split[-2]) - 1)
                else:
                    left_context_sidprefix = "%010d" % (int(sid_split[-2]) - 1)

                if left_context_sidprefix in all_sid_dict.keys():
                    has_left_context = True
            except Exception as e:
                print("warning (left context 0): non-numeric sentence number %s" % sid)
                has_left_context = False

    # TODO: align final sid format
    elif len(sid.strip().rsplit("_", 1)[-1]) < 10:
        try:
            left_context_sid = "%s_%d" % (sid.strip().rsplit("_", 1)[0], int(sid.strip().rsplit("_", 1)[-1]) - 1)
            if left_context_sid in all_sid_dict[sid.strip().rsplit("_", 1)[0]]:
                has_left_context = True
        except Exception as e:
            print("warning (left context 1): non-numeric sentence number %s" % sid)
            has_left_context = False
    else:
        raise Exception("sid format error: {}".format(sid))

    # if there is the next part of the current sid, then it has the right context
    # if sid is the last part of the sentence, find the first part of next sentence to confirm whether has right context
    # TODO: align final sid format
    if len(str(int(sid.strip().rsplit("_", 1)[-1]) + 1)) < 10:
        try:
            right_context_sid = "%s_%d" % (sid.strip().rsplit("_", 1)[0], int(sid.strip().rsplit("_", 1)[-1]) + 1)
            if right_context_sid in all_sid_dict[sid.strip().rsplit("_", 1)[0]]:
                has_right_context = True
        except Exception as e:
            print("warning (right context 0): non-numeric sentence number %s" % sid)
            has_right_context = False
    else:
        has_right_context = False
    if not has_right_context and sid == all_sid_dict[sid.strip().rsplit("_", 1)[0]][-1]:
        if sid.strip().rsplit("_", 2)[-2][5:] == "99999":
            has_right_context = False
        else:
            sid_split = sid.strip().rsplit('_', 2)
            try:
                if len(sid_split) > 2:
                    right_context_sidprefix = "%s_%010d" % (sid_split[0], int(sid_split[-2]) + 1)
                    right_context_sid = "%s_0" % right_context_sidprefix
                else:
                    right_context_sidprefix = "%10d" % (int(sid_split[0]) + 1)
                    right_context_sid = "%s_0" % right_context_sidprefix

                if right_context_sidprefix in all_sid_dict.keys() and right_context_sid in all_sid_dict[
                    right_context_sidprefix]:
                    has_right_context = True
                else:
                    has_right_context = False

            except Exception as e:
                print("warning (right context 1): non-numeric sentence number %s" % sid)
                has_right_context = False

    return has_left_context, has_right_context

def main(input_metadata):
    # duration_total=0
    # csvData2 = pandasForSortingCSV.read_csv(args.input_metadata,sep='|')
    # for index, row in csvData2.iterrows():
    #     duration_total = duration_total + row['speech_length_in_s']
    #
    # duration_total = round(duration_total/3600, 2)
    # print("duration2: " + str(duration_total))

    files=os.listdir(input_metadata)
    for file in files:
        rangeid = file.split('_')[1]
        input_metadata_file=os.path.join(input_metadata,file)
        output_metadata_file=os.path.join(input_metadata,file.replace('_v1', '_v2'))
        all_sid_set = extract_all_sid(input_metadata_file)
        print("update context: " + file)
        print(input_metadata_file)
        data = pd.read_csv(input_metadata_file, sep='|', encoding='utf-8', quoting=csv.QUOTE_NONE)
        index = list(range(data.shape[0]))
        for i in index:
            line = data.iloc[i]
            sid = line['sid']
            has_left_context, has_right_context = has_context(sid, all_sid_set)
            data.loc[i, 'has_left_context'] = 1 if has_left_context else 0
            data.loc[i, 'has_right_context'] = 1 if has_right_context else 0
        data.to_csv(output_metadata_file, sep='|', encoding='utf-8', index=False, quoting=csv.QUOTE_NONE)
        registry_folder_path = os.path.join(input_metadata, rangeid)
        if not os.path.exists(registry_folder_path):
            os.makedirs(registry_folder_path)
        registry_file = os.path.join(registry_folder_path, "registry.csv")
        registrywriter = open(registry_file,'a', encoding='utf-8')
        registrywriter.write('speaker|locale|style|metadata_path\n')
        registrywriter.write(r'YoutubeSpeakers|en-us|general|../' + file.replace('_v1', '_v2') + '\n')


if __name__ == "__main__":
#    args = get_arguments()
    arg_list = ["--input_metadata", r"C:\Users\v-zhazhai\Desktop\en-US\Human_Caption\merged_more_books_with_small_metadata_finall"]
#    main(args)
    main(r"C:\Users\v-zhazhai\Desktop\en-US\Human_Caption\merged_more_books_with_small_metadata_finall")

