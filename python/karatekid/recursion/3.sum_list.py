def sum_list(l):
    """Attempt 1"""
    if len(l) == 0:
        return 0
    else:
        return l[-1] + sum_list(l[0:-1])


def sum_list2(l, index):
    """Avoids slicing which creates new list every time"""
    if index < 0:
        return 0
    else:
        return l[index] + sum_list2(l, index - 1)


def sum_list3(l, index=0):
    """Starting from beginning means you don't need to pass in list length. But no substantial difference really."""
    if index > len(l) - 1:
        return 0
    else:
        return l[index] + sum_list3(l, index + 1)


l = [8, 2, 7]
print(sum_list(l))
print(sum_list2(l, len(l) - 1))
print(sum_list3(l))
