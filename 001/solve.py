# Problem comes from https://www.codewars.com/kata/5277c8a221e209d3f6000b56

"""
TLDR: Read in a string of braces (), [], and {}. If the string is valid, return true, otherwise return false.

Valid means that all braces are closed in the correct order.
"""


def solve(input_string: str) -> bool:
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    stack = []

    for char in input_string:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs.keys():
            if stack == [] or stack.pop() != pairs[char]:
                return False

    return stack == []


if __name__ == '__main__':
    assert solve('{}') is True
    assert solve('}') is False
    assert solve('[{}]') is True
    assert solve('[{}') is False
    assert solve('[{}]{') is False
    assert solve('[{}]{}') is True
    assert solve('{}[][]()[]{}()[]{}()') is True
