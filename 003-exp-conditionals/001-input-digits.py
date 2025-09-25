import math

name = input("Ingresa tu nombre: ")
num = int(input("Ingresa el numero: "))

n_digits = math.floor(math.log10(num)) + 1

print(name)
print(n_digits)
print(f"The number of digits is: {n_digits}")

# --------

[1, 2, 4, 64]
