#   https://leetcode.com/problems/number-of-good-pairs


from collections import Counter
from typing import List


class Solution:
    #   runtime; 28ms, 100.00%
    #   memory; 14MB, 100.00%
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(c * (c - 1) // 2 for c in Counter(nums).values())


s = Solution()
data = [([1, 2, 3, 1, 1, 3], 4),
        ([1, 1, 1, 1], 6),
        ([1, 2, 3], 0),
        ]
for nums, expect in data:
    real = s.numIdenticalPairs(nums)
    print(f'{nums} expect {expect} real {real} result {expect == real}')
