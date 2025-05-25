from Levenshtein import distance
from functools import lru_cache
import time


@lru_cache(maxsize=None)
def lev1(a: str, b: str):
    """
    O(n^k) - caching improves by several orders of magnitude but still 5x to 5x slower or more slower than library
    for approx word lenghts in our domain
    """

    if len(b) == 0:
        return len(a)
    elif len(a) == 0:
        return len(b)
    elif a[0] == b[0]:
        return lev1(a[1:], b[1:])
    else:
        return 1 + min(lev1(a[1:], b), lev1(a, b[1:]), lev1(a[1:], b[1:]))


def lev2(a: str, b: str):
    """5x or more faster then lev1"""

    grid = [[0 for _ in range(len(a) + 1)] for j in range(len(b) + 1)]
    grid[0] = [x for x in range(0, len(a) + 1)]
    for i in range(len(b) + 1):
        grid[i][0] = i

    for i in range(1, len(b) + 1):
        for j in range(1, len(a) + 1):
            match = 0 if a[j - 1] == b[i - 1] else 1
            grid[i][j] = min(
                grid[i - 1][j - 1] + match, grid[i][j - 1] + 1, grid[i - 1][j] + 1
            )

    return grid[-1][-1]


a = "dividend_price"
b = "orangeorangeorangeoranjhjhh"
start_time = time.time()
print(f"lev1: {lev1(a, b)}")
print(f"Time: {1000*(time.time() - start_time)}")
start_time = time.time()
print(f"lev2: {lev2(a, b)}")
print(f"Time: {1000*(time.time() - start_time)}")
start_time = time.time()
print(f"lev library: {distance(a, b)}")
print(f"Time: {1000*(time.time() - start_time)}")
