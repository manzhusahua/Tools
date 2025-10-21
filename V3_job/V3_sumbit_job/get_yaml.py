import os


class GETYAML():
    def __init__(self) -> None:
        super().__init__()
    
    def get_youtbue_yaml(self,basefile,batch,domain,savefile):
        with open(basefile,'r',encoding='utf8') as f,open(savefile,'w',encoding='utf8') as s:
            for line in f.readlines():
                if "batch02" in line:
                    line = line.replace("batch02",batch)
                elif "v18: &metadata " in line:
                    line = line.replace("affectionate",domain)
                s.writelines(line)

if __name__ == "__main__":
    basefile = r"C:\Users\v-zhazhai\OneDrive - Microsoft\yaml\others\shaofei\honor\emotions_filter\HonorEmotionvctest_filter\affectionate_try1.yaml"
    savedir = r"C:\Users\v-zhazhai\OneDrive - Microsoft\yaml\others\shaofei\honor\emotions_filter\HonorEmotionvctest_filter"
    maplist = ['angry  angry_xiaoxiao_f207_trim', 'anxiety  anxiety', 'cheerful  cheerful', 'curious  curious', 'disappointment  disappointment', 'empathetic  empathetic_xiaoxiao', 'encouraging  encouraging', 'excited  excited_xiaoxiao_trim', 'fearful  fearful_xiaoxiao', 'gulity  gulity', 'loneliness  loneliness', 'sad  sad_xiaoxiao_f207_trim', 'surprised  surprised', 'tired  tired']
    for map in maplist:
        # print(map)
        batch = map.split("  ")[-1]
        domain = map.split("  ")[0]
        savefile = os.path.join(savedir,"_".join([batch,"try1"])+".yaml")
        print(savefile)
        GETYAML().get_youtbue_yaml(basefile,batch,domain,savefile)          