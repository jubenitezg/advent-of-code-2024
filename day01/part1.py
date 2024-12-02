from typing import List
from day01.load import load
from utils.timeit import timeit


@timeit
def part1(lst1: List[int], lst2: List[int]) -> int:
    lst1.sort()
    lst2.sort()
    total = 0
    for v1, v2 in zip(lst1, lst2):
        total += abs(v1 - v2)
    return total


if __name__ == "__main__":
    lst1, lst2 = load()
    ans = part1(lst1, lst2)
    print(ans)
