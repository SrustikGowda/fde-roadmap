import csv

pune = 0

file = open("shipments.csv")
for row in csv.DictReader(file):
    if row["city"] == "Pune":
        pune = pune + 1

print("Pune:", pune)
