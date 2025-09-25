fibs = [0, 1]

# The list will contain the fibonacci numbers up to the N-th index
N = 20

for i in range(N - 1):
    fibs.append(fibs[-1] + fibs[-2])

print(fibs)
