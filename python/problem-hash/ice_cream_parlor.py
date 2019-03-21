#   https://www.hackerrank.com/challenges/ctci-ice-cream-parlor


from collections import defaultdict

def whatFlavors(cost, money):
    d = defaultdict(list)
    for i, c in enumerate(cost):
        d[c].append(i)
    for i, c in enumerate(cost):
        t = money - c
        if t in d:
            for j in d[t]:
                if i == j:
                    continue
                return [i + 1, j + 1]
    return [None, None]


data = [([1, 4, 5, 3, 2], 4, [1, 4]),
        ([2, 2, 4, 3], 4, [1, 2]),
        ]
for cost, money, expected in data:
    real = whatFlavors(cost, money)
    print('{}, {}, expected {}, real {}, result {}'.format(cost, money, expected, real, expected == real))
