#   https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order


from collections import defaultdict
from typing import List


class Solution:
    #   runtime; 156ms, 8.04%
    #   memory; 14MB, 100.00%
    def minSubsequence0(self, nums: List[int]) -> List[int]:
        if nums is None or not (1 <= len(nums) <= 500):
            return []
        r, sortedNums, s = [], sorted(nums, reverse=True), sum(nums)
        while sum(r) <= sum(sortedNums):
            r.append(sortedNums.pop(0))
        return r

    #   runtime; 56ms, 93.50%
    #   memory; 14MB, 100.00%
    def minSubsequence(self, nums: List[int]) -> List[int]:
        if nums is None or not (1 <= len(nums) <= 500):
            return []
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        r, rSum, s = [], 0, sum(nums)
        for n in range(100, 0, -1):
            if rSum > s:
                break
            while d[n] > 0 and rSum <= s:
                r.append(n)
                rSum += n
                s -= n
                d[n] -= 1
        return r


s = Solution()
data = [([4, 3, 10, 9, 8], [10, 9]),
        ([4, 4, 7, 6, 7], [7, 7, 6]),
        ([6], [6]),
        ([4, 3, 9, 10, 8, 1, 2, 9, 3], [10, 9, 9]),
        ]
for nums, expected in data:
    real = s.minSubsequence(nums)
    print(f'{nums} expected {expected} real {real} result {expected == real}')
