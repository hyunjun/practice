#   https://leetcode.com/problems/find-lucky-integer-in-an-array


from collections import Counter
from typing import List


class Solution:
    #   runtime; 44ms, 100.00%
    #   memory; 13.9MB, 100.00%
    def findLucky(self, arr: List[int]) -> int:
        if arr is None or not (1 <= len(arr) <= 500):
            return -1
        lucky_numbers = [v for v, cnt in Counter(arr).items() if v == cnt]
        if 0 == len(lucky_numbers):
            return -1
        return max(lucky_numbers)


s = Solution()
data = [([2, 2, 3, 4], 2),
        ([1, 2, 2, 3, 3, 3], 3),
        ([2, 2, 2, 3, 3], -1),
        ([5], -1),
        ([7, 7, 7, 7, 7, 7, 7], 7),
        ]
for arr, expected in data:
    real = s.findLucky(arr)
    print(f'{arr} expected {expected} real {real} result {expected == real}')
