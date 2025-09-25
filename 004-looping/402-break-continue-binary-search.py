# Sorted list of numbers
numbers = [1, 3, 5, 7, 9, 11, 13, 15]

# Target number to find
target = 13

low = 0
high = len(numbers) - 1
index = -1

# Binary search using while loop

while low <= high:
    mid = (low + high) // 2

    if numbers[mid] == target:
        index = mid
        break
    elif numbers[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

if index != -1:
    print("Target found at index:", index)
else:
    print("Target not in list.")
