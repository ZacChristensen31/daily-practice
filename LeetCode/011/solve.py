# Problem comes from LeetCode https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
# Solved on Friday May 20th, 2022

"""
    Given a strins s and an interger k, remove all consecutive strings or k or more letters, then recombine the remaining
    string. Repeat until this cannot be done anymore, then return the resulting string.

    For example:
        s = "deeedbbcccbdaa" and k = 3 would return 'aa'
        s = 'abcd' and k = 2 would return 'abcd'
        s = 'pbbcggttciiippooaais' and k = 2 would return 'ps'
"""

def solve(s: str, k: int) -> str:
    stack = []
    for char in s:
        if stack and stack[-1][0] == char:
            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append([char, 1])

    return ''.join(char * count for char, count in stack)

if __name__ == '__main__':
    assert solve('deeedbbcccbdaa', 3) == 'aa'
    assert solve('abcd', 2) == 'abcd'
    assert solve('pbbcggttciiippooaais', 2) == 'ps'