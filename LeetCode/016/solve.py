# Problem comes from LeetCode https://leetcode.com/problems/number-of-1-bits/
# Solved on Wednesday May 25th, 2022

"""
    Given a 32-bit signed integer, return the number of ones in the binary representation.
"""


def solve(num: int) -> int:
    return bin(num).count('1')


if __name__ == '__main__':
    assert solve(11) == 3
    assert solve(64) == 1
    assert solve(534520) == 10
