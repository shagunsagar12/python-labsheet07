with open("user.txt", "w") as file:
    n = int(input("Enter number of lines: "))

    for i in range(n):
        line = input("Enter a line: ")
        file.write(line + "\n")

print("Data saved successfully.")