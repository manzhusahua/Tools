import os,multiprocessing

def merger(name_count):
    names_list = []
    with open(r"C:\Users\v-zhazhai\Downloads\list_{}.txt".format(str(name_count)),'r',encoding='utf8') as s:
        for line in s.readlines():
            names_list.append(line.replace('\n',''))
    for name in names_list:
        names = name.replace("zh-CN_PodCast","zh-cn_podcast")
        word1 = 'C:/Users/v-zhazhai/Toosl/Tools/azcopy.exe copy "https://stdstoragetts01scus.blob.core.windows.net/data/experimentttsdataset_v2.1/Training/train/{}?sv=2023-01-03&st=2024-04-15T10%3A16%3A31Z&se=2024-04-22T10%3A31%3A31Z&sr=c&sp=rlt&sig=NRbUuYHiKdw%2F9Ge3gPVUidWPp4iGs%2FI6cYKwxfnbT%2Bw%3D" "https://stdstoragetts01scus.blob.core.windows.net/data/realisticttsdataset_v2.1/Training/train/{}?sv=2023-01-03&se=2024-05-15T10%3A31%3A32Z&sr=c&sp=rwlt&sig=cvMF85RudBGnYQv8SHrJXI2iJ4QvPFWIEEU1vx%2B0qHw%3D"'.format(name,names)

        print(word1)
        os.system(word1)
        



if __name__ == "__main__":

    # path1 = multiprocessing.Process(target=merger,args=("1"))
    # path1.start()

    # path2 = multiprocessing.Process(target=merger,args=("2"))
    # path2.start()

    # path3 = multiprocessing.Process(target=merger,args=("3"))
    # path3.start()

    # path4 = multiprocessing.Process(target=merger,args=("4"))
    # path4.start()

    path5 = multiprocessing.Process(target=merger,args=("5"))
    path5.start()