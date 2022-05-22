# Problem comes from CodeWars https://www.codewars.com/kata/546dba39fa8da224e8000467/python
# Solved on Friday May 20th, 2022

from typing import List

def solve(s: str) -> List[List[str or int]]:
    if s == '':
        return []

    curr = 0
    curr_char = s[0]
    output = []

    for char in s:
        if char != curr_char:
            output += [[curr, curr_char]]
            curr_char = char
            curr = 1
        else:
            curr += 1

    return output + [[curr, curr_char]]


if __name__ == '__main__':
    assert solve('aaabbbccc') == [[3, 'a'], [3, 'b'], [3, 'c']]
    assert solve('asdfasd') == [[1, 'a'], [1, 's'], [1, 'd'], [1, 'f'], [1, 'a'], [1, 's'], [1, 'd']]
    assert solve('') == []
    assert solve('a') == [[1, 'a']]
    assert solve('aa') == [[2, 'a']]
    assert solve('aafddsaa') == [[2, 'a'], [1, 'f'], [2, 'd'], [1, 's'], [2, 'a']]
