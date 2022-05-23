# Problem comes from CodeWars https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/train/python
# Solved on Sunday May 22nd, 2022

from typing import List

"""
    Given a sorted list of numbers, return a string denoting the ranges of the numbers. For example, [1, 2, 3] would
    return 1-3, while [1, 2, 3, 5, 7, 8, 9] would return '1-3,5,7-9'. If the list has only one number, return that
    number. If a range only has two numbers, those numbers are separated. For example, [1, 3, 4, 6] would return 
    '1,2,3,4'
"""

def solve(nums: List[int]) -> str:
    if len(nums) == 0:
        return ''

    start, end = None, None
    ranges = []

    for i in nums:
        if start is None:
            start = end = i
            continue
        elif i != end + 1:
            if start == end:
                ranges.append(str(end))
            elif end - start == 1:
                ranges.append(str(start))
                ranges.append(str(end))
            else:
                ranges.append(f'{start}-{end}')
            start = end = i
        else:
            end = i

    if start == end:
        ranges.append(str(end))
    elif end - start == 1:
        ranges.append(str(start))
        ranges.append(str(end))
    else:
        ranges.append(f'{start}-{end}')

    return ','.join(ranges)

if __name__ == '__main__':
    assert solve([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]) == '-6,-3-1,3-5,7-11,14,15,17-20'
    assert solve([-3,-2,-1,2,10,15,16,18,19,20]) == '-3--1,2,10,15,16,18-20'
    assert solve([]) == ''
