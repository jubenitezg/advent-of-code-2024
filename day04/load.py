from typing import List


def load() -> List[str]:
    with open("day04/input.txt", "r", encoding="utf-8") as f:
        m = []
        for line in f:
            m.append(line)
        return m
