

from typing import List


class Solution:
    #   https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/560/week-2-october-8th-october-14th/3494
    #   runtime; 32ms, 68.99%
    #   memory; 14MB
    def rob(self, nums: List[int]) -> int:
        if nums is None or 0 == len(nums):
            return 0
        if len(nums) < 3:
            return max(nums)

        def doRob(arr):
            if arr is None or 0 == len(arr):
                return 0
            if len(arr) <= 2:
                return max(arr)
            maxNum = 0
            for i in range(len(arr)):
                if i == 2:
                    arr[i] += arr[i - 2]
                elif i > 2:
                    arr[i] += max(arr[i - 2], arr[i - 3])
                maxNum = max(maxNum, arr[i])
            return maxNum

        return max(doRob(nums[:-1]), doRob(nums[1:]))


s = Solution()
data = [([2,3,2], 3),
        ([1,2,3,1], 4),
        ([0], 0),
        ([1], 1),
        ([1,3,1,3,100], 103),
        ([2,1,1,2], 3),
        ([200,3,140,20,10], 340),
        ]
for nums, expect in data:
    real = s.rob(nums)
    print(f'{nums} expect {expect} real {real} result {expect == real}')
