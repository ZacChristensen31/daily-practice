# Problem comes from LeetCode https://leetcode.com/problems/shortest-path-in-binary-matrix/
# Solved on Monday May 16th, 2022

from typing import List, Tuple, Dict
from heapq import heappop, heappush
from math import sqrt

"""
    Given a matrix of 0s and 1s, return the length of the shortest path from (0,0) to (n-1,m-1) traversing through
    only zeroes.
"""


def solve(grid: List[List[int]]) -> int:

    if len(grid) == 0:
        return -1

    if grid[0][0] != 0 or grid[-1][-1] != 0:
        return -1

    N = len(grid)
    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    queue = [(0, 0)]
    visited = {(0, 0)}

    def get_neighbors(node):
        x, y = node
        neighbors = []
        for x_offset, y_offset in offsets:
            new_row = x + x_offset
            new_col = y + y_offset

            if 0 <= new_row < N and 0 <= new_col < N and not grid[new_row][new_col] and (
            new_row, new_col) not in visited:
                neighbors.append((new_row, new_col))
        return neighbors

    distance = 1

    while queue:

        cells_at_distance = len(queue)

        for _ in range(cells_at_distance):
            current_node = queue.pop(0)
            if current_node == (N - 1, N - 1):
                return distance

            for next_node in get_neighbors(current_node):
                visited.add(next_node)
                queue.append(next_node)

        distance += 1

    return -1


if __name__ == '__main__':
    assert solve([]) == -1
    assert solve([[1]]) == -1
    assert solve([[0]]) == 1
    assert solve([[0, 0, 0], [1, 1, 0], [1, 1, 0]]) == 4

    test_input = [[0, 0, 0, 0, 1, 1, 1, 1, 0],
                  [0, 1, 1, 0, 0, 0, 0, 1, 0],
                  [0, 0, 1, 0, 0, 0, 0, 0, 0],
                  [1, 1, 0, 0, 1, 0, 0, 1, 1],
                  [0, 0, 1, 1, 1, 0, 1, 0, 1],
                  [0, 1, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 1, 0, 0, 0],
                  [0, 1, 0, 1, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0, 1, 0]]

    assert solve(test_input) == 11

    test_input = [[0, 0, 1, 0, 0, 1, 0, 1, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 1, 0, 1, 1, 1, 1, 1],
                  [0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [1, 1, 0, 0, 0, 1, 0, 0, 0],
                  [1, 0, 1, 0, 0, 1, 0, 0, 1],
                  [1, 1, 1, 1, 0, 0, 1, 0, 0],
                  [1, 0, 0, 1, 0, 0, 1, 1, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    assert solve(test_input) == 11

    # Successful - [(0, 0), (1, 1), (1, 2), (2, 3), (3, 4), (4, 4), (5, 4), (6, 5), (7, 5), (8, 6), (8, 7), (8, 8)]
    # [8, 0, 1, 0, 0, 1, 0, 1, 0]
    # [0, 8, 8, 0, 0, 0, 0, 0, 0]
    # [0, 1, 1, 8, 1, 1, 1, 1, 1]
    # [0, 0, 0, 1, 8, 0, 0, 0, 0]
    # [1, 1, 0, 0, 8, 1, 0, 0, 0]
    # [1, 0, 1, 0, 8, 1, 0, 0, 1]
    # [1, 1, 1, 1, 0, 8, 1, 0, 0]
    # [1, 0, 0, 1, 0, 8, 1, 1, 1]
    # [0, 0, 0, 0, 0, 0, 8, 8, 8]

    # Failure - [(0, 0), (1, 1), (1, 2), (2, 3), (3, 4), (4, 4), (5, 4), (6, 5), (7, 5), (8, 6), (8, 7), (8, 8)]
    # [8, 0, 1, 0, 0, 1, 0, 1, 0]
    # [0, 8, 8, 0, 0, 0, 0, 0, 0]
    # [0, 1, 1, 8, 1, 1, 1, 1, 1]
    # [0, 0, 0, 1, 8, 0, 0, 0, 0]
    # [1, 1, 0, 0, 8, 1, 0, 0, 0]
    # [1, 0, 1, 0, 8, 1, 0, 0, 1]
    # [1, 1, 1, 1, 0, 8, 1, 0, 0]
    # [1, 0, 0, 1, 0, 8, 1, 1, 1]
    # [0, 0, 0, 0, 0, 0, 8, 8, 8]