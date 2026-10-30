with open("sample.txt", "r") as file:
    words = file.read().split()

unique_words = sorted(set(words))

with open("unique.txt", "w") as file:
    file.write("\n".join(unique_words))

print("Unique words saved.")