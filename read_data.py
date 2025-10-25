import serial
import csv
from datetime import datetime
import os
import time

MAX_FILE_SIZE = 50 * 1024 * 1024 

ser = serial.Serial('/dev/cu.XXXXXXXX', 9600)

file = 'data/temp_humid_data.csv'
with open(file, 'a', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    while True:
        csvfile.flush() 
        if os.path.getsize(file) > MAX_FILE_SIZE:
            break

        line = ser.readline().decode('utf-8').strip()

        values = line.split(',')

        now_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        row = [now_str] + values

        csvwriter.writerow(row)

        time.sleep(900)

ser.close()
