from functools import reduce
from typing import List, Dict, Tuple

"""
General Breadth First Search Algorithm

Params: 
    edges: List[List[int]]
    start: int
    end: int
    
Outputs:
    distance: int
    path: List[int]
"""


# Path calculation comes from here
# https://stackoverflow.com/questions/8922060/how-to-trace-the-path-in-a-breadth-first-search
def bfs(edges: List[List[int]], start: int, end: int) -> Tuple[int, List[int]]:
    # Create a dictionary of all the nodes and their connections
    graph = reduce(lambda acc, curr: _handle_reduce(acc, curr), edges, {})

    # Create a queue of paths to explore
    queue = [[start]]

    while queue:
        current_path = queue.pop(0)
        current_node = current_path[-1]

        if current_node == end:
            print('Current Path', current_path)
            return len(current_path) - 1, current_path

        for edge in graph.get(current_node, []):
            next_path = list(current_path)
            next_path.append(edge)
            queue.append(next_path)

    return -1, []


def _handle_reduce(a: Dict[int, List[int]], b: List[int]):
    s, d = b
    if s not in a:
        a[s] = [d]
    else:
        a[s].append(d)
    return a
