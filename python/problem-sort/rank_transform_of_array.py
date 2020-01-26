#   https://leetcode.com/problems/rank-transform-of-an-array


from typing import List


class Solution:
    #   runtime; 516ms, 100.00%
    #   memory; 30.5MB, 100.00%
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if arr is None or not (0 <= len(arr) <= 10 ** 5):
            return []
        i, d = 1, {}
        for num in sorted(arr):
            if num not in d:
                d[num] = i
                i += 1
        return [d[num] for num in arr]


s = Solution()
data = [([40, 10, 20, 30], [4, 1, 2, 3]),
        ([100, 100, 100], [1, 1, 1]),
        ([37, 12, 28, 9, 100, 56, 80, 5, 12], [5, 3, 4, 2, 8, 6, 7, 1, 3]),
        ]
for arr, expected in data:
    real = s.arrayRankTransform(arr)
    print(f'{arr} expected {expected} real {real} result {expected == real}')
