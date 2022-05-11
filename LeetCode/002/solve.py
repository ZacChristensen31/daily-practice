# Problem comes from LeetCode https://leetcode.com/problems/combination-sum-iii/
# Completed Wednesday May 11th, 2022
from itertools import combinations
from typing import List, Tuple


def solve(k: int, n: int) -> List[Tuple[int]]:
    print(list(filter(lambda x: sum(x) == n, set(combinations([i for i in range(1, 10)], k)))))
    return list(filter(lambda x: sum(x) == n, set(combinations([i for i in range(1, 10)], k))))


if __name__ == '__main__':
    for possible in solve(3, 9):
        assert possible in [(1, 2, 6), (1, 3, 5), (2, 3, 4)]

    assert solve(4, 1) == []

    assert solve(3, 7) == [(1, 2, 4)]
