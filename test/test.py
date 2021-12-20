import datetime
import csv
import time
from csv import writer

file_path = "./test_data.csv"

def update_csv(ti, te, mo):
    try:
        list_data = [ti,te,mo]

        f = open(file_path, 'a', newline='')
        writer_object = csv.writer(f)
        writer_object.writerow(list_data)
        return "succeeded to write"
    except Exception as e:
        print(e)
        return "failed to write"
    finally:
        f.close()

print("test_csv")
for num in range(10):
    tim = "0"
    temp ="1"
    mois ="2"
    update_csv(tim, temp, mois)
    
print("finish")
