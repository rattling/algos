def power_set(lst):
    """
    Return the power set of the list lst:
    a list of all subsets of lst.
    """
    # Base case: the power set of the empty list is a list containing the empty list
    if not lst:
        return [[]]

    # Split into head and tail
    head, *tail = lst

    # 1) Recursively compute the power set of the tail
    subsets_without = power_set(tail)

    # 2) For each subset in subsets_without, prepend head to form new subsets
    subsets_with = [[head] + subset for subset in subsets_without]

    # 3) Combine the subsets that exclude head and those that include head
    return subsets_without + subsets_with

# Example usage:
print(power_set([1, 4, 6]))
# Output:
# [[], [6], [4], [4, 6], [1], [1, 6], [1, 4], [1, 4, 6]]
