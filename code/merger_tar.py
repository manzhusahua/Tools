import os,multiprocessing

def merger(start,end):
    n=start
    end = end
    while n<=(end):
        word1 = "C:/zhaizhaohui/Tools/Code/azcopy.exe copy \"https://zettaprod01scus.blob.core.windows.net/data/users/v-zhazhai/Language/zh-CN/SR_Chunk/output/Traindata140k_CTFMalign_Gen202307/output_binary_re/part2/"
        word2 = "/train/*?sv=2021-10-04&se=2024-03-13T07%3A20%3A52Z&sr=c&sp=rlt&sig=T8Te23GCLnkZfstPL4oePmMIhh18G3vr1BN%2B4S50QMw%3D\" \"https://zettaprod01scus.blob.core.windows.net/data/users/v-zhazhai/Language/zh-CN/SR_Chunk/output/Traindata140k_CTFMalign_Gen202307/output_binary_merger/?sv=2021-10-04&se=2024-03-13T07%3A20%3A52Z&sr=c&sp=rwlt&sig=qRJYDm1rHQvNq14tfn3UVtBqdwGlQSVoYRRDDT2ND%2Bo%3D\" --overwrite=false"
        counts = str(n).zfill(5)
        print(counts)
        print(word1+counts+word2)
        os.system(word1+counts+word2)
        n+=1


if __name__ == "__main__":
    count = int(156/5)
    path1 = multiprocessing.Process(target=merger,args=(count*0,count*1))
    path1.start()

    path2 = multiprocessing.Process(target=merger,args=(count*1,count*2))
    path2.start()

    path3 = multiprocessing.Process(target=merger,args=(count*2,count*3))
    path3.start()

    path4 = multiprocessing.Process(target=merger,args=(count*3,count*4))
    path4.start()

    path5 = multiprocessing.Process(target=merger,args=(count*4,count*5))
    path5.start()