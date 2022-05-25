# Problem comes from CodeWars https://www.codewars.com/kata/56269eb78ad2e4ced1000013/train/python
# Solved on Monday May 23rd, 2022

from math import sqrt, floor

"""
    Given a number n, return -1 if the number is not a square. If it is a perfect square, return the next perfect square.
"""

def solve(n: int) -> int:
    return -1 if sqrt(n) != floor(sqrt(n)) else (sqrt(n) + 1) ** 2



if __name__ == '__main__':
    assert solve(1) == 4
    assert solve(121) == 144
    assert solve(2) == -1