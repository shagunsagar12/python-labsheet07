word = input("Enter word: ")

with open("sample.txt", "r") as file:
    words = file.read().lower().split()

print("Occurrences:", words.count(word.lower()))