#   https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals


from collections import Counter
from typing import List


class Solution:
    #   runtime; 564ms, 76.26%
    #   memory; 32.7MB, 33.33%
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c, i = sorted(Counter(arr).items(), key=lambda t: t[1]), 0
        while 0 < k:
            while 0 < k and 0 < c[i][1]:
                c[i] = (c[i][0], c[i][1] - 1)
                k -= 1
            i += 1
        return len([n for n, cnt in c if 0 < cnt])


s = Solution()
data = [([5, 5, 4], 1, 1),
        ([4, 3, 1, 1, 3, 3, 2], 3, 2),
        ]
for arr, k, expect in data:
    real = s.findLeastNumOfUniqueInts(arr, k)
    print(f'{arr} {k} expect {expect} real {real} result {expect == real}')
