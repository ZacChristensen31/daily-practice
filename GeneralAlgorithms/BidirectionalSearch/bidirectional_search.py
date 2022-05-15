from typing import List, Dict, Tuple
from functools import reduce
from GeneralAlgorithms.PriorityQueue.priority_queue import PriorityQueue


def bidirectional_search(edges: List[List[int]], start: int, end: int) -> Tuple[int, List[int]]:
    graph = reduce(lambda acc, curr: _handle_reduce(acc, curr), edges, {})

    forward_queue = PriorityQueue()
    backward_queue = PriorityQueue()

    forward_queue.push([start], 0)
    backward_queue.push([end], 0)

    forward_costs = {start: 0}
    backward_costs = {end: 0}

    while not forward_queue.isEmpty() and not backward_queue.isEmpty():

        # Priority, Index, Path
        next_forward_priority, _ = forward_queue.top()
        next_backward_priority, _ = backward_queue.top()

        if next_forward_priority < next_backward_priority:
            result = _iteration(graph, forward_costs, backward_costs, forward_queue, backward_queue, _forwards_join)
            if result is not None:
                return result
        else:
            result = _iteration(graph, backward_costs, forward_costs, backward_queue, forward_queue, _backwards_join)
            if result is not None:
                return result

    return -1, []


def _iteration(graph, primary_costs, secondary_costs, primary_queue, secondary_queue, handle_join):
    priority, current_path = primary_queue.pop()
    current_node = current_path[-1]

    if current_node in secondary_costs.keys():
        secondary_paths = list(filter(lambda x: x[2][-1] == current_node, secondary_queue))
        target_secondary_path = secondary_paths[0][2]
        combined_path = handle_join(current_path, target_secondary_path)
        return len(combined_path) - 1, combined_path

    for next_node, next_priority in graph.get(current_node, []):
        next_cost = priority + next_priority
        if next_node not in primary_costs.keys() or next_cost < primary_costs[next_node]:
            primary_costs[next_node] = next_cost
            next_path = current_path + [next_node]
            primary_queue.push(next_path, next_cost)

    return None


def _backwards_join(primary_path, secondary_path):
    return [*secondary_path[:-1], *primary_path[::-1]]


def _forwards_join(primary_path, secondary_path):
    return [*primary_path[:-1], *secondary_path[::-1]]


def _handle_reduce(a: Dict[int, List[Tuple[int, int]]], b: List[int]):
    s, d, w = b
    if s not in a:
        a[s] = [(d, w)]
    else:
        a[s].append((d, w))

    if d not in a:
        a[d] = [(s, w)]
    else:
        a[d].append((s, w))

    return a
