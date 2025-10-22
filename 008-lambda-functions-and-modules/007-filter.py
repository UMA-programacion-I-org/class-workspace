numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda n: n % 2 == 0, numbers))
print(evens)  # [2, 4, 6]

evens_for = []
for n in numbers:
    if n % 2 == 0:
        evens_for.append(n)

print(evens_for)  # [2, 4, 6]


words = ["apple", "hi", "banana", "yes"]
long_words = list(filter(lambda w: len(w) >= 4, words))
print(long_words)  # ['apple', 'banana']

long_words_for = []
for w in words:
    if len(w) >= 4:
        long_words_for.append(w)

print(long_words_for)  # ['apple', 'banana']
