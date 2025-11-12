import time


def factorial(n: int) -> int:
    # caso base
    if n == 0:
        return 1

        # progreso: problema más pequeño
    return n * factorial(n - 1)


print(factorial(5))  # Output: 120
print(factorial(4))  # Output: 24


def factorial_iter(n: int) -> int:
    resultado = 1

    for k in range(1, n + 1):
        resultado *= k

    return resultado


print(factorial_iter(5))  # Output: 120
print(factorial_iter(4))  # Output: 24
