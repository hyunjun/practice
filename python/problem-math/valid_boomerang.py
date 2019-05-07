#   https://leetcode.com/problems/valid-boomerang

#   https://leetcode.com/problems/valid-boomerang/discuss/287645/Python%3A-Heron's-formula-(beats-100)


class Solution:
    #   runtime; 40ms, 31.58%
    #   memory; 13.2MB, 100.00%
    def isBoomerang(self, points):

        def isSame(i, j):
            return i != j and points[i][0] == points[j][0] and points[i][1] == points[j][1]

        for i in range(3):
            for j in range(i + 1, 3):
                if isSame(i, j):
                    return False

        def angle(i, j):
            if points[j][0] == points[i][0]:
                return 90.0
            if points[j][1] == points[i][1]:
                return 0.0
            return (points[j][0] - points[i][0]) / (points[j][1] - points[i][1])

        if angle(0, 1) == angle(1, 2):
            return False

        return True


s = Solution()
data = [([[1, 1], [2, 3], [3, 2]], True),
        ([[1, 1], [2, 2], [3, 3]], False),
        ([[0, 0], [1, 0], [2, 2]], True),
        ]
for points, expected in data:
    real = s.isBoomerang(points)
    print('{}, expected {}, real {}, result {}'.format(points, expected, real, expected == real))
