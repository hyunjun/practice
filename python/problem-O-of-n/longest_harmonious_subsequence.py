#   https://leetcode.com/problems/longest-harmonious-subsequence

#   https://leetcode.com/problems/longest-harmonious-subsequence/solution


from collections import defaultdict
from typing import List


class Solution:
    #   55.60%
    def findLHS0(self, nums):
        d = {}
        for i, n in enumerate(nums):
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        maxLen = 0
        for n, cnt in d.items():
            if n - 1 in d:
                maxLen = max(maxLen, cnt + d[n - 1])
            if n + 1 in d:
                maxLen = max(maxLen, cnt + d[n + 1])
        return maxLen

    #   https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3628
    #   runtime; 484ms, 8.46%
    #   memory; 17.5MB
    def findLHS(self, nums: List[int]) -> int:
        if nums is None or 0 == len(nums):
            return 0
        d = defaultdict(list)
        for i, n in enumerate(nums):
            d[n].append(i)
        l, maxLen = sorted(d.items()), 0
        for i, (k, idxList) in enumerate(l):
            if 0 == i:
                continue
            if k - l[i - 1][0] == 1:
                maxLen = max(maxLen, len(idxList) + len(l[i - 1][1]))
        return maxLen


s = Solution()
data = [([1, 3, 2, 2, 5, 2, 3, 7], 5),
        ([1, 2, 3, 4], 2),
        ([1, 1, 1, 1], 0),
        ]
for nums, expect in data:
    real = s.findLHS(nums)
    print(f'{nums} expect {expect}, real {real}, result {expect == real}')
