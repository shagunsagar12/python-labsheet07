import csv

marks = []
ages = []

with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        marks.append(float(row["Marks"]))
        ages.append(float(row["Age"]))

print("Average Marks:", sum(marks) / len(marks))
print("Average Age:", sum(ages) / len(ages))