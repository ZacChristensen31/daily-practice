# Problem comes from LeetCode https://leetcode.com/problems/count-sorted-vowel-strings/
# Completed Tuesday May 10th, 2022

def solve(n: int) -> int:
    start = [1, 1, 1, 1, 1]

    for _ in range(1, n):
        new_start = []
        for index, value in enumerate(start[::-1]):
            if index == 0:
                new_start.append(value)
            else:
                new_start = [new_start[0] + value, *new_start]
        start = new_start

    return sum(start)


def clean_solve(n: int) -> int:
    rolling_sum = [1, 1, 1, 1, 1]

    for _ in range(1, n):
        for index in range(5):
            rolling_sum[index] = sum(rolling_sum[index:])

    return sum(rolling_sum)


if __name__ == '__main__':
    target_solve = clean_solve

    assert target_solve(1) == 5
    assert target_solve(2) == 15
    assert target_solve(3) == 35
    assert target_solve(4) == 70
    assert target_solve(33) == 66045
