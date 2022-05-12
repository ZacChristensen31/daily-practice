# Problem comes from CodeWars https://www.codewars.com/kata/5552101f47fc5178b1000050/python
# Solved on Thursday May 12th, 2022

def solve(n: int, p: int) -> int:
    total = sum([int(x) ** (p + i) for i, x in enumerate(str(n))])
    return total / n if total % n == 0 else -1


if __name__ == '__main__':
    assert solve(89, 1) == 1
    assert solve(695, 2) == 2
    assert solve(46288, 3) == 51
    assert solve(92, 1) == -1
