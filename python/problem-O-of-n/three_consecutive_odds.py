#   https://leetcode.com/problems/three-consecutive-odds


from typing import List


class Solution:
    #   runtime; 44ms, 88.89%
    #   memory; 14MB, 43.06%
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(2, len(arr)):
            if arr[i - 2] % 2 == 1 and arr[i - 1] % 2 == 1 and arr[i] % 2 == 1:
                return True
        return False


s = Solution()
data = [([2, 6, 4, 1], False),
        ([1, 2, 34, 3, 4, 5, 7, 23, 12], True),
        ]
for arr, expect in data:
    real = s.threeConsecutiveOdds(arr)
    print(f'{arr} expect {expect} real {real} result {expect == real}')
