#   https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence


from typing import List


class Solution:
    #   runtime; 44ms, 89.68%
    #   memory; 14MB, 100.00%
    def canMakeArithmeticProgression0(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        for i, a in enumerate(arr):
            if 0 == i:
                continue
            if diff != a - arr[i - 1]:
                return False
        return True

    #   runtime; 40ms, 94.92%
    #   memory; 14MB, 100.00%
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        return 1 == len(set(map(lambda t: t[1] - t[0], zip(arr, arr[1:]))))


s = Solution()
data = [([3, 5, 1], True),
        ([1, 2, 4], False),
        ]
for arr, expect in data:
    real = s.canMakeArithmeticProgression(arr)
    print(f'{arr} expect {expect} real {real} result {expect == real}')
