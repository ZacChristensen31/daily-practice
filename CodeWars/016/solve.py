# Problem comes from CodeWars https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5/train/python
# Solved on Wednesday May 25th, 2022

"""
    Given a string s, return the number value of the string displayed
"""


def solve(s: str) -> int:
    if 'million' in s:
        return 1000000

    nums = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7,
        'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14,
        'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20,
        'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90,
        'hundred': 100, 'thousand': 1000,
    }

    and_removed = s.replace(' and ', ' ')
    words = and_removed.split()

    total = 0
    current = 0

    for word in words:
        if word == 'thousand':
            total += current * 1000
            current = 0
        elif word == 'hundred':
            current = 100 * current if current > 0 else 100
        elif '-' in word:
            tens, ones = word.split('-')
            current += nums[tens] + nums[ones]
        else:
            current += nums[word]

    return total + current


if __name__ == '__main__':
    assert solve('one') == 1
    assert solve('twenty') == 20
    assert solve('two hundred forty-six') == 246
    assert solve('seven hundred eighty-three thousand nine hundred and nineteen') == 783919
