word = input("Enter word to search: ")

with open("sample.txt", "r") as file:
    content = file.read()

if word.lower() in content.lower().split():
    print("Word found.")
else:
    print("Word not found.")