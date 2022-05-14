from typing import Tuple, List, Dict
from functools import reduce

"""
Depth First Search

params:
    edges: List of [start, end] edges
    start: starting node
    
outputs:
    distance: number of edges traversed
    path: List of nodes visited

Returns a distance, and a path of nodes visited
"""


def dfs(edges: List[List[int]], start: int, end) -> Tuple[int, List[int]]:
    graph = reduce(lambda acc, curr: _handle_reduce(acc, curr), edges, {})

    output = _dfs_iteration(graph, [], [start], end)
    return (-1, []) if output is None else (len(output) - 1, output)


def _dfs_iteration(graph: Dict[int, List[int]], visited: List[int], current_path: List[int], target: int):
    current_node = current_path[-1]
    if current_node == target:
        return current_path

    if current_node not in visited and current_node in graph.keys():
        visited.append(current_node)
        for next_node in graph[current_node]:
            response = _dfs_iteration(graph, visited, [*current_path, next_node], target)
            if response is not None:
                return response

    return None

def _handle_reduce(a: Dict[int, List[int]], b: List[int]):
    s, d = b
    if s not in a:
        a[s] = [d]
    else:
        a[s].append(d)
    return a
