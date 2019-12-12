

from typing import List


class Solution:
    def maxSubSumArray(self, arr: List[int]) -> int:
        if arr is None or 0 == len(arr):
            return 0
        if 1 == len(arr):
            return arr[0]
        maxSum, subSum = 0, [0] * len(arr)
        for i, a in enumerate(arr):
            curSum = subSum[i - 1] + a
            if curSum <= 0:
                continue
            subSum[i] = curSum
            maxSum = max(maxSum, curSum)
        return maxSum


s = Solution()
data = [([-2, -3, 4, -1, -2, 1, 5, -3], 7),
        ]
for arr, expected in data:
    real = s.maxSubSumArray(arr)
    print(f'{arr} expected {expected} real {real} result {expected == real}')
