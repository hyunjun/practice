#   https://leetcode.com/problems/maximum-difference-between-increasing-elements


from typing import List


class Solution:
    #   runtime; 44ms, 94.20%
    #   memory; 14.3MB, 89.54%
    def maximumDifference(self, nums: List[int]) -> int:
        if nums is None or 0 == len(nums):
            return -1

        diff = -1
        _max = _min = nums[0]
        for n in nums:
            if _max < n:
                _max = n
                diff = max(diff, _max - _min)
            elif n < _min:
                _max = _min = n

        return diff


s = Solution()
data = [([7, 1, 5, 4], 4),
        ([9, 4, 3, 2], -1),
        ([1, 5, 2, 10], 9),
        ]
for nums, expect in data:
    real = s.maximumDifference(nums)
    print(f'{nums} expect {expect} real {real} result {expect == real}')
