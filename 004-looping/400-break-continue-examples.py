
# Example with continue - print only odd numbers
for i in range(1, 6):
    if i % 2 == 0:
        continue  # skips even numbers

    print(i)

print("Loop finished!")

# ---------

# Example with break - linear search
numbers = [3, 7, 12, 9, 5]

for num in numbers:
    print(f"checking element {num}")

    if num == 12:
        print("Found:", num)
        break  # ends the loop
