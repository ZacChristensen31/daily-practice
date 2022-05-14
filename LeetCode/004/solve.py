# Problem comes from LeetCode https://leetcode.com/problems/roman-to-integer/
# Solved on Friday May 13th, 2022

def solve(s: str) -> int:
    sub_dict = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }

    total = 0

    for k, v in sub_dict.items():
        if k in s:
            s = s.replace(k, '')
            total += v
    num_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    for k, v in num_dict.items():
        foobar = s.count(k)
        total += foobar * v

    return total


if __name__ == '__main__':
    assert solve('III') == 3
    assert solve('IV') == 4
    assert solve('IX') == 9
    assert solve('LVIII') == 58
    assert solve('MCMXCIV') == 1994
