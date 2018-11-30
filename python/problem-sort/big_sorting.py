#   https://www.hackerrank.com/challenges/big-sorting/problem


#   timeout
def bigSorting0(unsorted):
    return [str(s) for s in sorted([int(u) for u in unsorted])]


def bigSorting(unsorted):
    sortedByLen = sorted(unsorted, key=lambda u: len(u))
    idx, res = 0, []
    for i, s in enumerate(sortedByLen):
        if 0 == i:
            continue
        if len(sortedByLen[i - 1]) != len(sortedByLen[i]):
            res.extend(sorted(sortedByLen[idx:i], key=lambda s: int(s)))
            idx = i
    res.extend(sorted(sortedByLen[idx:], key=lambda s: int(s)))
    return res


data = [(['31415926535897932384626433832795', '1', '3', '10', '3', '5'], ['1', '3', '3', '5', '10', '31415926535897932384626433832795']),
        (['1', '2', '100', '12303479849857341718340192371', '3084193741082937', '3084193741082938', '111', '200'], ['1', '2', '100', '111', '200', '3084193741082937', '3084193741082938', '12303479849857341718340192371']),
        (['11', '123', '10', '122', '9', '0', '4'], ['0', '4', '9', '10', '11', '122', '123']),
        ]
for unsorted, expected in data:
    real = bigSorting(unsorted)
    print(real)
    print('result {}'.format(expected == real))
