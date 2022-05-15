# Problem from CodeWars https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/python
# Solved on Sunday May 15th, 2022

"""
Given a string, return the first non-repeating character. For example, the first non-repeating character in "stress" is "t".

This is case-insensitive when calculating repeating characters, but we return the original case of the first non-repeating character.
"""


def solve(s: str) -> str:
    for char in s:
        if s.lower().count(char.lower()) == 1:
            return char
    return ''


if __name__ == '__main__':
    assert solve('Stress') == 't'
    assert solve('sTreSS') == 'T'
    assert solve('AbbA') == ''
    assert solve('aaBbCcDdeEf') == 'f'
