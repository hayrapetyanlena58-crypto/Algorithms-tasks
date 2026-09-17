def insertion_sort(x):
    for i in range(1, len(x)):
        key = x[i]
        y = i - 1
        while y >= 0 and x[y] > key:
            x[y + 1] = x[y]
            y -= 1
        x[y + 1] = key
    return x

print(insertion_sort([9, 2, 6, 3, 8, 1, 4, 7])),
