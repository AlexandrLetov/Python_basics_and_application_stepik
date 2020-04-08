import csv
from collections import Counter

res = []
with open('./Data/Crimes.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        temp = row['Primary Type']
        res.append(temp)
print(res)

c = Counter(res)
print(c)
