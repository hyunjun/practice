#   https://www.hackerrank.com/challenges/two-arrays


from collections import defaultdict

def twoArrays0(k, A, B):
    d, maxB = defaultdict(list), -float('inf')
    for i, b in enumerate(B):
        d[b].append(i)
        maxB = max(maxB, b)
    for a in A:
        t = k - a
        while t < maxB and t not in d:
            t += 1
        if t not in d or 0 == len(d[t]):
            return 'NO'
        d[t].pop()
    return 'YES'

def twoArrays(k, A, B):
    sortedA, sortedB = sorted(A), sorted(B, reverse=True)
    for i, a in enumerate(sortedA):
        if a + sortedB[i] < k:
            return 'NO'
    return 'YES'


data = [(10, [2, 1, 3], [7, 8, 9], 'YES'),
        (5, [1, 2, 2, 1], [3, 3, 3, 4], 'NO'),
        ]
for k, A, B, expected in data:
    real = twoArrays(k, A, B)
    print('{}, {}, {}, expected {}, real {}, result {}'.format(k, A, B, expected, real, expected == real))
