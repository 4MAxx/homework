import csv
from datetime import date

filename = 'zad3_files.txt'
date_list = []
with open(filename, 'r') as f_read:
    fr = csv.reader(f_read, delimiter="/")
    for row in fr:
        date_list.append(date(int(row[2]), int(row[1]), int(row[0])))
print(f'Самая ранняя дата из файла {filename}')
a = sorted(date_list)[0]
print(f'{a.day}/{a.month}/{a.year}')