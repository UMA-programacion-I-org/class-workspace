def mean(numbers):
    if len(numbers) == 0:
        return 0

    total = 0

    for number in numbers:
        total += number

    return total / len(numbers)


print(mean([1, 2, 3, 4, 5]))  # Output: 3.0
print(mean([]))  # Output: 0
print(mean([10, 20, 30]) + mean([1, 2, 3, 4, 5]))  # Output: 23.0


def stats(numbers):
    if len(numbers) == 0:
        return 0, None, None

    total = 0
    minimum = numbers[0]
    maximum = numbers[0]

    for number in numbers:
        total += number
        if number < minimum:
            minimum = number
        if number > maximum:
            maximum = number

    return mean(numbers), minimum, maximum


avg, min_val, max_val = stats([1, 2, 3, 4, 5])
# Output: Avg: 3.0, Min: 1, Max: 5
print(f"Avg: {avg}, Min: {min_val}, Max: {max_val}")
