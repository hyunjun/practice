#   https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3289


from collections import Counter
from typing import List


class Solution:
    #   runtime; 28ms
    #   memory; 14.1MB
    def countElements(self, arr: List[int]) -> int:
        if arr is None or not (1 <= len(arr) <= 1000):
            return 0
        c, tot = Counter(arr), 0
        for k, cnt in c.items():
            if k + 1 in c:
                tot += cnt
        return tot


s = Solution()
data = [([1, 2, 3], 2),
        ([1, 1, 3, 3, 5, 5, 7, 7], 0),
        ([1, 3, 2, 3, 5, 0], 3),
        ([1, 1, 2, 2], 2),
        ]
for arr, expected in data:
    real = s.countElements(arr)
    print(f'{arr} expected {expected} real {real} result {expected == real}')
