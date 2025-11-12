import time


def fib(n: int) -> int:
  # casos base
    if n == 0:
        return 0
    if n == 1:
        return 1

    # progreso: las llamadas recursivas son a n mas pequeños
    # eventualmente se alcanzara un caso base.
    return fib(n - 1) + fib(n - 2)


print(fib(5))  # Output: 5


def fib_iter(n: int) -> int:
    if n == 0:
        return 0

    a, b = 0, 1  # F(0), F(1)

    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


print(fib_iter(5))  # Output: 5

# Efficiency comparison
# N = 10
# N = 20
# N = 30
N = 50

start_time = time.time()
print(fib_iter(N))  # Output: 12586269025
print("Iterative fib took %s seconds" % (time.time() - start_time))

start_time = time.time()
print(fib(N))  # Output: 12586269025
print("Recursive fib took %s seconds" % (time.time() - start_time))
