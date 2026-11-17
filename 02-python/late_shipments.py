import csv

late = 0
waiting = 0

file = open("shipments.csv")
for row in csv.DictReader(file):
    if row["days_taken"] == "":
        waiting = waiting + 1
    elif int(row["days_taken"]) > int(row["days_promised"]):
        late = late + 1

print("Late:", late)
print("Not delivered yet:", waiting)
