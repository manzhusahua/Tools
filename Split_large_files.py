import pandas as pd
import os


# 读取csv文件
df = pd.read_csv(r"C:\Users\v-zhazhai\Desktop\metadata_Zh-TWMale_general.csv", sep='|', encoding='utf-8')
save_path = r"C:\Users\v-zhazhai\Desktop\merged_more_books_with_small_metadata"
if not os.path.exists(save_path):
    os.makedirs(save_path, exist_ok=True)
# 获取文件总行数
row_num = len(df)
print(row_num)


# 确定每个小文件要包含的数据量
step = 2000
i=0
for start in range(0, row_num, step):
    stop = start + step
    filename = os.path.join(save_path,"metadata_{}.csv".format(str(i)))
    d = df[start: stop]
    print("Saving file : " + filename + ", data size : " + str(len(d)))
    d.to_csv(filename, sep='|', encoding='utf-8', index=None)
    i+=1


# 输出如下
# Saving file : ./small_0-500.csv, data size : 500
# Saving file : ./small_500-1000.csv, data size : 500