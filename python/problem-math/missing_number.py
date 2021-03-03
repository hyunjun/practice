#   https://leetcode.com/problems/missing-number

#   https://leetcode.com/problems/missing-number/solution


from typing import List


class Solution:
    #   40.62%
    def missingNumber0(self, nums):
        if nums is None or 0 == len(nums):
            return None
        maxNum = nums[0]
        for n in nums:
            if maxNum < n:
                maxNum = n
        allNums = list(range(maxNum + 1))
        for n in nums:
            allNums[n] = None
        for i in allNums:
            if i or 0 == i:
                return i
        return maxNum + 1

    #   https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3659
    #   runtime: 128ms, 81.32%
    #   memory: 16.5MB
    def missingNumber1(self, nums: List[int]) -> int:
        maxNum = len(nums)
        expectSet, realSet = set(i for i in range(maxNum)), set(nums)
        if len(expectSet - realSet) == 0:
            return maxNum
        return list(expectSet - realSet)[0]

    #   runtime: 124ms, 91.29%
    #   memory: 16.5MB
    def missingNumber(self, nums: List[int]) -> int:
        maxNum = len(nums)
        diffSet = set(i for i in range(maxNum)) - set(nums)
        if len(diffSet) == 0:
            return maxNum
        return list(diffSet)[0]


s = Solution()
data = [([0], 1),
        ([2], 0),
        ([0, 1], 2),
        ([3, 0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
        ]
for nums, expect in data:
    real = s.missingNumber(nums)
    print(f'{nums}, expect {expect}, real {real}, result {expect == real}')
