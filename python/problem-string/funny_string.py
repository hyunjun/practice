#   https://www.hackerrank.com/challenges/funny-string


def funnyString(s):
    if s is None or 0 == len(s):
        return 'Not Funny'
    diffs = []
    for i, c in enumerate(s):
        if 0 == i:
            continue
        diffs.append(abs(ord(s[i - 1]) - ord(c)))
    if diffs == diffs[::-1]:
        return 'Funny'
    return 'Not Funny'


data = [('acxz', 'Funny'),
        ('bcxz', 'Not Funny'),
        ('ivvkxq', 'Not Funny'),
        ('ivvkx', 'Not Funny'),
        ]
for s, expected in data:
    real = funnyString(s)
    print('{}, expected {}, real {}, result {}'.format(s, expected, real, expected == real))
