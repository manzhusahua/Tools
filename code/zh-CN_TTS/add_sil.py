import os
import wave

"""
用于在alignment最后添加sil
"""

def add_sil(alignmentfile,wavefile):
    # print(time_count)
    # print(format(round(float(time_count)-0.005, 5), '.5f'))
    if os.path.exists(alignmentfile):
        f = wave.open(wavefile, 'rb')
        time_count = f.getparams().nframes/f.getparams().framerate
        with open(alignmentfile,'a',encoding='utf8') as f:
            start_times = str(format(round(float(time_count)-0.005, 5), '.5f'))
            f.writelines(f"{start_times} sil\n")


if __name__=="__main__":

    wave_path = r"D:\users\v-zhazhai\TTS\M564-01\Wave16k.16bit\0010001033-0010001277"
    aignment_path = r"D:\users\v-zhazhai\TTS\M564-01\mixligual\ForcedAlignOutput\SliceSegment\0010001033-0010001277"
    names = ["0010001034","0010001043","0010001045","0010001068","0010001081","0010001100","0010001127","0010001151","0010001152","0010001153","0010001154","0010001155","0010001163","0010001164","0010001165","0010001172","0010001173","0010001175","0010001181","0010001184","0010001187","0010001192","0010001197","0010001207","0010001226","0010001229","0010001240","0010001249","0010001253"]
    for name in names:
        add_sil(os.path.join(aignment_path,name+".txt"),os.path.join(wave_path,name+".wav"))