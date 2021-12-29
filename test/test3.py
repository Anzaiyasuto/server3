# Generate a fake csv file.

import datetime
import random

file = open("data.csv", "w")

# header
file.write("date,data1,data2\n")

# data
date = datetime.datetime.now()
data1 = 0.5
data2 = 0.5

for i in range(100):
    date = date + datetime.timedelta(seconds=1)
    data1 = data1 + random.uniform(-0.01,0.01)
    data2 = data2 + random.uniform(-0.01,0.01)
    
    file.write(date.strftime("%Y/%m/%d %H:%M:%S"))
    file.write(",")
    file.write(str(data1))
    file.write(",")
    file.write(str(data2))
    file.write("\n")

file.close()