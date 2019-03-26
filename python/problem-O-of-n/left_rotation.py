#   https://www.hackerrank.com/challenges/ctci-array-left-rotation
#   https://www.hackerrank.com/challenges/array-left-rotation


def rotLeft0(a, d):
    return a[d:] + a[:d]


def rotLeft(a, d):
    def swapRange(arr, _from, _to):
        l, r = _from, _to
        while l < r:
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1
    #   reverse from 0~d - 1
    swapRange(a, 0, d - 1)
    #   reverse from d~len(a) - 1
    swapRange(a, d, len(a) - 1)
    #   reverse from 0~len(a) - 1
    swapRange(a, 0, len(a) - 1)
    return a


def rotate(arr, d):
    for l, r in [(0, d - 1), (d, len(arr) - 1), (0, len(arr) - 1)]:
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
    return arr


data = [([1, 2, 3, 4, 5], 2, [3, 4, 5, 1, 2]),
        ([1, 2, 3, 4, 5], 4, [5, 1, 2, 3, 4]),
        ]
for a, d, expected in data:
    real = rotLeft(a, d)
    print('{}, {}, expected {}, real {}, result {}'.format(a, d, expected, real, expected == real))
'''
1 2 3 4 5
2 1 5 4 3
3 4 5 1 2

1 2 3 4 5
4 3 2 1 5
5 1 2 3 4
'''
