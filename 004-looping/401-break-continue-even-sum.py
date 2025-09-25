
N = 10
sum_evens = 0

for n in range(N):
    if n % 2 != 0:
        continue  # Skip odd numbers

    sum_evens += n

print("Sum of even numbers from 0 to", N-1, "is:", sum_evens)
