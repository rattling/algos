def merge(a, b):
    """I had it close. But this one uses pointers again to avoid popping which has higher time complexity"""
    merged = []
    i, j = 0, 0  # pointers for list a and b respectively
    # Loop until one of the lists is exhausted
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    # Append any remaining elements from a or b
    if i < len(a):
        merged.extend(a[i:])
    if j < len(b):
        merged.extend(b[j:])
    return merged


def merge_sort(l):
    if len(l) < 2:
        return l
    else:
        m = len(l) // 2
        left = merge_sort(l[:m])
        right = merge_sort(l[m:])
        return merge(left, right)


# Test the optimized merge sort:
l = [9, 3, 26, 22, 19, 101, 5, 7, 32, 100]
print(merge_sort(l))
