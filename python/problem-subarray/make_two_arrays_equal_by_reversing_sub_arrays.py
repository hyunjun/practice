#   https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays


from collections import Counter
from typing import List


class Solution:
    #   runtime; 76ms, 95.92%
    #   memory; 14MB, 100.00%
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if target is None or not (1 <= len(target) <= 1000) or arr is None or len(target) != len(arr):
            return False
        return Counter(target) == Counter(arr)


s = Solution()
data = [([1, 2, 3, 4], [2, 4, 1, 3], True),
        ([7], [7], True),
        ([1, 12], [12, 1], True),
        ([3, 7, 9], [3, 7, 11], False),
        ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1], True),
        ([1, 1, 2, 3], [1, 2, 2, 3], False),
        ]
for target, arr, expect in data:
    real = s.canBeEqual(target, arr)
    print(f'{target} {arr} expect {expect} real {real} result {expect == real}')
