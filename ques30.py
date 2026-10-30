import csv

files = ["students1.csv", "students2.csv"]

with open("combined.csv", "w", newline="") as output:
    writer = csv.writer(output)

    for index, filename in enumerate(files):
        with open(filename, "r", newline="") as source:
            reader = csv.reader(source)

            for row_number, row in enumerate(reader):
                if index > 0 and row_number == 0:
                    continue

                writer.writerow(row)

print("CSV files combined successfully.")