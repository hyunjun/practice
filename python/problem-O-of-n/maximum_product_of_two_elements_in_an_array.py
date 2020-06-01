#   https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array


from typing import List


class Solution:
    #   runtime; 56ms, 87.56%
    #   memory; 14MB, 100.00%
    def maxProduct0(self, nums: List[int]) -> int:
        if nums is None or not (2 <= len(nums) <= 500):
            return float('-inf')
        max1st, max2nd = nums[0], nums[1]
        if max1st < max2nd:
            max1st, max2nd = max2nd, max1st
        for i in range(2, len(nums)):
            if max1st < nums[i]:
                max2nd, max1st = max1st, nums[i]
            elif max1st == nums[i] or max2nd < nums[i]:
                max2nd = nums[i]
        return (max1st - 1) * (max2nd - 1)

    #   runtime; 56ms, 87.56%
    #   memory; 14MB, 100.00%
    def maxProduct(self, nums: List[int]) -> int:
        if nums is None or not (2 <= len(nums) <= 500):
            return float('-inf')
        max2nd, max1st = sorted(nums)[-2:]
        return (max1st - 1) * (max2nd - 1)


s = Solution()
data = [([3, 4, 5, 2], 12),
        ([1, 5, 4, 5], 16),
        ([3, 7], 12),
        ([10, 2, 5, 2], 36),
        ]
for nums, expect in data:
    real = s.maxProduct(nums)
    print(f'{nums} expect {expect} real {real} result {expect == real}')
