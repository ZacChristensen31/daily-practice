# Problem comes from LeetCode https://leetcode.com/problems/permutations-ii/
# Solved on Thursday May 12th, 2022

from typing import List
from itertools import permutations


def easy_solve(nums: List[int]):
    return list(set(permutations(nums, len(nums))))


if __name__ == '__main__':
    for i in easy_solve([1, 2, 1]):
        assert i in [(1, 1, 2), (1, 2, 1), (2, 1, 1)]

    for i in easy_solve([1, 2, 3]):
        assert i in [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
