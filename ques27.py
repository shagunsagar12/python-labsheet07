import csv

with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["Name"], row["Marks"])