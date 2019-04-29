#   https://leetcode.com/problems/moving-stones-until-consecutive


class Solution:
    #   Wrong Answer
    def numMovesStones0(self, a, b, c):
        if not (a < b < c):
            return [0, 0]

        diff1, diff2 = b - a, c - b
        minCnt = (0 if diff1 <= 1 else 1) + (0 if diff2 <= 1 else 1)
        maxCnt = (diff1 - 1 if diff1 > 1 else 0) + (diff2 - 1 if diff2 > 1 else 0)
        return [minCnt, maxCnt]

    #   Wrong Answer
    def numMovesStones1(self, a, b, c):
        if not (a < b < c):
            minVal, maxVal = min([a, b, c]), max([a, b, c])
            return self.numMovesStones(minVal, sum([a, b, c]) - minVal - maxVal, maxVal)

        diff1, diff2 = b - a, c - b
        minCnt = (0 if diff1 <= 1 else 1) + (0 if diff2 <= 1 else 1)
        maxCnt = (diff1 - 1 if diff1 > 1 else 0) + (diff2 - 1 if diff2 > 1 else 0)
        return [minCnt, maxCnt]

    #   runtime; 36ms, 100.00%
    #   memory; 12.9MB, 100.00%
    def numMovesStones(self, a, b, c):
        if not (a < b < c):
            minVal, maxVal = min([a, b, c]), max([a, b, c])
            return self.numMovesStones(minVal, sum([a, b, c]) - minVal - maxVal, maxVal)

        diff1, diff2 = b - a, c - b
        if diff1 == 2 or diff2 == 2:
            minCnt = 1
        else:
            minCnt = (0 if diff1 <= 1 else 1) + (0 if diff2 <= 1 else 1)
        maxCnt = (diff1 - 1 if diff1 > 1 else 0) + (diff2 - 1 if diff2 > 1 else 0)
        return [minCnt, maxCnt]


s = Solution()
data = [(1, 2, 5, [1, 2]),
        (4, 3, 2, [0, 0]),
        (2, 4, 1, [1, 1]),
        (3, 5, 1, [1, 2]),
        ]
for a, b, c, expected in data:
    real = s.numMovesStones(a, b, c)
    print('{}, {}, {}, expected {}, real {}, result {}'.format(a, b, c, expected, real, expected == real))
