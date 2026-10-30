with open("sample.txt", "r") as file:
    content = file.read()

lines = content.splitlines()
print("Number of lines:", len(lines))
print("Number of characters:", len(content))