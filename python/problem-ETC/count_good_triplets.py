#   https://leetcode.com/problems/count-good-triplets


from typing import List


class Solution:
    #   runtime; 364ms, 95.37%
    #   memory; 13.8MB, 68.27%
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        s = 0
        for i in range(len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                if abs(arr[i] - arr[j]) > a:
                    continue
                for k in range(j + 1, len(arr)):
                    if abs(arr[j] - arr[k]) > b or abs(arr[i] - arr[k]) > c:
                        continue
                    s += 1
        return s


s = Solution()
data = [([3, 0, 1, 1, 9, 7], 7, 2, 3, 4),
        ([1, 1, 2, 2, 3], 0, 0, 1, 0),
        ]
for arr, a, b, c, expect in data:
    real = s.countGoodTriplets(arr, a, b, c)
    print(f'{arr} {a} {b} {c} expect {expect} real {real} result {expect == real}')
