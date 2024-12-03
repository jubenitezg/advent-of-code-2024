from typing import List
from day02.load import load
from utils.timeit import timeit


@timeit
def part1(reports: List[List[int]]) -> int:
    safe = 0
    for report in reports:
        increasing = all(report[i] < report[i+1]
                         for i in range(0, len(report)-1))
        decreasing = all(report[i] > report[i+1]
                         for i in range(0, len(report)-1))
        if not increasing and not decreasing:
            continue
        if all(0 < abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1)):
            safe += 1
    return safe


if __name__ == '__main__':
    m = load()
    print(part1(m))
