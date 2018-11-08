#   https://www.hackerrank.com/challenges/candies


def candies(n, arr):
    res = []
    for i, a in enumerate(arr):
        if i == 0:
            res.append(1)
            continue
        if arr[i - 1] < a:
            res.append(res[i - 1] + 1)
        else:
            res.append(1)
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > arr[i + 1] and res[i] <= res[i + 1]:
            res[i] = res[i + 1] + 1
    return sum(res)


data = [([1, 2, 2], 4),  #  1, 2, 1
        ([2, 4, 2, 6, 1, 7, 8, 9, 2, 1], 19),  #  1, 2, 1, 2, 1, 2, 3, 4, 2, 1
        ([2, 4, 3, 5, 2, 6, 4, 5], 12),  #  1, 2, 1, 2, 1, 2, 1, 2
        ]
for arr, expected in data:
    real = candies(len(arr), arr)
    print('{}, expected {}, real {}, result {}'.format(arr, expected, real, expected == real))
