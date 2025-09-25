numbers = [3, 4, 7, 8, 12, 14, 15, 18, 21]

for num in numbers:
    if num % 2 == 0:
        continue  # if the number is even, skip to the next iteration

    if num > 10:
        print("First odd greater than 10:", num)
        break  # stop the loop when found

    print("Checked number:", num)

print("Odd number less than or equal to 10:", num)
