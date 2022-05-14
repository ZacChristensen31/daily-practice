from math import inf
from functools import reduce
from typing import List, Dict, Tuple

"""
Weighted Breadth First Search Algorithm. Returns not the path with least edges, but lowest weight.

params:
    edges: List[List[int]]
    start: int
    end: int

outputs:
    distance: int
    path: List[int]
"""


def dijkstra(edges: List[List[int]], start: int) -> Tuple[Dict[int, int], Dict[int, int]]:
    graph = reduce(lambda acc, curr: _handle_reduce(acc, curr), edges, {})
    nodes = list({*[x[0] for x in edges], *[x[1] for x in edges]})
    distances = {
        i: inf
        for i in nodes
    }

    previous = {
        i: None
        for i in nodes
    }

    distances[start] = 0

    while nodes:
        current_node = min(nodes, key=lambda x: distances[x])
        nodes.remove(current_node)

        for neighbor in graph.get(current_node, []):
            destination_node, distance = neighbor
            combined_distance = distances[current_node] + distance
            if combined_distance < distances[destination_node]:
                distances[destination_node] = combined_distance
                previous[destination_node] = current_node

    return previous, distances


def shortest_path_dijkstra(edges: List[List[int]], start: int, end: int) -> Tuple[int, List[int]]:
    if not edges:
        return -1, []
    previous, distances = dijkstra(edges, start)
    if end not in distances:
        return -1, []
    return distances[end], _calc_path(previous, start, end)


def _handle_reduce(acc: Dict[int, List[Tuple[int, int]]], curr: List[int]) -> Dict[int, List[Tuple[int, int]]]:
    s, d, t = curr
    if s not in acc:
        acc[s] = [(d, t)]
    else:
        acc[s].append((d, t))
    return acc


def _calc_path(previous: Dict[int, int], start: int, end: int) -> List[int]:
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    return path[::-1]
