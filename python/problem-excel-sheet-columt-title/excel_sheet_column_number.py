#   https://leetcode.com/problems/excel-sheet-column-number


import math


class Solution:
    #   12.06%
    def titleToNumber0(self, s):
        if s is None or 0 == len(s):
            return 0
        d = {chr(ord('A') + i): i + 1 for i in range(26)}
        number = 0
        for i, c in enumerate(s[::-1]):
            print(i, c)
            number += math.pow(26, i) * d[c]
        return (int)(number)

    #   https://leetcode.com/explore/featured/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3419
    #   runtime; 20ms, 99.62%
    #   memory; 14MB, 6.48%
    def titleToNumber(self, s: str) -> int:
        d = {chr(i) : i - ord('A') + 1 for i in range(ord('A'), ord('Z') + 1)}
        return sum(26 ** i * d[c] for i, c in enumerate(s[::-1]))

s = Solution()
data = [('A', 1),
        ('AB', 28),
        ('ZY', 701),
        ]
for title, expect in data:
    real = s.titleToNumber(title)
    print(f'{title}, expect {expect}, real {real}, result {expect == real}')
