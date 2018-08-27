#   https://leetcode.com/problems/01-matrix

#   https://leetcode.com/problems/01-matrix/solution


class Solution:
    #   62.14%
    def updateMatrix(self, matrix):
        if matrix is None or 0 == len(matrix) or matrix[0] is None or 0 == len(matrix[0]):
            return None
        row, column = len(matrix), len(matrix[0])
        oup = [[row * column] * column for _ in range(row)]
        #for r in range(row):
        #    print(oup[r])
        lastZero = row * column
        if 0 == matrix[0][0]:
            lastZero = 0
            oup[0][0] = 0
        for r in range(1, row):
            if 0 == matrix[r][0]:
                oup[r][0] = 0
                lastZero = r
            else:
                if lastZero < row * column:
                    oup[r][0] = r - lastZero
        lastZero = 0 if 0 == matrix[0][0] else row * column
        for c in range(1, column):
            if 0 == matrix[0][c]:
                oup[0][c] = 0
                lastZero = c
            else:
                if lastZero < row * column:
                    oup[0][c] = c - lastZero
        for r in range(1, row):
            for c in range(1, column):
                if 0 == matrix[r][c]:
                    oup[r][c] = 0
                else:
                    oup[r][c] = min(oup[r - 1][c] + 1, oup[r][c - 1] + 1, oup[r - 1][c - 1] + 2)
        #for r in range(row):
        #    print(oup[r])
        lastZero = row - 1 if 0 == matrix[row - 1][column - 1] else row * column
        for r in range(row - 2, -1, -1):
            if 0 == matrix[r][column - 1]:
                oup[r][column - 1] = 0
                lastZero = r
            else:
                oup[r][column - 1] = min(oup[r][column - 1], lastZero - r)
        lastZero = column - 1 if 0 == matrix[row - 1][column - 1] else row * column
        for c in range(column - 2, -1, -1):
            if 0 == matrix[row - 1][c]:
                oup[row - 1][c] = 0
                lastZero = c
            else:
                oup[row - 1][c] = min(oup[row - 1][c], lastZero - c)
        #oup[row - 1][column - 1] = min(oup[row - 1][column - 1], oup[row - 2][column - 1] + 1, oup[row - 1][column - 2] + 1, oup[row - 2][column - 2] + 1)
        for r in range(row - 2, -1, -1):
            for c in range(column - 2, -1, -1):
                if 0 == matrix[r][c]:
                    oup[r][c] = 0
                    continue
                oup[r][c] = min(oup[r][c], oup[r + 1][c] + 1, oup[r][c + 1] + 1, oup[r + 1][c + 1] + 2)
        #oup[0][column - 1] = min(oup[0][column - 1], oup[1][column - 1] + 1, oup[0][column - 2] + 1, oup[1][column - 2] + 1)
        for r in range(1, row):
            for c in range(column - 2, -1, -1):
                if 0 == matrix[r][c]:
                    oup[r][c] = 0
                    continue
                oup[r][c] = min(oup[r][c], oup[r - 1][c] + 1, oup[r][c + 1] + 1, oup[r - 1][c + 1] + 2)
        #oup[row - 1][0] = min(oup[row - 1][0], oup[row - 2][0] + 1, oup[row - 1][1] + 1, oup[row - 2][1] + 1)
        for r in range(row - 2, -1, -1):
            for c in range(1, column):
                if 0 == matrix[r][c]:
                    oup[r][c] = 0
                    continue
                oup[r][c] = min(oup[r][c], oup[r + 1][c] + 1, oup[r][c - 1] + 1, oup[r + 1][c - 1] + 2)
        #for r in range(row):
        #    print(oup[r])
        return oup


s = Solution()
inp1 = [[0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]]
oup1 = [[0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]]
inp2 = [[0, 0, 0],
        [0, 1, 0],
        [1, 1, 1]]
oup2 = [[0, 0, 0],
        [0, 1, 0],
        [1, 2, 1]]
inp3 = [[0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 0, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 0]]
oup3 = [[0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 0, 0, 1, 2, 1],
        [2, 1, 1, 2, 1, 0]]
inp4 = [[1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
        [1, 0, 0, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 0, 1, 1, 1, 1]]
oup4 = [[2, 1, 0, 0, 1, 0, 0, 1, 1, 0],
        [1, 0, 0, 1, 0, 1, 1, 2, 2, 1],
        [1, 1, 1, 0, 0, 1, 2, 2, 1, 0],
        [0, 1, 2, 1, 0, 1, 2, 3, 2, 1],
        [0, 0, 1, 2, 1, 2, 1, 2, 1, 0],
        [1, 1, 2, 3, 2, 1, 0, 1, 1, 1],
        [0, 1, 2, 3, 2, 1, 1, 0, 0, 1],
        [1, 2, 1, 2, 1, 0, 0, 1, 1, 2],
        [0, 1, 0, 1, 1, 0, 1, 2, 2, 3],
        [1, 2, 1, 0, 1, 0, 1, 2, 3, 4]]
data = [([[0]], [[0]]),
        ([[1]], [[1]]),
        ([[0, 1]], [[0, 1]]),
        (inp1, oup1),
        (inp2, oup2),
        (inp3, oup3),
        (inp4, oup4),
        ]
for inp, expected in data:
    real = s.updateMatrix(inp)
    print(expected == real)
