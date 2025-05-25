import time

from functools import lru_cache


cache = {}


# memoization i.e. cache is way faster
def fib2(n):
    global cache
    if n in cache:
        return cache[n]
    if n <= 2:
        return 1
    elif n == 0:
        return 0
    else:
        cache[n] = fib2(n - 1) + fib2(n - 2)
        return cache[n]


# @lru_cache(maxsize=None)
def fib1(n):
    if n <= 2:
        return 1
    elif n == 0:
        return 0
    else:
        return fib1(n - 1) + fib1(n - 2)


start_time = time.time()
print(fib1(5))
print(f"Time: {1000*(time.time() - start_time)}")
start_time = time.time()
print(fib2(4))
print(f"Time: {1000*(time.time() - start_time)}")
