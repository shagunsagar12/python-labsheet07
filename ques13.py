with open("numbers.txt", "r") as file:
    numbers = list(map(float, file.read().split()))

print("Sum:", sum(numbers))
print("Average:", sum(numbers) / len(numbers))