
import numpy as np
import os
import soundfile as sf
from tqdm import tqdm
import shutil
import tarfile


def un_tar(file_name):
    shutil.copyfile(file_name,file_name+'.tar')
    # os.renames(file_name,file_name+'.tar')
    tar = tarfile.open(file_name)
    names = tar.getnames()
    if os.path.isdir(file_name + "_files"):
        pass
    else:
        os.mkdir(file_name + "_files")
    # 由于解压后是许多文件，预先建立同名文件夹
    for name in names:
        tar.extract(name, file_name + "_files/")
    tar.close()
    # os.remove(file_name)
    os.remove(file_name+'.tar')
    return file_name+"_files"

def zip_tar(fine_segment_dir,fine_segment_name):
    if os.path.exists(fine_segment_name):
        os.remove(fine_segment_name)
    os.chdir(fine_segment_dir)
    count = ' '.join(str(n) for n in range(0,len(os.listdir(fine_segment_dir))))
    # with open(r"C:\Users\v-zhazhai\Desktop\1.sh",'w',encoding='utf8') as s:
    #     s.writelines(f"tar -cvf {fine_segment_name} {count}")
    os.system(f"tar -cvf {fine_segment_name} {count}")
    for line in os.listdir(fine_segment_dir):
        os.remove(os.path.join(fine_segment_dir,line))

def rms_energy(wav):
    return np.sqrt(np.mean(np.square(wav), axis=0))

def normalize_wavs(ref_folder, target_folder, out_folder):
    os.makedirs(out_folder, exist_ok=True)

    # 计算参考文件夹所有wav的平均RMS能量
    ref_energies = []
    for fn in os.listdir(ref_folder):
        if fn.lower().endswith(".wav"):
            wav_path = os.path.join(ref_folder, fn)
            data, sr = sf.read(wav_path)
            ref_energies.append(rms_energy(data))
    if len(ref_energies) == 0:
        raise RuntimeError("参考文件夹中没有wav文件")
    ref_avg_energy = np.mean(ref_energies)

    print(f"参考文件夹平均RMS能量: {ref_avg_energy:.6f}")

    # 对待归一化文件做归一化处理
    for fn in tqdm(os.listdir(target_folder)):
        if fn.lower().endswith(".wav"):
            wav_path = os.path.join(target_folder, fn)
            data, sr = sf.read(wav_path)

            current_energy = rms_energy(data)
            if current_energy == 0:
                print(f"警告：{fn}能量为0，跳过")
                continue

            gain = ref_avg_energy / current_energy
            normalized_data = data * gain

            # 防止 clipping，简单裁剪到 [-1, 1]
            max_amp = np.max(np.abs(normalized_data))
            if max_amp > 1:
                normalized_data = normalized_data / max_amp

            out_path = os.path.join(out_folder, fn)
            sf.write(out_path, normalized_data, sr)

    print("归一化完成")

def run_chunk(chunk_path,save_path,ref_folder):
    chunk_name = os.path.basename(chunk_path)
    save_chunk_path = os.path.join(save_path,chunk_name)
    temp_path = os.path.join(save_path,"temp")
    
    os.makedirs(save_path, exist_ok=True)
    os.makedirs(temp_path, exist_ok=True)
    
    un_tar_path = un_tar(chunk_path)
    for line in os.listdir(un_tar_path):
        os.renames(os.path.join(un_tar_path,line),os.path.join(un_tar_path,line+".wav"))
    normalize_wavs(ref_folder, un_tar_path, temp_path)
    
    for line in os.listdir(temp_path):
        os.renames(os.path.join(temp_path,line),os.path.join(temp_path,line.replace(".wav","")))
    zip_tar(temp_path,save_chunk_path)
    shutil.rmtree(un_tar_path)
    
if __name__ == "__main__":

    # ref_dir = r"C:\Users\v-zhazhai\Desktop\wavenorm_xiaoshuang\ref_xiaoshuang"
    # chunk_path = r"C:\Users\v-zhazhai\Downloads\ZhCNJinghan\Story"
    chunk_path = r"C:\Users\v-zhazhai\Downloads\ZhCNFT005"
    save_path = r"C:\Users\v-zhazhai\Downloads\ZhCNFT005_updata1"
    ref_folder = r"C:\Users\v-zhazhai\Desktop\wavenorm_xiaoshuang\ref_xiaoshuang"
    for line in os.listdir(chunk_path):
        run_chunk(os.path.join(chunk_path,line),save_path,ref_folder)
    # run_chunk(chunk_path,save_path,ref_folder)
    