import os

def mkdir_floder(inputdir,fodername):
    save_path = os.path.join(inputdir,fodername,"PlainText")
    if not os.path.exists(save_path):
        os.makedirs(save_path, exist_ok=True)
    with open(os.path.join(save_path,fodername+'.txt'),'w',encoding='utf8') as s:
        s.writelines('\n')

def prepare_wav(inputdir,local):
    print("run {} add ssml file".format(local))
    add_ssml_path = os.path.join(inputdir,local,"1_add_ssml.py")
    # print(add_ssml_path)
    with open(r"D:\users\voices\1_add_ssml.py",'r',encoding='utf8') as f,open(add_ssml_path,'w',encoding='utf8') as s:
        for line in f.readlines():
            if "INPUT_Locale" in line:
                line = line.replace("INPUT_Locale","{}".format(local))
            s.writelines(line)
    os.system('C:/Users/v-zhazhai/.conda/envs/test/python.exe {}'.format(add_ssml_path))

    

if __name__ == "__main__":
    
    inputdir = r"D:\users\voices"
    locals_list = ["kk-KZ","km-KH","kn-IN","ko-KR","lo-LA","lt-LT","lv-LV","mk-MK","ml-IN","mn-MN","ms-MY","mt-MT","my-MM","nb-NO"]
    for name in locals_list:

        prepare_wav(inputdir,name)