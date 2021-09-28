#   https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k


from collections import Counter
from typing import List


class Solution:
    #   runtime; 60ms, 93.85%
    #   memory; 14.1MB, 93.85%
    def countKDifference(self, nums: List[int], k: int) -> int:
        tot, d = 0, Counter(nums)
        for n, cnt in d.items():
            if n + k in d:
                tot += cnt * d[n + k]
        return tot


s = Solution()
data = [([1,2,2,1], 1, 4),
        ([1,3], 3, 0),
        ([3,2,1,5,4], 2, 3),
        ([10,2,10,9,1,6,8,9,2,8], 5, 1),
        ]
for nums, k, expect in data:
    real = s.countKDifference(nums, k)
    print(f'{nums} {k} expect {expect} real {real} result {expect == real}')
