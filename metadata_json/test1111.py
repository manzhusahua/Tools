import os
import json


def get_styleWave(style,style_list,wave_list,speaker):
    sid = {}
    with open(wave_list,'r',encoding='utf8') as f:
            for name in f.readlines():
                if '.wav' in name:
                    wave_name  = os.path.split(name)[-1].replace('.wav\n','')
                    for audio_range in style_list[style]:
                        if audio_range.split('-')[0] <= wave_name <= audio_range.split('-')[-1]:
                            sid[wave_name] = {"style":style,"role":"","speaker":speaker,"domain":""}
    return sid

style = {'NeutralChat': ['3000000001-3000000500'], 'NeutralCustomerService': ['4000000001-4000000500'], 'Cheerfulchat': ['9130000001-9130000500'], 'CheerfulCustomerService': ['9140000001-9140000500']}

output_dir = r'C:\Users\v-zhazhai\Toosl\code\metadata_json\output'
wave_list = r"C:\Users\v-zhazhai\Toosl\code\metadata_json\output\ArEGShaKir.txt"

d = {}
for name in style:
    uttid = get_styleWave(name,style,wave_list,"ArEGShaKir")
    print(uttid)
#     d.update(uttid)
# with open(os.path.join(output_dir,"record_style.json"),'a') as write_f:
#         json.dump(d, write_f, indent=4, ensure_ascii=False)


