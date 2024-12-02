from collections import Counter
from typing import List

from day01.load import load
from utils.timeit import timeit


@timeit
def part2(lst1: List[int], lst2: List[int]) -> int:
    cnt = Counter(lst2)
    total = 0
    for v1 in lst1:
        total += v1 * cnt[v1]
    return total


if __name__ == '__main__':
    lst1, lst2 = load()
    print(part2(lst1, lst2))
