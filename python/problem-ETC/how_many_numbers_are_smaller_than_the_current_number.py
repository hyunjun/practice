#   https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number


from collections import defaultdict
from typing import List


class Solution:
    #   runtime; 60ms, 63.01%
    #   memory; 13.8MB, 100.00%
    def smallerNumbersThanCurrent0(self, nums: List[int]) -> List[int]:
        if nums is None or not (2 <= len(nums) <= 500):
            return []
        sortedNums, result = sorted([(i, n) for i, n in enumerate(nums)], key=lambda t: t[1]), [None] * len(nums)
        for cnt, (i, n) in enumerate(sortedNums):
            if 0 < cnt and n == sortedNums[cnt - 1][1]:
                result[i] = result[sortedNums[cnt - 1][0]]
            else:
                result[i] = cnt
        return result

    #   runtime; 56ms, 72.91%
    #   memory; 14.1MB, 100.00%
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        if nums is None or not (2 <= len(nums) <= 500):
            return []
        counts, result = [0] * 102, [None] * len(nums)
        for n in nums:
            counts[n] += 1
        prev = 0
        for i, c in enumerate(counts[:max(nums) + 1]):
            counts[i] = prev
            prev += c
        for i, n in enumerate(nums):
            result[i] = counts[n]
        return result


s = Solution()
data = [([8, 1, 2, 2, 3], [4, 0, 1, 1, 3]),
        ([6, 5, 4, 8], [2, 1, 0, 3]),
        ([7, 7, 7, 7], [0, 0, 0, 0]),
        ([5, 0, 10, 0, 10, 6], [2, 0, 4, 0, 4, 3]),
        ]
for nums, expected in data:
    real = s.smallerNumbersThanCurrent(nums)
    print(f'{nums} expected {expected} real {real} result {expected == real}')
'''
    0   5   6  10
    0   2   3   4
p   0   2   3   4
t   2   3   4   6
p   2   3   4   6
'''
