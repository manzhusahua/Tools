"""
用于WaveNorm 中的ERROR: Error(s) in item [0029]: Last segment [er_h] in file name.txt should be [sil].
在结尾强加0.1的sil
"""


import os
import wave

class WaveNorm():
    def __init__(self) -> None:
        super().__init__()
    
    def process_a_filelist(self, input_log, alignment_dir,wave_dir):
        logs = open(input_log,'r',encoding='utf8').readlines()
        for log in logs:
            try:
                if "should be [sil]" in log:
                    name = log.split(']')[0].replace("ERROR: Error(s) in item [",'')
                    alignment_txt = os.path.join(alignment_dir,name+'.txt')
                    f = wave.open(os.path.join(wave_dir,"Wave16k.16bit",name+'.wav'), 'rb')
                    time_count = f.getparams().nframes/f.getparams().framerate
                    times = round(sum(time_count-0.1)/3600, 5)
                    with open(alignment_txt,'a') as s:
                        s.write(f'{times} sil')
            except:
                print(log)
        
INPUT_STEP = None

def init():

    global INPUT_STEP
    INPUT_STEP = WaveNorm()

    INPUT_STEP.prs_step_init()

def run(mini_batch):

    return INPUT_STEP.prs_step_run(mini_batch)

if __name__ == "__main__":
    Wave_Norm = WaveNorm()

    input_log = r"D:\users\v-zhazhai\TTS\zh-CN\yinbiao\data\xiaochen\log\WaveNorm.log"
    alignment_dir = r"D:\users\v-zhazhai\TTS\zh-CN\yinbiao\data\xiaochen\mixligual\ForcedAlignOutput\SliceSegment"
    wave_dir = r"D:\users\v-zhazhai\TTS\zh-CN\yinbiao\data\xiaochen"
    Wave_Norm.process_a_filelist(input_log, alignment_dir,wave_dir)