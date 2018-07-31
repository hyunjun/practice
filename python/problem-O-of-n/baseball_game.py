#   https://leetcode.com/problems/baseball-game

#   https://leetcode.com/problems/baseball-game/solution


class Solution:
    #   3.71%
    def calPoints(self, ops):
        if ops is None or 0 == len(ops):
            return 0
        points = []
        for op in ops:
            if '+' == op:
                points.append(points[-2] + points[-1])
            elif 'D' == op:
                points.append(2 * points[-1])
            elif 'C' == op:
                points.pop()
            else:
                points.append(int(op))
        return sum(points)


s = Solution()
data = [(['5', '2', 'C', 'D', '+'], 30),
        (['5', '-2', '4', 'C', 'D', '9', '+', '+'], 27),
        ]
for ops, expected in data:
    real = s.calPoints(ops)
    print('{}, expected {}, real {}, result {}'.format(ops, expected, real, expected == real))
