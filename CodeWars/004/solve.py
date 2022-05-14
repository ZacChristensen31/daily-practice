# Problem comes from CodeWars https://www.codewars.com/kata/52449b062fb80683ec000024/python
# Solved on Friday May 13th, 2022

def solve(s: str):
    if s == '':
        return False

    output = '#'

    capped = True

    for char in s:
        if char == ' ':
            capped = True
            continue
        if capped:
            output += char.upper()
            capped = False
        else:
            output += char.lower()

    return False if len(output) > 140 else output


if __name__ == '__main__':
    assert solve('Hello there thanks for trying my Kata') == '#HelloThereThanksForTryingMyKata'
    assert solve('lorEm IpSuM dOLor sIT AMET') == '#LoremIpsumDolorSitAmet'
    assert solve('') is False
