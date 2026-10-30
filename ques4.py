with open("sample.txt", "r") as file:
    content = file.read()

words = content.split()
print("Number of words:", len(words))