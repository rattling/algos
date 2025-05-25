def factorial(n):
    if n < 0 or int(n) != n:
        raise ValueError("n must be a non-negative integer")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(factorial(10))
