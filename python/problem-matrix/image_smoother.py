#   https://leetcode.com/problems/image-smoother

#   https://leetcode.com/problems/image-smoother/solution


import math


class Solution:
    #   92.24%
    def imageSmoother(self, M):
        if M is None or 0 == len(M) or M[0] is None or 0 == len(M[0]):
            return []
        row, column = len(M), len(M[0])
        res = []
        [res.append([0] * column) for r in range(row)]

        def avg(r, c):
            _sum, cnt = 0, 0
            if 0 < r:
                if 0 < c:
                    _sum += M[r - 1][c - 1]
                    cnt += 1
                _sum += M[r - 1][c]
                cnt += 1
                if c < column - 1:
                    _sum += M[r - 1][c + 1]
                    cnt += 1
            if 0 < c:
                _sum += M[r][c - 1]
                cnt += 1
            _sum += M[r][c]
            cnt += 1
            if c < column - 1:
                _sum += M[r][c + 1]
                cnt += 1
            if r < row - 1:
                if 0 < c:
                    _sum += M[r + 1][c - 1]
                    cnt += 1
                _sum += M[r + 1][c]
                cnt += 1
                if c < column - 1:
                    _sum += M[r + 1][c + 1]
                    cnt += 1
            return math.floor(_sum / cnt)

        for i in range(row):
            for j in range(column):
                res[i][j] = avg(i, j)
        return res


s = Solution()
data = [([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
        ]
for M, expected in data:
    real = s.imageSmoother(M)
    print('{}, expected {}, real {}, result {}'.format(M, expected, real, expected == real))
