"""
用于批量生成yaml
"""
import codecs
import chardet
import os

def BatchGenerateYaml(yamlfile,outputdir,word):
    content=codecs.open(yamlfile,'rb').read()
    yaml_word = open(yamlfile,'r',encoding=chardet.detect(content)['encoding']).readlines()
    with open(outputdir,'w',encoding='utf8') as s:
        for line in yaml_word:
            if "AncientPoetry" in line:
                line = line.replace("AncientPoetry",word)
            # if "last_output_datastore_path" in line:
            #     line = line.replace('zh-cn/asr','zh-cn/'+word)
            s.writelines(line)

def GenerateSH(outputdir):
    with open(r"C:\Users\v-zhazhai\OneDrive - Microsoft\yaml\zh-CN\zh-CN_TTS\V3\ZhCNHonor.bat",'a',encoding='utf8') as s:
    # with open(outputdir+'.bat','a',encoding='utf8') as s:
        for line in os.listdir(outputdir):
            # if "filelist_50" in line and "try2.yaml" in line:
            if ".yaml" in line:
            # if "_speaker_detect" in line:
                word = 'python aml_submit.py --config_path "{}" --experiment_name  zh-CN_TTS_V3_ZhCNHonor --workspace_name zetta-prod-ws03-wus2 --prs_compute_target_name ZettA-AML-Data --pss_compute_target_name ZettA-AML-Data --display_name {}_try1'.format(os.path.join(outputdir,line),line.replace('.yaml',''))
                s.writelines(word+'\n\n')

if __name__ == "__main__":
    
    yamlfile = r"C:\Users\v-zhazhai\OneDrive - Microsoft\yaml\zh-CN\zh-CN_TTS\V3\F128\F128_AncientPoetry_speaker_detect.yaml"
    save_path = r"C:\Users\v-zhazhai\OneDrive - Microsoft\yaml\zh-CN\zh-CN_TTS\V3\ZhCNHonor"
    # n = 2
    # while n<=2:
    #     outputdir = os.path.join(save_path,"filelist_0-15_part"+str(n)+"_statistics_try1.yaml")
    #     BatchGenerateYaml(yamlfile,outputdir,"filelist_0-15_part"+str(n))
    #     n+=1
    
    GenerateSH(save_path)
    # chunk_path = ["AudioBook","Chat","CloudAudio","CustomerService","General","Mixlingual","ModernPoetry","Newscast","ProperNoun","PureEnglish","Recipe","Sentiment","Speech","Spelling","Story","TrueConfession","TV","VA"]
    
    # for name in chunk_path:
    #     outputdir = os.path.join(save_path,f"F128_{name}_speaker_detect.yaml")
    #     BatchGenerateYaml(yamlfile,outputdir,name)