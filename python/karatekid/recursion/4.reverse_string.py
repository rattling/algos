def reverse(str, index):
    if index == 0:
        return str[index]
    else:
        return str[index] + reverse(str, index - 1)


str = "string"

print(reverse(str, len(str) - 1))
