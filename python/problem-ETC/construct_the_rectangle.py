#   https://leetcode.com/problems/construct-the-rectangle

#   https://leetcode.com/problems/construct-the-rectangle/discuss/146876/Python-Beats-100


import math


class Solution:
    #   Time Limit Exceeded
    def constructRectangle0(self, area):
        L = int(math.sqrt(area))
        while True:
            W = area / L
            if int(W) == W:
                W = int(W)
                if L >= W:
                    return [L, W]
                return [W, L]
            L += 1
        return []

    #   Wrong Answer
    def constructRectangle1(self, area):
        L = int(math.sqrt(area))
        while L <= (area // 2) + 1:
            W = area / L
            if int(W) == W:
                W = int(W)
                if L >= W:
                    return [L, W]
                return [W, L]
            L += 1
        return []

    #   28.94%
    def constructRectangle(self, area):
        for l in range(int(math.sqrt(area)), 0, -1):
            W = area / l
            if int(W) == W:
                W = int(W)
                if l >= W:
                    return [l, W]
                return [W, l]
        return []


s = Solution()
data = [(4, [2, 2]),
        (5, [5, 1]),
        (3, [3, 1]),
        (2, [2, 1]),
        (1, [1, 1]),
        (9999997, [1428571, 7]),
        ]
for area, expected in data:
    real = s.constructRectangle(area)
    print('{}, expected {}, real {}, result {}'.format(area, expected, real, expected == real))
