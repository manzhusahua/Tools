import numpy as np
import glob
import os

# 定义计算平均绝对误差的函数
def mean_absolute_error(y_true, y_pred):
    """
    计算平均绝对误差（Mean Absolute Error，MAE）

    参数：
    y_true: 真实值，array-like
    y_pred: 预测值，array-like

    返回：
    mae: 平均绝对误差
    """
    # 将输入转换为numpy数组
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    # 计算每个样本的预测误差
    absolute_errors = np.abs(y_pred - y_true)
    print(absolute_errors)

    # 计算平均绝对误差
    mae = np.mean(absolute_errors)
    
    return mae

def chunk_abs_error_calculation(chunkfile1,chunkfile2):
    chunkfile1_ms_scores = []
    chunkfile2_ms_scores = []
    
    input_file1_list = glob.glob(os.path.join(chunkfile1, "**", "ms_score"), recursive=True)
    input_file2_list = glob.glob(os.path.join(chunkfile2, "**", "ms_score"), recursive=True)
    
    for files in input_file1_list:
        chunkfile1_ms_scores.append(np.fromfile(r"C:\Users\v-zhazhai\Downloads\ms_score1")[0])
    for files in input_file2_list:
        chunkfile2_ms_scores.append(np.fromfile(r"C:\Users\v-zhazhai\Downloads\ms_score1")[0])
    
    return chunkfile1_ms_scores,chunkfile2_ms_scores

def run(chunkfile1,chunkfile2):
    chunkfile1_ms_scores,chunkfile2_ms_scores = chunk_abs_error_calculation(chunkfile1,chunkfile2)
    mean_absolute_error(chunkfile1_ms_scores, chunkfile2_ms_scores)


chunkfile1 = r"C:\Users\v-zhazhai\Downloads\chunk_0a03ac1fabe00a07ceca9991bf54abe9_0_V1.fine_segment"
chunkfile2 = r"C:\Users\v-zhazhai\Downloads\chunk_0a03ac1fabe00a07ceca9991bf54abe9_0_V2.fine_segment"
mae = run(chunkfile1,chunkfile2)
print("平均绝对误差（MAE）:", mae)