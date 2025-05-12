import os
import glob
import numpy as np
import json
import matplotlib.pyplot as plt

validdata_info_file = r"C:\Users\v-zhazhai\Toosl\statistic\validdata_info.txt"
duration_list = []
with open(validdata_info_file, "r", encoding="utf-8")as fin:
    while True:
        line = fin.readline()
        if line:
            data = json.loads(line.strip())
            if 'segment_successful_duration' in data:
                isinvalid = False
                for key, value in data.items():
                    if value == 'invalid':
                        isinvalid = True
                if not isinvalid:
                    duration_list.append(float(data['segment_successful_duration']))
        else:
            break

p10 = np.percentile(duration_list, 10)
print(f"The 10th percentile (P10) of the list is: {p10}")
p20 = np.percentile(duration_list, 20)
print(f"The 20th percentile (P20) of the list is: {p20}")
p30 = np.percentile(duration_list, 30)
print(f"The 30th percentile (P30) of the list is: {p30}")
p40 = np.percentile(duration_list, 40)
print(f"The 40th percentile (P40) of the list is: {p40}")
p50 = np.percentile(duration_list, 50)
print(f"The 50th percentile (P50) of the list is: {p50}")
p60 = np.percentile(duration_list, 60)
print(f"The 60th percentile (P60) of the list is: {p60}")
p70 = np.percentile(duration_list, 70)
print(f"The 70th percentile (P70) of the list is: {p70}")
p80 = np.percentile(duration_list, 80)
print(f"The 80th percentile (P80) of the list is: {p80}")
p90 = np.percentile(duration_list, 90)
print(f"The 90th percentile (P90) of the list is: {p90}")
print("average value: " + str(sum(duration_list) / len(duration_list)))


    # Create histogram
print("count of valid segment: " + str(len(duration_list)))
plt.hist(duration_list, bins=200, edgecolor='black')

# Add title and labels
plt.title('Histogram of segment_duration')
plt.xlabel('segment_duration')
plt.ylabel('Frequency')

# Show plot
plt.show()