#   https://leetcode.com/problems/first-missing-positive

#   https://leetcode.com/problems/first-missing-positive/discuss/871665/Python-O(n)-solution-without-additional-memory-explained
from typing import List


class Solution:
    #   Memory Error
    def firstMissingPositive0(self, nums: List[int]) -> int:
        if nums is None or 0 == len(nums):
            return 1
        maxNum = max(nums)
        exists = [False] * (maxNum + 1)
        for n in nums:
            if n <= 0:
                continue
            exists[n] = True
        for i in range(1, len(exists)):
            if not exists[i]:
                return i
        return maxNum + 1

    #   https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/558/week-5-september-29th-september-30th/3478
    #   runtime; 36ms, 67.86%
    #   memory; 13.9MB, 35.31%
    def firstMissingPositive(self, nums: List[int]) -> int:
        if nums is None or 0 == len(nums):
            return 1
        res, nums = 1, sorted(set(nums))
        for n in nums:
            if n <= 0:
                continue
            if res < n:
                break
            res += 1
        return res


s = Solution()
data = [([], 1),
        ([2], 1),
        ([1, 1], 2),
        ([1,2,0], 3),
        ([3,4,-1,1], 2),
        ([7,8,9,11,12], 1),
        ([2147483647], 1),
        ]
for nums, expect in data:
    real = s.firstMissingPositive(nums)
    print(f'{nums} expect {expect} real {real} result {expect == real}')
