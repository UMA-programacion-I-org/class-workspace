flags = [False, False, True]
print(any(flags))  # True

any_for = False
for flag in flags:
    if flag:
        any_for = True
        break

print(any_for)  # True

numbers = [3, 5, 8, 11]
has_even = any(list(map(lambda n: n % 2 == 0, numbers)))
print(has_even)  # True

has_even_for = False
for n in numbers:
    if n % 2 == 0:
        has_even_for = True
        break

print(has_even_for)  # True
