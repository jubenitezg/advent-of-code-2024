from typing import List
from day02.load import load
from utils.timeit import timeit


def is_safe(report: List[int]) -> bool:
    length = len(report)
    any_safe = False
    for i in range(0, length):
        report_copy = report[:i] + report[i + 1:]
        n = len(report_copy)
        increasing = all(report_copy[x] < report_copy[x+1]
                         for x in range(0, n-1))
        decreasing = all(report_copy[x] > report_copy[x+1]
                         for x in range(0, n-1))
        if not increasing and not decreasing:
            continue
        any_safe = any_safe or all(
            0 < abs(report_copy[i] - report_copy[i + 1]) <= 3 for i in range(n - 1))

    return any_safe


@timeit
def part2(reports: List[List[int]]) -> int:
    safe = 0
    for report in reports:
        r_safe = is_safe(report)
        if r_safe:
            safe += 1
    return safe


if __name__ == '__main__':
    m = load()
    print(part2(m))
