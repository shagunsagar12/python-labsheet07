import csv

with open("students.csv", "r", newline="") as source:
    data = list(csv.reader(source))

with open("students_copy.csv", "w", newline="") as destination:
    writer = csv.writer(destination)
    writer.writerows(data)

print("CSV file copied successfully.")