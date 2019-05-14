#   https://www.educative.io/collection/page/5668639101419520/5671464854355968/4578892830474240

def smallest_subarray_with_given_sum0(s, arr):
    if arr is None or 0 == len(arr):
        return 0

    def getMaxSubsumWithLength(k):
        maxSubsum, subsum = -float('inf'), 0
        for i, a in enumerate(arr):
            if k <= i:
                subsum -= arr[i - k]
            subsum += a
            if k - 1 <= i:
                maxSubsum = max(maxSubsum, subsum)
        return maxSubsum

    for i in range(1, len(arr) + 1):
        if s <= getMaxSubsumWithLength(i):
            return i
    return 0

def smallest_subarray_with_given_sum(s, arr):
    if arr is None or 0 == len(arr):
        return 0

    i, subsum, minLen = 0, 0, float('inf')
    for j in range(len(arr)):
        subsum += arr[j]
        while s <= subsum:
            minLen = min(minLen, j - i + 1)
            subsum -= arr[i]
            i += 1
    if minLen == float('inf'):
        return 0
    return minLen


data = [(7, [2, 1, 5, 2, 3, 2], 2),
        (7, [2, 1, 5, 2, 8], 1),
        (8, [3, 4, 1, 1, 6], 3),
        ]
for s, arr, expected in data:
    real = smallest_subarray_with_given_sum(s, arr)
    print('{}, {}, expected {}, real {}, result {}'.format(s, arr, expected, real, expected == real))
