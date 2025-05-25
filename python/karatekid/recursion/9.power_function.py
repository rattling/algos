import math


def power(base: float, exp: int) -> float:
    """
    Compute base**exp using exponentiation by squaring.
    Supports negative exponents as well.
    """
    # Handle negative exponent by flipping and taking reciprocal
    if exp < 0:
        return 1 / power(base, -exp)
    # Base cases
    if exp == 0:
        return 1
    if exp == 1:
        return base
    # Recursive “square” step
    if exp % 2 == 0:
        half = power(base, exp // 2)
        return half * half
    else:
        # NOTE - I corrected ChatGPT here. We don't need to subtract 1 from exp as we are using floor division
        half = power(base, exp // 2)
        return base * half * half


# Examples
print(power(2, 10))  # 1024
print(power(7, -3))  # 1/343 ≈ 0.0029154518950437317
print(power(5, 0))  # 1
print(power(3, 5))  # 243
