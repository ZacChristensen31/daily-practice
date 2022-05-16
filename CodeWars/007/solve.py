# Problem comes from CodeWars https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/python
# Solved on Monday May 16th, 2022

from typing import List

"""
    Given a list of numbers, return a list where the odd numbers are sorted and the even numbers are left untouched
"""
def solve(nums: List[int]) -> List[int]:
    odds = sorted([x for x in nums if x % 2 == 1], reverse=True)
    return [x if x % 2 == 0 else odds.pop() for x in nums]


if __name__ == '__main__':
    assert solve([7, 1]) == [1, 7]
    assert solve([3, 2, 1]) == [1, 2, 3]
    assert solve([4, 3, 2, 1]) == [4, 1, 2, 3]
    assert solve([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]