numbers = [12, 45, 7, 32, 89, 21]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number is:", largest)
