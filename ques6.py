with open("sample.txt", "r") as file:
    for number, line in enumerate(file, start=1):
        if number % 2 == 0:
            print(line, end="")