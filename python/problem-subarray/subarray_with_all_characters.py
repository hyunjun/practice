#   https://www.geeksforgeeks.org/smallest-window-contains-characters-string


def subarray_with_all(string):
    if string is None or 0 == len(string):
        return ''
    minRange, minS, minE = len(string), 0, 0
    s, d = 0, {c: 0 for c in set(string)}
    for e, c in enumerate(string):
        d[c] += 1
        while 1 < d[string[s]]:
            d[string[s]] -= 1
            s += 1
        if all([0 < cnt for _, cnt in d.items()]):
            if e - s + 1 < minRange:
                minRange, minS, minE = e - s + 1, s, e
    return string[s:e + 1]


data = [('aabcbcdbca', 'dbca'),
        ('aaab', 'ab'),
        ('abaacabacd', 'bacd'),
        ]
for s, expected in data:
    real = subarray_with_all(s)
    print('{}, expected {}, real {}, result {}'.format(s, expected, real, expected == real))
