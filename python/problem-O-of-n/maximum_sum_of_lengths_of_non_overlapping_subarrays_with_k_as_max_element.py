#   https://www.codela.io/challenges/5a5ddbbd9934dfb3614af732/maximum-sum-of-lengths-of-non-overlapping-subarrays-with-k-as-max-element


def solution(arr, num):
    if arr is None or 0 == len(arr):
        return 0
    s, e, cnt, hasNum = 0, 0, 0, False
    for i, a in enumerate(arr):
        if num < a:
            if hasNum:
                cnt += e - s + 1
            hasNum = False
            s = e = i + 1
        else:
            e = i
            if a == num:
                hasNum = True
    if s < e < len(arr) and hasNum:
        cnt += e - s + 1
    return cnt


data = [([2, 1, 4, 9, 2, 3, 8, 3, 4], 4, 5),
        ([1, 2, 3, 2, 3, 4, 1], 4, 7),
        ]
for arr, num, expected in data:
    real = solution(arr, num)
    print('{}, {}, expected {}, real {}, result {}'.format(arr, num, expected, real, expected == real))
