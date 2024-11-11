from curses import wrapper
from functools import lru_cache, wraps


@lru_cache(maxsize=5)
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(6))

@lru_cache(maxsize=5)
def fibonacci(n):
    '''This function outputs the sum of n Fibonacci numbers'''
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci.__doc__)
print(fibonacci(6))

import time

def log_execute(func):
    def wrapper(*args):
        print(f"\nEntering function {func.__name__} at {time.time()}")
        res = func(*args)
        print(f"Exiting function {func.__name__} at {time.time()}")
        return res
    return wrapper

@log_execute
@lru_cache
def fibonacci(n):
    '''This function outputs the sum of n Fibonacci numbers'''
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci.__doc__)
print(fibonacci(10))