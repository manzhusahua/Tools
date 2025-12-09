import os

def get_file(dataset,filelist_durations_path):
    get_filelist_duration = fr'C:/Users/v-zhazhai/Toosl/code/Tool/merger_tar/azcopy.exe copy "https://stdstoragetts01scus.blob.core.windows.net/data/realisticttsdataset_v3/train/statistics/{dataset}/{filelist_durations_path}?sv=2025-07-05&st=2025-12-03T08%3A27%3A50Z&se=2025-12-10T08%3A42%3A50Z&skoid=c52a83f4-cefb-4d0c-a81d-a2747c46fd59&sktid=72f988bf-86f1-41af-91ab-2d7cd011db47&skt=2025-12-03T08%3A27%3A50Z&ske=2025-12-10T08%3A42%3A50Z&sks=b&skv=2025-07-05&sr=c&sp=rl&sig=wud%2Fl45o%2B%2B0VtJJKCj865pq1TqAH46iAM8uR637F5Ww%3D" "C:\Users\v-zhazhai\Toosl\Tools\code\statistic\filelist_duration.txt" --overwrite=true --check-md5 FailIfDifferent --from-to=BlobLocal --blob-type BlockBlob --recursive --log-level=INFO'
    os.system(get_filelist_duration)
    get_data_summary = fr'C:/Users/v-zhazhai/Toosl/code/Tool/merger_tar/azcopy.exe copy "https://stdstoragetts01scus.blob.core.windows.net/data/realisticttsdataset_v3/train/statistics/{dataset}/{filelist_durations_path}?sv=2025-07-05&st=2025-12-03T08%3A27%3A50Z&se=2025-12-10T08%3A42%3A50Z&skoid=c52a83f4-cefb-4d0c-a81d-a2747c46fd59&sktid=72f988bf-86f1-41af-91ab-2d7cd011db47&skt=2025-12-03T08%3A27%3A50Z&ske=2025-12-10T08%3A42%3A50Z&sks=b&skv=2025-07-05&sr=c&sp=rl&sig=wud%2Fl45o%2B%2B0VtJJKCj865pq1TqAH46iAM8uR637F5Ww%3D" "C:\Users\v-zhazhai\Toosl\Tools\code\statistic\data_summary.txt" --overwrite=true --check-md5 FailIfDifferent --from-to=BlobLocal --blob-type BlockBlob --recursive --log-level=INFO'
    os.system(get_data_summary)

def filelist_duration(dataset,filelist_durations_path):
    get_file(dataset,filelist_durations_path)
    total_duration = 0.0
    valid_duration = 0.0
    words = [x.replace('\n','') for x in open(r"C:\Users\v-zhazhai\Toosl\Tools\code\statistic\data_summary.txt",'r',encoding="utf8").readlines()]
    if "valid durations:0.00 hours" not in words:   
        with open(r"C:\Users\v-zhazhai\Toosl\Tools\code\statistic\filelist_duration.txt",'r',encoding="utf8") as f:
            for line in f.readlines()[1:]:
                total_duration+=float(line.split("\t")[1])
                valid_duration+=float(line.split("\t")[2])
    else:
        total_duration = float([x for i,x in enumerate(words) if x.find("total durations") != -1][0].replace("total durations:","").replace(" hours",""))*3600
        valid_duration = total_duration

    valid_ratio = valid_duration/total_duration
    return str(round(total_duration/3600, 2)),str(round(valid_duration/3600, 2)),"{:.2%}".format(valid_ratio)
            
def data_summary(dataset):
    get_list = []
    get_list_word = fr'C:/Users/v-zhazhai/Toosl/code/Tool/merger_tar/azcopy.exe list "https://stdstoragetts01scus.blob.core.windows.net/data/realisticttsdataset_v3/train/statistics/{dataset}/?sv=2025-07-05&spr=https%2Chttp&st=2025-12-03T08%3A34%3A18Z&se=2025-12-04T08%3A34%3A18Z&skoid=c52a83f4-cefb-4d0c-a81d-a2747c46fd59&sktid=72f988bf-86f1-41af-91ab-2d7cd011db47&skt=2025-12-03T08%3A34%3A18Z&ske=2025-12-04T08%3A34%3A18Z&sks=b&skv=2025-07-05&sr=c&sp=racwdxltf&sig=hWHA%2FKEfblmFL5W36dKC70TXKfbNIFIVcvC0ZFCBSdY%3D" > "C:\Users\v-zhazhai\Toosl\Tools\code\statistic\get_summary.txt"'
    print(get_list_word)
    os.system(get_list_word)
    with open(r"C:\Users\v-zhazhai\Toosl\Tools\code\statistic\get_summary.txt",'r',encoding='utf8') as f:
        for line in f.readlines():
            if "statistics/merged_statistics_result/filelist_duration.txt" in line:
                get_list.append(line.split(";")[0].replace("INFO: ",'').replace("/statistics/merged_statistics_result/filelist_duration.txt",""))
    for line in get_list:
        total_duration,valid_duration,valid_ratio = filelist_duration(dataset,line)
        print(f"{dataset}_{line.replace('/statistics/merged_statistics_result/filelist_duration.txt','')}\t{total_duration}\t{valid_duration}\t{valid_ratio}")

if __name__ == "__main__":
    data_summary("tier1/en-us/mls")