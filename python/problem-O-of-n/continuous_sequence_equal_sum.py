#   continuous sequence of array that sums up to exactly T


def continuous_sequence(A, T):
    s, e, _sum = -1, -1, 0
    for i, a in enumerate(A):
        if T < a:
            s, e, _sum = -1, -1, 0
            continue
        _sum += a
        if s == e == -1:
            s = i
        e = i
        while T < _sum:
            _sum -= A[s]
            s += 1
        if T == _sum:
            return [s, e]
    return []


data = [([23, 5, 4, 7, 2, 11], 20, [3, 5]),
        ([1, 3, 5, 23, 2], 8, [1, 2]),
        ([1, 3, 5, 23, 2], 7, []),
        ]
for A, T, expected in data:
    real = continuous_sequence(A, T)
    print('{}, {}, expected {}, real {}, result {}'.format(A, T, expected, real, expected == real))
