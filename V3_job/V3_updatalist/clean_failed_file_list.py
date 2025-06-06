import os

def clean_failed_file_list(inputdir):
    with open(inputdir, 'r', encoding='utf8') as f, open(inputdir.replace('.txt', '_clean.txt'), 'w', encoding='utf8') as s:
        for line in f.readlines():
            if "No such file or directory" not in line:
                s.writelines(line)

if __name__ == "__main__":
    clean_failed_file_list(r"C:\Users\v-zhazhai\Downloads\failed_file_list.txt")