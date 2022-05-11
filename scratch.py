from collections import Counter

def solve():
    start = [1, 1, 1, 1, 1]

    for _ in range(1, 33):
        new_start = []
        for index, value in enumerate(start[::-1]):
            if index == 0:
                new_start.append(value)
            else:
                new_start = [new_start[0] + value, *new_start]
        start = new_start

    return sum(start)

# Counter({'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1})
# 5

# Counter({'a': 5, 'e': 4, 'i': 3, 'o': 2, 'u': 1})
# 15

# Counter({'a': 15, 'e': 10, 'i': 6, 'o': 3, 'u': 1})
# 35

# Counter({'a': 35, 'e': 20, 'i': 10, 'o': 4, 'u': 1})
# 70

# Counter({'a': 70, 'e': 35, 'i': 15, 'o': 5, 'u': 1})
# 126



if __name__ == '__main__':
    print(solve())