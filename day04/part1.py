from typing import List
from day04.load import load
from utils.timeit import timeit


di = [-1, -1, -1, 0, 1, 1,  1,  0]
dj = [-1,  0,  1, 1, 1, 0, -1, -1]


@timeit
def part1(grid: List[str]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    total = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "X":
                for k in range(8):
                    word = "X"
                    for u in range(1, 4):
                        dik = i + di[k]*u
                        djk = j + dj[k]*u
                        if 0 <= dik < rows and 0 <= djk < cols:
                            word += grid[dik][djk]
                    if word == "XMAS":
                        total += 1
    return total


if __name__ == '__main__':
    print(part1(load()))
