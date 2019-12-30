#   https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side


from typing import List


class Solution:
    #   runtime; 76ms, 90.18%
    #   memory; 13.6MB, 100.00%
    def replaceElements(self, arr: List[int]) -> List[int]:
        if arr is None or not (1 <= len(arr) <= 10 ** 4):
            return []
        curMax = arr[-1]
        arr[-1] = -1
        for i in range(len(arr) - 2, -1, -1):
            tmp = curMax
            curMax = max(curMax, arr[i])
            arr[i] = tmp
        return arr


s = Solution()
data = [([17, 18, 5, 4, 6, 1], [18, 6, 6, 6, 1, -1]),
        ]
for arr, expected in data:
    original, real = arr[:], s.replaceElements(arr)
    print(f'{original} expected {expected} real {real} result {expected == real}')
