def hipotenuse(a, b):
    squares = a**2 + b**2
    return squares ** 0.5


# This will raise an error because 'squares' is not defined outside the function
# print(squares)

x = 100  # Global variable


def show():
    x = 5   # Local variable with the same name
    print("Inside the function, x =", x)


show()
print("Outside the function, x =", x)

# Output:
# Inside the function, x = 5
# Outside the function, x = 100
