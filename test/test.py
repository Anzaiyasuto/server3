import datetime
import csv
import time

file_path = "./test_data.csv"

def update_csv(ti, te, mo):
    time = ti
    temp = te
    mois = mo

    try:
        f = open(file_path, 'a')
        writer = csv.writer(f)
        writer.writerow([ti, te, mo])
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
