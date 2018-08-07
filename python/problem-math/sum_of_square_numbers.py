#   https://leetcode.com/problems/sum-of-square-numbers

#   https://leetcode.com/problems/sum-of-square-numbers/solution


import math


class Solution:
    #   90.88%
    def judgeSquareSum(self, c):
        if c < 0:
            return False
        if 0 == c:
            return True
        smaller, larger = 1, int(math.sqrt(c))
        while smaller <= larger:
            smaller = math.sqrt(c - larger ** 2)
            if int(smaller) == smaller:
                return True
            larger -= 1
        return False


s = Solution()
data = [(5, True),
        (4, True),
        (3, False),
        (125, True),
        (129, False),
        ]
for c, expected in data:
    real = s.judgeSquareSum(c)
    print('{}, expected {}, real {}, result {}'.format(c, expected, real, expected == real))
