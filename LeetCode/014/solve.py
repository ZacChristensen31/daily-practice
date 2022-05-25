# Problem comes from LeetCode https://leetcode.com/problems/132-pattern/
# Solved on Monday, May 23rd, 2022

from typing import List
from math import inf

"""
    Given an array of integers, return true if there is a 132 pattern in the array.
    
    A 132 patter is defined as i < j < k, where n[i] < n[k] < n[j].
"""


def solve_O_n(nums: List[int]) -> bool:
    if len(nums) < 3:
        return False

    # Set up j (middle number) and the stack
    j = -inf
    stack = []

    # Work backwards, with the iterator being out "i" or "left" number
    for i in range(len(nums) - 1, -1, -1):

        # If the current number is greater than the middle number, then we have a 132 pattern
        if nums[i] < j:
            return True

        # If we have a stack to check, and the top of the stack is less than "i", remove off of the stack. This will
        # remove all numbers that are less than "i".
        while stack and stack[-1] < nums[i]:
            j = stack.pop()

        # Because we have popped everything off of the stack less than i, we guarantee that stack is sorted
        stack.append(nums[i])

    return False


if __name__ == '__main__':
    target_solve = solve_O_n

    assert target_solve([1, 2, 3, 4]) is False
    assert target_solve([3, 1, 4, 2]) is True
    assert target_solve([-1, 3, 2, 0]) is True
    assert target_solve([1, 7, 6, 5, 4, 3, 2]) is True
    assert target_solve([1, 2, 4, 1, 2]) is True
    assert target_solve([2, 2, 2, 4, 2, 2, 1]) is False
