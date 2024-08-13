import os
"""
主要用于生成checkin所需要的 Alignment、Speech、TextScripts、XmlScripts文件夹
"""
class TTSCheckin():
    def __init__(self) -> None:
        super().__init__()
    
    names = ["Alignment","Speech","TextScripts","XmlScripts"]
    def wave_floder(inputdir,wave_list):
        for name in wave_list:
            for 
            if not os.path.exists(save_path):
                os.makedirs(save_path, exist_ok=True)

    def prepare_folder(inputdir):
        names = ["Alignment","Speech","TextScripts","XmlScripts"]
        for name in names:
            save_path = os.path.join(inputdir,name)
            if not os.path.exists(save_path):
                os.makedirs(save_path, exist_ok=True)

if __name__=="__main__":
    input_dir = r"D:\users\v-zhazhai\Tools\TTSData\ttsdata\ttsdata\zh-CN\Voices\Others\Honor\CNV"
    for name in os.listdir(input_dir):
        prepare_folder(os.path.join(input_dir,name))