import csv

with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Priya", 88, 20])

print("Record added successfully.")