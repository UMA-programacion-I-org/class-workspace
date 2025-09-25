# Sorted list of numbers
numbers = [1, 3, 5, 7, 9, 11, 13, 15]

# Target number to find
target = 13

low = 0
high = len(numbers) - 1
found = False
index = -1

# Binary search using while loop

while low <= high and not found:
    mid = (low + high) // 2

    if numbers[mid] == target:
        found = True
        index = mid
    elif numbers[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

if found:
    print("Target found at index:", index)
else:
    print("Target not in list.")
