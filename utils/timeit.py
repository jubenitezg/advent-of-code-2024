import time
from typing import Callable


def timeit(func: Callable):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed = end - start
        print(f"Time taken: {elapsed:.6f} seconds")
        return result

    return wrapper
