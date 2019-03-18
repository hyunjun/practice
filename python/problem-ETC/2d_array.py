#   https://www.hackerrank.com/challenges/2d-array


def hourglassSum(arr):
    if arr is None or 0 == len(arr) or 0 == len(arr[0]):
        return 0
    _sum, ROW, COL = -float('inf'), len(arr), len(arr[0])
    for r in range(ROW - 2):
        for c in range(COL - 2):
            _sum = max(_sum, sum(arr[r][c:c + 3]) + arr[r + 1][c + 1] + sum(arr[r + 2][c:c + 3]))
    return _sum


data = [([[-9, -9, -9, 1, 1, 1],
          [0, -9, 0, 4, 3, 2],
          [-9, -9, -9, 1, 2, 3],
          [0, 0, 8, 6, 6, 0],
          [0, 0, 0, -2, 0, 0],
          [0, 0, 1, 2, 4, 0]], 28),
        ([[1, 1, 1, 0, 0, 0],
          [0, 1, 0, 0, 0, 0],
          [1, 1, 1, 0, 0, 0],
          [0, 0, 2, 4, 4, 0],
          [0, 0, 0, 2, 0, 0],
          [0, 0, 1, 2, 4, 0]], 19),
        ]
for arr, expected in data:
    real = hourglassSum(arr)
    print('{}, expected {}, real {}, result {}'.format(arr, expected, real, expected == real))
