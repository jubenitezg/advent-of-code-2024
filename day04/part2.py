from typing import List
from day04.load import load
import re

from utils.timeit import timeit


# order
# 123
# 4x5
# 678
di = [-1, 0, -1, 0, 0, 1, 1, 1]
dj = [-1, -1, 1, -1, 1, -1, 0, 1]


@timeit
def part2(grid: List[str]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    total = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "A":
                word = ""
                for k in range(8):
                    dik = i + di[k]
                    djk = j + dj[k]
                    if 0 <= dik < rows and 0 <= djk < cols:
                        word += grid[dik][djk]
                if re.match(r"M.S..M.S|S.S..M.M|M.M..S.S|S.M..S.M", word):
                    total += 1
    return total


if __name__ == '__main__':
    print(part2(load()))
