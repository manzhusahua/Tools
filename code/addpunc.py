import os
from addpunc.auto_addpunc_for_transcription import auto_addpunc_for_transcription

def addpunc(text_file,user_temp_dir):
    chunk_temp_addpunc_dir = os.path.join(user_temp_dir, "add_punc_temp")
    os.makedirs(chunk_temp_addpunc_dir, exist_ok=True)
    for line in open(text_file,'r',encoding='utf8').readlines():
        try:
            text_removed_punc = line.split('\t')[-1]
            with open(text_file.replace('.txt','_punc.txt'),'a',encoding='utf8') as s:
                
                step_resource_addpunc_model_dir = "/mnt/c/Users/v-zhazhai/debug/richland/locale/zh-cn/punc/zhCN"
                step_resource_addpunc_model_name = "punc.onnx"
                
                punc_list = [".", ",", "?", "!", ";", ":", "，", "？", "。", "！", "；", "："]
                addpunc_model_path = os.path.join(step_resource_addpunc_model_dir, step_resource_addpunc_model_name)
                auto_addpunc = auto_addpunc_for_transcription(addpunc_model_path)
                
                for punc in punc_list:
                    text_removed_punc = text_removed_punc.replace(punc, "")
                simplified_input_text = auto_addpunc.add_punc_for_transcription(text_removed_punc, chunk_temp_addpunc_dir)
                s.writelines(line.split('\t')[0]+'\t'+simplified_input_text.replace(' ','')+'\n')
        except Exception as e:
            print(line)


if __name__ == "__main__":
    text_file = "/mnt/c/Users/v-zhazhai/Downloads/金龟子_output/金龟子教你看图写话_wavtrans.txt"
    user_temp_dir = '/mnt/c/Users/v-zhazhai/Downloads/金龟子_output/test'
    addpunc(text_file,user_temp_dir)