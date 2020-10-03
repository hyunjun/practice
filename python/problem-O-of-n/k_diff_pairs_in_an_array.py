#   https://leetcode.com/problems/k-diff-pairs-in-an-array


from collections import Counter
from typing import List


class Solution:
    #   runtime; 76ms, 99.09%
    def findPairs0(self, nums, k):
        if nums is None or 0 == len(nums) or k < 0:
            return 0

        d, resSet = {}, set()
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        for n, cnt in d.items():
            if 0 == k:
                if 1 < cnt:
                    resSet.add((n, n))
            else:
                if n - k in d:
                    smaller, bigger = min(n - k, n), max(n - k, n)
                    resSet.add((smaller, bigger))
                if n + k in d:
                    smaller, bigger = min(n, n + k), max(n, n + k)
                    resSet.add((smaller, bigger))

        return len(resSet)

    #   https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3482
    #   runtime; 80ms, 98.90%
    #   memory; 15.5MB, 42.53%
    def findPairs(self, nums: List[int], k: int) -> int:
        if nums is None or 0 == len(nums) or k < 0:
            return 0

        res, c = 0, Counter(nums)
        for n, cnt in c.items():
            if k == 0:
                res += 1 if 1 < cnt else 0
            else:
                res += 1 if 0 < min(cnt, c[n + k]) else 0
        return res


s = Solution()
data = [([3, 1, 4, 1, 5], 2, 2),
        ([1, 2, 3, 4, 5], 1, 4),
        ([1, 3, 1, 5, 4], 0, 1),
        ([1, 2, 3, 4, 5], -1, 0),
        ([1, 1, 1, 2, 2], 1, 1),
        ]
for nums, k, expected in data:
    real = s.findPairs(nums, k)
    print(f'{nums}, {k}, expected {expected}, real {real}, result {expected == real}')
