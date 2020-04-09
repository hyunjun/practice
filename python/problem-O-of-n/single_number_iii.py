#   https://leetcode.com/problems/single-number-ii


from collections import Counter
from functools import reduce
from typing import List


class Solution:
    #   runtime; 56ms, 89.36%
    #   memory; 15.5MB, 50.00%
    def singleNumber(self, nums: List[int]) -> int:
        if nums is None or 0 == len(nums):
            return 0
        return [k for k, v in Counter(nums).items() if v == 1]


s = Solution()
data = [([1, 2, 1, 3, 2, 5], [3, 5])
        ]
for nums, expected in data:
    real = s.singleNumber(nums)
    print(f'{nums} expected {expected} real {real} result {sorted(expected) == sorted(real)}')
