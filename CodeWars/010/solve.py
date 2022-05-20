# Problem comes from CodeWars https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python
# Solved on Thursday May 19th, 2022

from typing import List

"""
    Given an array, return the array with all zeros moved to the end, retaining the order of the other elements.
"""


def solve(array: List[int]) -> List[int]:
    return sorted(array, key=lambda x: x == 0)


if __name__ == '__main__':
    assert solve([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]) == [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
    assert solve([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]) == [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0,
                                                                                   0, 0, 0, 0, 0, 0, 0, 0]
    assert solve([0, 0]) == [0, 0]
    assert solve([0, 1, 0]) == [1, 0, 0]
    assert solve([]) == []
