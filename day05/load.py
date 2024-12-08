from typing import Tuple


def load() -> Tuple[str, str]:
    with open("day05/input.txt", "r", encoding="utf-8") as f:
        p1, p2 = f.read().strip().split("\n\n")
        return p1.splitlines(), p2.splitlines()
