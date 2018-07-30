#   https://leetcode.com/problems/judge-route-circle

#   https://leetcode.com/problems/judge-route-circle/solution


class Solution:
    #   26.73%
    def judgeCircle(self, moves):
        if moves is None or 0 == len(moves):
            return True
        pos = [0, 0]
        for move in moves:
            if 'U' == move:
                pos[1] += 1
            elif 'D' == move:
                pos[1] -= 1
            elif 'L' == move:
                pos[0] -= 1
            elif 'R' == move:
                pos[0] += 1
        return pos[0] == 0 and pos[1] == 0


s = Solution()
data = [('UD', True),
        ('LL', False),
        ]
for moves, expected in data:
    real = s.judgeCircle(moves)
    print('{}, expected {}, real {}, result {}'.format(moves, expected, real, expected == real))
