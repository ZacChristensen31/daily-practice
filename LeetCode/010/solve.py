# Problem comes from LeetCode https://leetcode.com/problems/unique-paths-ii/
# Solved on Thursday May 19th, 2022

from typing import List

"""
    Given a matrix where 0 is an open cell and 1 is a blocked cell, find the total number of paths from the top left
    to the bottom right if you can only move right or down 
"""


def solve(obstacleGrid: List[List[int]]) -> int:
    for i in range(len(obstacleGrid)):
        for j in range(len(obstacleGrid[0])):
            if obstacleGrid[i][j] == 1:
                obstacleGrid[i][j] = 0
            else:
                if i == 0 and j == 0:
                    obstacleGrid[i][j] = 1
                else:
                    top = 0 if i == 0 else obstacleGrid[i - 1][j]
                    left = 0 if j == 0 else obstacleGrid[i][j - 1]
                    obstacleGrid[i][j] = top + left

    return obstacleGrid[-1][-1]


if __name__ == '__main__':
    assert solve([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]) == 2

    assert solve([
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 0, 0, 0]
    ]) == 3

    assert solve([
        [0, 0, 0, 0, 1],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]) == 5

    assert solve([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]) == 15
