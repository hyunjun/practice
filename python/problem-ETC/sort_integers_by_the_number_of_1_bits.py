#   https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits


from typing import List


class Solution:
    #   runtime; 88ms, 25.75%
    #   memory; 13.9MB, 100.00%
    def sortByBits(self, arr: List[int]) -> List[int]:
        if arr is None or not (1 <= len(arr) <= 500):
            return []
        def countOnes(n):
            return sum([1 if b == '1' else 0 for b in bin(n)[2:]])
        return sorted(arr, key=lambda a: (countOnes(a), a))


s = Solution()
data = [([0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 4, 8, 3, 5, 6, 7]),
        ([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1], [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]),
        ([10000, 10000], [10000, 10000]),
        ([2, 3, 5, 7, 11, 13, 17, 19], [2, 3, 5, 17, 7, 11, 13, 19]),
        ]
for arr, expected in data:
    real = s.sortByBits(arr)
    print(f'{arr} expected {expected} real {real} result {expected == real}')
