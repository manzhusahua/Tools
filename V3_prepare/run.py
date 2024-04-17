import os
from step3_extractvttlist import step3
from step4_dump_json import step4
from step5_UpdataBlob import step5


list_file_name = [r"FY23Q2\BingYouTube\Travel_Events",r"FY23Q2\YouTube\Travel_Events",r"FY23Q4-1\YouTube\Travel_Events",r"FY23Q4-2\YouTube\Travel_Events",r"FY23Q4-3\YouTube\Travel_Events",r"FY24Q1-1\YouTube\Travel_Events",r"FY24Q1-3\YouTube\Travel_Events",r"FY24Q2-1\YouTube\Travel_Events",r"FY24Q2-2\YouTube\Travel_Events",r"FY24Q2-3\YouTube\Travel_Events",r"FY24Q3-1\YouTube\Travel_Events"]

locals = "fr-FR"
inputdir = r"C:\Users\v-zhazhai\Downloads"

inputdirs = os.path.join(inputdir,locals)


batch = "batch15"

step3 = step3()
step4 = step4()
step5 = step5()

# print("step3_extractvttlist start")
# step3.step3_extractvttlist(list_file_name,inputdirs,batch)
# print("step4_dump_json start")
# step4.step4_dump_json(list_file_name,inputdirs,batch)

# step5.step5_updata_tts_filelist(locals,inputdir)
step5.step5_updata_dump_json(locals,inputdir,int(batch.replace('batch','')))