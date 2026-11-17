import csv

file = open("shipments.csv")
for row in csv.DictReader(file):
    if row["days_taken"] == "":
        print(row["id"], "not delivered yet")
    elif int(row["days_taken"]) > int(row["days_promised"]):
        print(row["id"], "LATE")
