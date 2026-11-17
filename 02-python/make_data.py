"""Make shipments.csv: 2,000 made-up shipments for episode 2 (same file every time: fixed seed).
The first five rows are written by hand, because the video walks through them one by one."""
import csv
import random

random.seed(2)
CITIES = ["Pune", "Delhi", "Mumbai", "Chennai", "Bengaluru", "Hyderabad", "Kolkata", "Jaipur"]
rows = [
    ["S1001", "Pune", 3, 5],        # late
    ["S1002", "Delhi", 2, 2],       # exactly on time
    ["S1003", "Mumbai", 4, 3],      # early
    ["S1004", "Chennai", 2, ""],    # not delivered yet: the messy row
    ["S1005", "Bengaluru", 3, 6],   # late
]
for n in range(1006, 3001):
    promised = random.randint(2, 5)
    roll = random.random()
    if roll < 0.04:
        taken = ""                                   # not delivered yet
    elif roll < 0.30:
        taken = promised + random.randint(1, 4)      # late
    else:
        taken = random.randint(1, promised)          # on time
    rows.append([f"S{n}", random.choice(CITIES), promised, taken])

with open("shipments.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["id", "city", "days_promised", "days_taken"])
    w.writerows(rows)
print(len(rows), "shipments written")
