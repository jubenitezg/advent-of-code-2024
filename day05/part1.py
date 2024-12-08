from collections import defaultdict
from typing import Dict, Set

from day05.load import load
from utils.timeit import timeit


def build_graph(parts: str) -> Dict[Set[int]]:
    adj_graph = defaultdict(set)
    for val in parts:
        x, y = map(int, val.split('|'))
        adj_graph[x].add(y)

    return adj_graph


@timeit
def part1(order: str, updates: str) -> int:
    g = build_graph(order)
    total = 0
    for update in updates:
        values = list(map(int, update.split(',')))
        current = values[0]
        correct = True
        for i in range(1, len(values)):
            if values[i] not in g[current]:
                correct = False
                break
            current = values[i]
        if correct:
            total += values[len(values)//2]
    return total


if __name__ == '__main__':
    p1, p2 = load()
    print(part1(p1, p2))
