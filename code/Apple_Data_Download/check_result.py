"""
用于检查fasttranscription 完成的比率
"""
import os,sys
def fasttranscription_ratio(input_file, output_dir):
    Failed = []
    names = ["_".join(line.split('/')[-2:]).split(".")[0]+".json".replace('\n','') for line in open(input_file, 'r', encoding='utf-8').readlines()]
    print(names)
    n=0
    for line in os.listdir(output_dir):
        print(line)
        if line in names:
            n+=1
            names.remove(line)
    if n == 0:
        print("fasttranscription 全部未完成")
    else:
        print("fasttranscription rotio: %s" % str(n/len(names)))
        with open(os.path.join(os., "fasttranscription_ratio.txt"), 'w', encoding='utf-8') as s:
            s.writelines("fasttranscription rotio: %s" % str(n/len(names)))
if __name__ == "__main__":
    # fasttranscription_ratio(sys.argv[1], sys.argv[2])
    # fasttranscription_ratio(r"C:\Users\v-zhazhai\Downloads\1.txt", r"C:\Users\v-zhazhai\Downloads\1")
    # output_dir = r"C:\Users\v-zhazhai\Downloads\1"
    # print(os.path.split(output_dir)[0])