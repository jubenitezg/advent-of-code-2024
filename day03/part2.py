import re
from day03.load import load
from utils.timeit import timeit


@timeit
def part2(msg: str) -> int:
    values = re.findall(r'mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))', msg)
    total = 0
    enabled = True
    for v in values:
        g1, g2, g3, g4 = v
        if g3 or g4:
            enabled = (g4 != "don't()") or (g3 == "do()")
        if g1 and g2 and enabled:
            total += int(g1) * int(g2)

    return total


if __name__ == '__main__':
    print(part2(load()))
