#   https://www.educative.io/collection/page/5668639101419520/5671464854355968/5177043027230720


def max_sum_subarray(nums, k):
    if nums is None or 0 == len(nums) or len(nums) < k:
        return 0
    maxSum, curSum = -float('inf'), 0
    for i, n in enumerate(nums):
        if k <= i:
            curSum -= nums[i - k]
        curSum += n
        if k - 1 <= i:
            maxSum = max(maxSum, curSum)
    return maxSum


data = [([2, 1, 5, 1, 3, 2], 3, 9),
        ([2, 3, 4, 1, 5], 2, 7),
        ]
for nums, k, expected in data:
    real = max_sum_subarray(nums, k)
    print('{}, {}, expected {}, real {}, result {}'.format(nums, k, expected, real, expected == real))
