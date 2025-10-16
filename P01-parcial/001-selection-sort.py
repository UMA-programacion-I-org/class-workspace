items = [4, 1, 3, 2]

print(f'Unsorted: {items}')

N = len(items)

for i in range(0, N - 1):
    min_idx = i

    for j in range(i + 1, N):
        if items[j] < items[min_idx]:
            min_idx = j

    if min_idx != i:
        temp = items[i]
        items[i] = items[min_idx]
        print(f'Pass {i}.a: {items}')
        items[min_idx] = temp

    print(f'Pass {i}.b: {items}')

print(f'Sorted: {items}')
