import csv

data = [
    ["Name", "Marks", "Age"],
    ["Aman", 85, 20],
    ["Riya", 92, 21],
    ["Rahul", 78, 19]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file created successfully.")