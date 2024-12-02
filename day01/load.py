from typing import List, Tuple


def load() -> Tuple[List[int], List[int]]:
    with open("day01/input.txt", "r", encoding="utf-8") as f:
        lst1 = []
        lst2 = []
        for line in f:
            v1, v2 = map(int, line.split())
            lst1.append(v1)
            lst2.append(v2)
    return lst1, lst2
