# Problem comes from CodeWars https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/python
# Solved on Tuesday May 24th, 2022

from itertools import permutations
from typing import List

"""
    Given a string, return all unique permutations of the characters in the string
"""

def solve(s: str) -> List[str]:
    return [''.join(x) for x in list(set(permutations(s)))]

if __name__ == '__main__':
    target_solve = solve

    assert sorted(target_solve('a')) == ['a']
    assert sorted(target_solve('ab')) == ['ab', 'ba']
    assert sorted(target_solve('aabb')) == ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']