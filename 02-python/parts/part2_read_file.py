import csv

file = open("shipments.csv")
for row in csv.DictReader(file):
    print(row)
