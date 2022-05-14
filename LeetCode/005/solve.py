# Problem comes from LeetCode https://leetcode.com/problems/network-delay-time/
# Solved on Saturday May 14th, 2022

from typing import List
from GeneralAlgorithms.Dijkstra.dijkstra import dijkstra

'''
Given a list of times (source node, target node, time), a number of nodes n, and a starting node k, return how long it
takes to reach all nodes from the starting node. If it is impossible to reach a node, return -1.
'''


def solve(times: List[List[int]], n: int, k: int) -> int:
    previous, distances = dijkstra(times, k)
    if len(previous) != n:
        return -1
    del previous[k]
    return -1 if None in previous.values() else max(distances.values())


if __name__ == '__main__':
    assert solve([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2
    assert solve([[1, 2, 1]], 2, 1) == 1
    assert solve([[1, 2, 1]], 2, 2) == -1
