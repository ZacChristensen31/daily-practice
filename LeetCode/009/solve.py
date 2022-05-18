# Problem comes from LeetCode https://leetcode.com/problems/sort-array-by-parity/submissions/
# Solved on Wednesday May 18, 2022

from typing import List

"""
    Given a list of numbers, return the list with even numbers first, in any order, then odd numbers, in any order.
"""


def solve(nums: List[int]) -> List[int]:
    return sorted(nums, key=lambda x: x % 2)


def _check_solution(input_nums):
    solution = solve(input_nums)
    still_even = True
    for num in solution:
        if num % 2 == 1:
            still_even = False
        if not still_even and num % 2 == 0:
            raise Exception(f"{num} is even, but the list is not sorted correctly", solution)


if __name__ == '__main__':
    _check_solution([3, 1, 2, 4])
    _check_solution([1, 3, 5, 7])
    _check_solution([2, 4, 6, 8])
    _check_solution([1, 2, 3, 4, 5, 6, 7, 8])
    _check_solution([1, 2, 3, 4, 5, 6, 7, 8, 9])
    _check_solution([])
    _check_solution([2, 4, 6, 8, 1, 3, 5, 7])
