#   https://leetcode.com/problems/check-if-n-and-its-double-exist


from typing import List


class Solution:
    #   runtime; 52ms, 64.22%
    #   memory; 13.8MB, 100.00%
    def checkIfExist0(self, arr: List[int]) -> bool:
        if arr is None or not (2 <= len(arr) <= 500):
            return False
        if arr == [0, 0]:
            return True
        s = set(arr)
        for a in arr:
            if 0 == a:
                continue
            if (a / 2) in s or (a * 2) in s:
                return True
        return False

    #   runtime; 52ms, 64.22%
    #   memory; 13.8MB, 100.00%
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr is None or not (2 <= len(arr) <= 500):
            return False
        if arr == [0, 0]:
            return True
        s = set(arr)
        for a in sorted(arr):
            if 0 == a:
                continue
            if (a * 2) in s:
                return True
        return False


s = Solution()
data = [([10, 2, 5, 3], True),
        ([7, 1, 14, 11], True),
        ([3, 1, 7, 11], False),
        ([-2, 0, 10, -19, 4, 6, -8], False)
        ]
for arr, expected in data:
    real = s.checkIfExist(arr)
    print(f'{arr} expected {expected} real {real} result {expected == real}')
