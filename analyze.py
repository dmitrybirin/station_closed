import csv

with open(file='./imported_data.csv', mode='r', encoding='utf-8-sig') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row)