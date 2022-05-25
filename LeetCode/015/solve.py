# Problem comes from LeetCode https://leetcode.com/problems/zigzag-conversion/
# Solved on Tuesday May 24th, 2022

def solve(s: str, num_rows: int) -> str:
    if num_rows == 1:
        return s

    curr_level = 0
    update = 1

    level_dict = {
        k: ''
        for k in range(num_rows)
    }

    for char in s:
        level_dict[curr_level] += char

        curr_level += update

        if curr_level == 0 or curr_level == num_rows - 1:
            update *= -1

    return ''.join([level_dict[x] for x in range(num_rows)])

if __name__ == '__main__':
    assert solve('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
    assert solve('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI'
    assert solve('AB', 1) == 'AB'