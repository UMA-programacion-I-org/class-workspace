double = lambda x: x * 2
print(double(5))  # 10

apply_discount = lambda price, discount: price * (1 - discount)
print(apply_discount(100, 0.2))  # 80.0

is_even = lambda n: n % 2 == 0
print(is_even(4))  # True
print(is_even(5))  # False

is_odd = lambda n: not is_even(n)
print(is_odd(4))  # False
print(is_odd(5))  # True