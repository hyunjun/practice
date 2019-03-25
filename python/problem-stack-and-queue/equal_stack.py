#   https://www.hackerrank.com/challenges/equal-stacks


from collections import defaultdict

def equalStacks(h1, h2, h3):
    d, s1, s2, s3 = defaultdict(list), sum(h1), sum(h2), sum(h3)
    for i, h in enumerate(h1):
        d[s1].append(i)
        s1 -= h
    for i, h in enumerate(h2):
        d[s2].append(i)
        s2 -= h
    for i, h in enumerate(h3):
        d[s3].append(i)
        s3 -= h
    for hSum, indices in d.items():
        if 3 == len(indices):
            return hSum
    return 0


data = [([3, 2, 1, 1, 1], [4, 3, 2], [1, 1, 4, 1], 5),
        ]
for h1, h2, h3, expected in data:
    real = equalStacks(h1, h2, h3)
    print('{}, {}, {}, expected {}, real {}, result {}'.format(h1, h2, h3, expected, real, expected == real))
