# Problem comes from CodeWars https://www.codewars.com/kata/550498447451fbbd7600041c
# Solved on Wednesday May 11th, 2022

"""
Essentially a function that takes in two lists. Check if list b matches the squares of list a. Order does not matter.
"""

from typing import List


def solve(a: List[int] or None, b: List[int] or None) -> bool:
    if not a or not b:
        return False
    return [x * x for x in sorted(a)] == sorted(b)


if __name__ == '__main__':
    assert solve([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]) is True
    assert solve(None, []) is False
    assert solve([121, 144, 19, 161, 19, 144, 19, 11], [132, 14641, 20736, 361, 25921, 361, 20736, 361]) is False
