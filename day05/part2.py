from collections import defaultdict, deque
from typing import Dict, List, Set

from day05.load import load
from utils.timeit import timeit


def build_graph(parts: str) -> Dict[Set[int]]:
    adj_graph = defaultdict(set)
    for val in parts:
        x, y = map(int, val.split('|'))
        adj_graph[x].add(y)

    return adj_graph


def is_correct(values: List[int], g: Dict[Set[int]]):
    current = values[0]
    correct = True
    for i in range(1, len(values)):
        if values[i] not in g[current]:
            correct = False
            break
        current = values[i]
    return correct


def get_incorrects(updates: str, g: Dict[Set[int]]):
    incorrect = []
    for update in updates:
        values = list(map(int, update.split(',')))
        correct = is_correct(values, g)
        if not correct:
            incorrect.append(values)
    return incorrect


# https://www.interviewcake.com/concept/java/topological-sort
def topological_sort(nodes: List[int], g: Dict[Set[int]]):
    in_degree = {node: 0 for node in nodes}
    for node in nodes:
        for neighbor in g[node]:
            if neighbor in nodes:
                in_degree[neighbor] += 1

    queue = deque([node for node in nodes if in_degree[node] == 0])
    sorted_order = []
    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        for neighbor in g[node]:
            if neighbor in nodes:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

    if len(sorted_order) != len(nodes):
        raise ValueError("Graph has a cycle! No topological ordering exists.")
    return sorted_order


@timeit
def part2(order: str, updates: str):
    g = build_graph(order)
    incorrects = get_incorrects(updates, g)
    total = 0
    for incorrect in incorrects:
        correct = topological_sort(incorrect, g)
        total += correct[len(correct)//2]
    return total


if __name__ == '__main__':
    p1, p2 = load()
    print(part2(p1, p2))
