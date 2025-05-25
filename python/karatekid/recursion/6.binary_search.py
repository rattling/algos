import math


def binary_search(l: list, i: tuple, x):
    if i[0] > i[1]:
        return -1
    if i[1] == i[0]:
        if l[i[0]] != x:
            return -1
        else:
            return i[0]
    else:
        m = (i[1] + i[0]) // 2
        if x == l[m]:
            return m
        elif x > l[m]:
            return binary_search(l, (m + 1, i[1]), x)
        else:
            return binary_search(l, (i[0], m - 1), x)


l = [1, 2, 7, 9, 10, 11, 15]
x = 11

print(binary_search(l, (0, len(l) - 1), x))
