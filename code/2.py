import os

def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            # 确保文件存在（防止符号链接等问题）
            if os.path.exists(file_path):
                total_size += os.path.getsize(file_path)
    return total_size

# 示例用法
folder_path = r"C:\Users\v-zhazhai\Downloads\podcast_list"
size_in_bytes = get_folder_size(folder_path)
size_in_mb = size_in_bytes / (1024 * 1024)  # 转换为 MB
print(f"文件夹大小: {size_in_bytes} 字节 ({size_in_mb:.2f} MB)")
