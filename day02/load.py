from typing import List


def load() -> List[List[int]]:
    with open("day02/input.txt", "r", encoding="utf-8") as f:
        m = []
        for line in f:
            row = list(map(int, line.split()))
            m.append(row)
    return m
