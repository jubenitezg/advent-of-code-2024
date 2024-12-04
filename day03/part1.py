import re
from day03.load import load
from utils.timeit import timeit


@timeit
def part1(msg: str) -> int:
    values = re.findall(r'mul\((\d+),(\d+)\)', msg)
    total = 0
    for v in values:
        ia, ib = map(int, v)
        total += ia * ib
    return total


if __name__ == '__main__':
    print(part1(load()))
