#   https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x


from typing import List


class Solution:
    #   runtime; 44ms, 58.20%
    #   memory; 14.1MB, 78.37%
    def specialArray(self, nums: List[int]) -> int:
        for x in range(len(nums) + 1):
            if len([n for n in nums if x <= n]) == x:
                return x
        return -1


s = Solution()
data = [([3,5], 2),
        ([0,0], -1),
        ([0,4,3,0,4], 3),
        ([3,6,7,7,0], -1),
        ]
for nums, expect in data:
    real = s.specialArray(nums)
    print(f'{nums} expect {expect} real {real} result {expect == real}')
