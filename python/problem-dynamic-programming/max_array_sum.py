#   https://www.hackerrank.com/challenges/max-array-sum


def maxSubsetSum(arr):
    if arr is None or 0 == len(arr):
        return 0
    if len(arr) < 3:
        return max(arr)
    dp = [0] * len(arr)
    dp[0], dp[1] = arr[0], max(arr[0:2])
    for i in range(2, len(arr)):
        if dp[i - 2] > 0:
            dp[i] = arr[i] + dp[i - 2]
        else:
            dp[i] = arr[i]
        dp[i] = max(dp[i], dp[i - 1])
    return dp[-1]


data = [([-2, 1, 3, -4, 5], 8),
        ([3, 7, 4, 6, 5], 13),
        ([2, 1, 5, 8, 4], 11),
        ([3, 5, -7, 8, 10], 15),
        ]
for arr, expected in data:
    real = maxSubsetSum(arr)
    print('{}, expected {}, real {}, result {}'.format(arr, expected, real, expected == real))
'''
f(n) = max(arr[n] + f(n - 2) if f(n - 2) > 0 else arr[n], f(n - 1))
...
f(3) = arr[3] + f(1) if f(1) > 0 else arr[3]
f(2) = max(arr[2] + f(0) if f(0) > 0 else arr[2], f(1))
f(1) = max(arr[0:2])
f(0) = arr[0]
'''
