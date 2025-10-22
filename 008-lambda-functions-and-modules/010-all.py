flags = [True, True, True]
print(all(flags))  # True

all_for = True
for flag in flags:
    if not flag:
        all_for = False
        break

print(all_for)  # True

passwords = ["abc123", "secure1", "pass!"]
valid = all(map(lambda p: len(p) >= 6, passwords))
print(f'valid: {valid}')  # False

valid_for = True
for p in passwords:
    if not (len(p) >= 6):
        valid_for = False
        break

print(valid_for)  # True
