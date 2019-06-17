#   https://leetcode.com/problems/duplicate-zeros


from typing import List


class Solution:
    #   runtime; 56ms, 84.05%
    #   memory; 13.4MB, 100.00%
    def duplicateZeros(self, arr: List[int]) -> None:
        if arr is None or 0 == len(arr):
            return
        cnt, move = 0, [0] * len(arr)
        for i, a in enumerate(arr):
            move[i] = cnt
            if 0 == a:
                cnt += 1
        for i in range(len(arr) - 1, -1, -1):
            if 0 == move[i]:
                break
            if len(arr) <= i + move[i]:
                arr[i] = 0
                continue
            arr[i + move[i]] = arr[i]
            arr[i] = 0


s = Solution()
data = [([1, 0, 2, 3, 0, 4, 5, 0], [1, 0, 0, 2, 3, 0, 0, 4]),
        ([1, 2, 3], [1, 2, 3]),
        ]
for arr, expected in data:
    before = arr[:]
    s.duplicateZeros(arr)
    print(f'{before}, expected {expected}, real {arr}, result {expected == arr}')
