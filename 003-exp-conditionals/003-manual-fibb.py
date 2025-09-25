fib_0 = 0
fib_1 = 1

fib_2 = fib_0 + fib_1
fib_3 = fib_2 + fib_1
fib_4 = fib_3 + fib_2
fib_5 = fib_3 + fib_4

lis = [fib_0, fib_1, fib_2, fib_3, fib_4, fib_5]

print(lis)

fibs = [0, 1]

fibs.append(fibs[-1] + fibs[-2])
fibs.append(fibs[-1] + fibs[-2])
fibs.append(fibs[-1] + fibs[-2])
fibs.append(fibs[-1] + fibs[-2])

print(fibs)
