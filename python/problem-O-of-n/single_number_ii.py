#   https://leetcode.com/problems/single-number-ii


from collections import Counter
from typing import List


class Solution:
    #   runtime; 52ms, 92.93%
    #   memory; 15.5MB, 6.67%
    def singleNumber0(self, nums: List[int]) -> int:
        if nums is None or 0 == len(nums):
            return 0
        return [k for k, v in Counter(nums).items() if v == 1][0]

    def singleNumber(self, nums: List[int]) -> int:
        if nums is None or 0 == len(nums):
            return 0
        return [k for k, v in Counter(nums).items() if v == 1][0]


s = Solution()
data = [([2, 2, 3, 2], 3),
        ([0, 1, 0, 1, 0, 1, 99], 99),
        ]
for nums, expected in data:
    real = s.singleNumber(nums)
    print(f'{nums} expected {expected} real {real} result {expected == real}')
