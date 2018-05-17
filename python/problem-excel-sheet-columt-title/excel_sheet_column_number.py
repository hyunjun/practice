#   https://leetcode.com/problems/excel-sheet-column-number
#   12.06%


import math


class Solution:
    def titleToNumber(self, s):
        if s is None or 0 == len(s):
            return 0
        d = {chr(ord('A') + i): i + 1 for i in range(26)}
        number = 0
        for i, c in enumerate(s[::-1]):
            print(i, c)
            number += math.pow(26, i) * d[c]
        return (int)(number)

s = Solution()
data = [('A', 1), ('AB', 28), ('ZY', 701)]
for title, expected in data:
    real = s.titleToNumber(title)
    print('{}, expected {}, real {}, result {}'.format(title, expected, real, expected == real))
