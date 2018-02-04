import csv

from getters.station import normalizer
from datetime import datetime, date, time

data = []

with open(file='./manually_improved.csv', mode='r', encoding='utf-8-sig') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        if 'переход' in row['station']:
            print(row['station'])  
        # print(row['station'])
        # print(normalizer(row['station']))
        # row['station'] = normalizer(row['station'])