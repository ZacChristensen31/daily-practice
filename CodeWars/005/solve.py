# Problem comes from CodeWars https://www.codewars.com/kata/526571aae218b8ee490006f4/python
# Solved on Saturday May 14th, 2022

"""
Taking in a positive integer n, find the number of ones in the binary representation
"""


def solve(n: int) -> int:
    return bin(n).count('1')


if __name__ == '__main__':
    assert solve(0) == 0
    assert solve(1) == 1
    assert solve(2) == 1
    assert solve(9) == 2
    assert solve(15) == 4
