#   https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum


from typing import List


class Solution:
    #   runtime; 48ms, 29.06%
    #   memory; 13.9MB, 100.00%
    def minStartValue(self, nums: List[int]) -> int:
        if nums is None or not (1 <= len(nums) <= 100):
            return 0
        curSum, maxNegative = 0, 0
        for n in nums:
            curSum += n
            maxNegative = min(maxNegative, curSum)
        return -maxNegative + 1


s = Solution()
data = [([-3, 2, -3, 4, 2], 5),
        ([1, 2], 1),
        ([1, -2, -3], 5),
        ]
for nums, expected in data:
    real = s.minStartValue(nums)
    print(f'{nums} expected {expected} real {real} result {expected == real}')
