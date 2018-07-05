#   https://practice.geeksforgeeks.org/problems/cutting-binary-string/0


def cut_binary_string(s):
    if s is None or 0 == len(s) or '1' not in s:
        return -1
    if 0 == int(s, 2) % 5:
        return 1
    prev, result = -1, [0] * len(s)
    for i, c in enumerate(s):
        if '0' == c:
            continue
        result[i] = 1
        if -1 < prev and 0 == int(s[prev:i + 1], 2) % 5:
            result[prev] = 0
        prev = i
    print(result)
    return sum(result)


data = [('101101101', 3),   #   101101101 = 365 -> 1 vs. 101, 101, 101 = 5, 5, 5 -> 3
        ('1111101', 1),
        ('00000', -1),
        ('1101', 2),
        ]
for s, expected in data:
    real = cut_binary_string(s)
    print('{}, expected {}, real {}, result {}'.format(s, expected, real, expected == real))
