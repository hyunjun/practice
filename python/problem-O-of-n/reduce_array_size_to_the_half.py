#   https://leetcode.com/problems/reduce-array-size-to-the-half


from collections import Counter
from typing import List


class Solution:
    #   runtime; 876ms, 5.88%
    #   memory; 41.7MB, 100.00%
    def minSetSize(self, arr: List[int]) -> int:
        if arr is None or not (1 <= len(arr) <= 10 ** 5):
            return 0
        reducedLen, c, res = len(arr), Counter(arr), 0
        target = reducedLen // 2
        for _, cnt in sorted(c.items(), key=lambda t: (-t[1], t[0])):
            reducedLen -= cnt
            res += 1
            if reducedLen <= target:
                return res
        return res


s = Solution()
data = [([3, 3, 3, 3, 5, 5, 5, 2, 2, 7], 2),
        ([7, 7, 7, 7, 7, 7], 1),
        ([1, 9], 1),
        ([1000, 1000, 3, 7], 1),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5),
        ]
for arr, expected in data:
    real = s.minSetSize(arr)
    print(f'{arr} expected {expected} real {real} result {expected == real}')
