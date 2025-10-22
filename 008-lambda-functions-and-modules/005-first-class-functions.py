# First-class functions: functions can be assigned to variables, passed as arguments, and returned from other functions.

# ----- Example 1: Assigning functions to variables

def greet(name):
    return f"Hello, {name}!"


say_hello = greet 
print(say_hello("Alice"))

say_hello2 = lambda name: f"Hello, {name}!"
print(say_hello2("Bob"))

# ----- Example 2: Passing functions as arguments

def apply_operation(x, y, func):
    return func(x, y)

# pasando una función definida
def multiply(a, b):
    return a * b

print(apply_operation(3, 4, multiply))  # 12

# pasando una lambda directamente
print(apply_operation(3, 4, lambda a, b: a + b))  # 7

# ----- Example 3: Returning functions from other functions

def make_incrementer(n):
    return lambda x: x + n

increment_by_5 = make_incrementer(5)
print(increment_by_5(10))  # 15

increment_by_10 = make_incrementer(10)
print(increment_by_10(10))  # 20
