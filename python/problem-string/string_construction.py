#   https://www.hackerrank.com/challenges/string-construction


def stringConstruction(s):
    return len(set(s))


data = [('abcd', 4),
        ('abab', 2),
        ('aaa', 1),
        ('abcab', 3),
        ('abcbc', 3),
        ('abcbcab', 3),
        ]
for s, expected in data:
    real = stringConstruction(s)
    print('{}, expected {}, real {}, result {}'.format(s, expected, real, expected == real))
