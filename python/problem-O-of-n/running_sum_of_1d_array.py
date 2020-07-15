#   https://leetcode.com/problems/running-sum-of-1d-array


from typing import List


class Solution:
    #   runtime; 32ms, 97.63%
    #   memory; 14.1MB, 33.33%
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums


s = Solution()
data = [([1,2,3,4], [1,3,6,10]),
        ([1,1,1,1,1], [1,2,3,4,5]),
        ([3,1,2,10,1], [3,4,6,16,17]),
        ]
for nums, expect in data:
    real = s.runningSum(nums)
    print(f'{nums} expect {expect} real {real} result {expect == real}')
