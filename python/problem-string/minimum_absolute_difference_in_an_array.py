#   https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array


def minimumAbsoluteDifference(arr):
    sortedArr, minDiff = sorted(arr), float('inf')
    for i, a in enumerate(sortedArr):
        if 0 == i:
            continue
        minDiff = min(minDiff, abs(a - sortedArr[i - 1]))
    return minDiff


data = [([3, -7, 0], 3),
        ([-59, -36, -13, 1, -53, -92, -2, -96, -54, 75], 1),
        ([1, -3, 71, 68, 17], 3),
        ]
for arr, expected in data:
    real = minimumAbsoluteDifference(arr)
    print('{}, expected {}, real {}, result {}'.format(arr, expected, real, expected == real))
