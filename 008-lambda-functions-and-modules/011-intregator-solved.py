transactions = [500, -1200, 3000, 150, -50, 7000]

# 1. Total balance
balance = sum(transactions)

# 2. Absolute values
abs_values = list(map(lambda x: abs(x), transactions))

# 3. Large transactions (> 1000)
large = list(filter(lambda x: abs(x) > 1000, transactions))

# 4. Check if all positive
all_positive = all(list(map(lambda x: x > 0, transactions)))

# 5. Check if any transaction > 5000
any_huge = any(list(map(lambda x: abs(x) > 5000, transactions)))

print("Balance:", balance)
print("Absolute values:", abs_values)
print("Large transactions:", large)
print("All positive?", all_positive)
print("Any huge transaction?", any_huge)
