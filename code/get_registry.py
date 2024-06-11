import os

# speaker|locale|style|metadata_path
# YoutubeSpeakers|zh-cn|general|../metadata_00000_v1.csv

def not_fold(speaker,suncoumt,save_path,locale,general):
        n=0
        if not os.path.exists(save_path):
                os.makedirs(save_path, exist_ok=True)
        if type(suncoumt) == int:
                while n<=suncoumt:
                        os.mkdir(os.path.join(save_path,str(n).zfill(5)))
                        with open(os.path.join(save_path,str(n).zfill(5),"registry.csv"),'w',encoding='utf8') as f:
                                f.writelines("speaker|locale|style|metadata_path"+"\n")
                                f.writelines(speaker+"|"+locale+"|"+general+"|../metadata_"+str(n)+".csv\n")
                        n+=1
        else:
                os.mkdir(os.path.join(save_path,suncoumt))
                with open(os.path.join(save_path,suncoumt,"registry.csv"),'w',encoding='utf8') as f:
                        f.writelines("speaker|locale|style|metadata_path"+"\n")
                        f.writelines(speaker+"|"+locale+"|"+general+"|../metadata_"+str(n)+".csv\n")
                         
def has_folder(speaker,metadatafloder):
        m=0
        for name in os.listdir(metadatafloder):
                os.mkdir(os.path.join(metadatafloder,str(m).zfill(5)))
                with open(os.path.join(metadatafloder,str(m).zfill(5),"registry.csv"),'w',encoding='utf8') as f:
                        f.writelines("speaker|locale|style|metadata_path"+"\n")
                        f.writelines("%s|en-us|general|../%s\n" % (speaker,name))
                m+=1

if __name__ == "__main__":
        # has_folder("EnUSLibri-RTTS",r"C:\Users\v-zhazhai\Desktop\merged_more_books_with_small_metadata_updata_sid_context_speaker2")
        speaker = "general"
        suncoumt = 16
        save_path = r"C:\Users\v-zhazhai\Downloads\749_finall_updata_context"
        locale = "zh-cn"
        general = "ZhCNYunYe"
        not_fold(speaker,suncoumt,save_path,locale,general)
