import csv

file = open("shipments.csv")
for row in csv.DictReader(file):
    if int(row["days_taken"]) > int(row["days_promised"]):
        print(row["id"], "LATE")
