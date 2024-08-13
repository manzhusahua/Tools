import os

"""
主要用于生成checkin所需要的 Alignment、Speech、TextScripts、XmlScripts文件夹
"""


class TTSCheckin:
    def __init__(self) -> None:
        super().__init__()

    names = ["Alignment", "Speech", "TextScripts", "XmlScripts"]

    def wave_floder(self, inputdir, wave_list):
        for wave_name in wave_list:
            for name in self.names:
                save_path = os.path.join(inputdir, wave_name, name)
                if not os.path.exists(save_path):
                    os.makedirs(save_path, exist_ok=True)

    def prepare_folder(self, inputdir):
        for name in self.names:
            save_path = os.path.join(inputdir, name)
            if not os.path.exists(save_path):
                os.makedirs(save_path, exist_ok=True)


if __name__ == "__main__":
    input_dir = r"D:\users\v-zhazhai\Tools\TTSData\ttsdata\ttsdata\zh-CN\Voices\Others\Honor\CNV"
    for name in os.listdir(input_dir):
        prepare_folder(os.path.join(input_dir, name))
