from pydub import AudioSegment
import os
import shutil


# 读取音频文件
def sampling_rate(wav_file):
    audio = AudioSegment.from_file(wav_file)
    
    # 获取采样率
    sample_rate = audio.frame_rate
    # print(f"音频的真实采样率是: {sample_rate} Hz")
    return sample_rate

def get_rate(wave_floder):
    wave_rate = []
    for line in os.listdir(wave_floder):
        sample_rate = sampling_rate(os.path.join(wave_floder,line))
        if sample_rate not in wave_rate:
            wave_rate.append(sample_rate)
    print(f"{os.path.basename(wave_floder)} sample_rate if {str(wave_rate)}")

if __name__ == "__main__":
    wav_file = r"C:\Users\v-zhazhai\Downloads\test\1"
    get_rate(wav_file)
    shutil.rmtree(wav_file)
    os.mkdir(wav_file)