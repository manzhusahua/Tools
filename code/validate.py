import os

import json

input=r"D:\test\validate\podcast\validdata_info.txt"
with open(input)as fin:
    lines = fin.readlines()
ctotal = 0
cvalidate = 0
cinvalidate = 0
cfailed = 0
totalduration = 0
validateduration = 0
invalidateduration = 0
linenumber = 0
for line in lines:
    linenumber = linenumber + 1
    #print(linenumber)
    #print(line.strip())
    data = json.loads(line.strip())
    if 'segment_successful_duration' in data:
        totalduration = totalduration + float(data['segment_successful_duration'])
        isinvalid = False
        for key, value in data.items():
            if value == 'invalid':
                isinvalid = True
        if isinvalid:
            cinvalidate = cinvalidate + 1
            invalidateduration = invalidateduration + float(data['segment_successful_duration'])
        else:
            cvalidate = cvalidate + 1
            validateduration = validateduration + float(data['segment_successful_duration'])
    #print(data)
    else:
        cfailed = cfailed + 1
        print(data)
print("total line: " + str(linenumber))
print("faile line = " + str(cfailed))
print("invalidate line = " + str(cinvalidate))
print("validate line = " + str(cvalidate))

print("total duration = " + str(totalduration))
print("validate duration = " + str(validateduration))
print("invalidateduration duration = " + str(invalidateduration))
