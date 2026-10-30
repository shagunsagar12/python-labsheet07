with open("file1.txt", "r") as file:
    data1 = file.read()

with open("file2.txt", "r") as file:
    data2 = file.read()

with open("merged.txt", "w") as file:
    file.write(data1 + "\n" + data2)

print("Files merged successfully.")