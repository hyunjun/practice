#   https://leetcode.com/problems/set-mismatch

#   https://leetcode.com/problems/set-mismatch/solution


from collections import Counter
from typing import List


class Solution:
    #   8.33%
    def findErrorNums0(self, nums):
        if nums is None or 0 == len(nums):
            return []
        d, maxVal = {}, nums[0]
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
            maxVal = max(maxVal, n)
        twice, missing = None, None
        for i in range(1, maxVal + 1):
            if 1 < d.get(i, 0):
                twice = i
            elif i not in d:
                missing = i
        if missing is None:
            missing = maxVal + 1
        return [twice, missing]

    #   https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3658
    #   runtime: 188ms, 82.20%
    #   memory: 16MB, 31.95%
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c, duplicated, missing = Counter(nums), -1, -1
        for i in range(1, len(nums) + 1):
            if i not in c:
                missing = i
            elif c[i] > 1:
                duplicated = i
        return [duplicated, missing]


s = Solution()
data = [([1, 2, 2, 4], [2, 3]),
        ([1, 1], [1, 2]),
        ([2, 2], [2, 1]),
        ([3, 2, 2], [2, 1]),
        ]
for nums, expected in data:
    real = s.findErrorNums(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
