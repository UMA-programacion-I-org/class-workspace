items = [1, 2, 3, 4, 5]

doubled = list(map(lambda x: x * 2, items))

print(doubled)  # [2, 4, 6, 8, 10]

doubled_for = []
for item in items:
    doubled_for.append(item * 2)

print(doubled_for)  # [2, 4, 6, 8, 10]

temperatures_c = [0, 20, 37, 100]
temperatures_f = list(map(lambda c: (c * 9/5) + 32, temperatures_c))
print(temperatures_f)  # [32, 68, 98.6, 212]

temperatures_f_for = []
for c in temperatures_c:
    temperatures_f_for.append((c * 9/5) + 32)

print(temperatures_f_for)  # [32, 68, 98.6, 212]
