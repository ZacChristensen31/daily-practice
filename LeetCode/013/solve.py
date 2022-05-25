# Problem comes from LeetCode https://leetcode.com/problems/ones-and-zeroes/
# Solved on Sunday May 22nd, 2022

from typing import List

"""
    Given a list of binary strings, a max number of zeros m, and a max number of ones n, return the max number of strings
    you can select while staying under m and n.
"""


def solve(nums: List[str], m: int, n: int) -> int:
    # Set up a dp storing max number of ones and zeros
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Extract the number of ones and zeros from each string
    counts = [[x.count('0'), x.count('1')] for x in nums]

    # Loop through each of the counts
    for zero, one in counts:
        for i in range(m, zero - 1, -1):
            for j in range(n, one - 1, -1):
                dp[i][j] = max(dp[i][j], 1 + dp[i - zero][j - one])

    return dp[-1][-1]


if __name__ == '__main__':
    assert solve(["10", "0001", "111001", "1", "0"], 5, 3) == 4
    assert solve(["10", "0", "1"], 1, 1) == 2
