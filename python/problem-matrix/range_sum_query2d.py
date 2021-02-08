#   https://leetcode.com/problems/range-sum-query-2d-immutable

#   https://leetcode.com/problems/range-sum-query-2d-immutable/solution


#   89.33%
class NumMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        if self.matrix and self.matrix[0]:
            self.row = len(self.matrix)
            self.col = len(self.matrix[0])
            self.sumMatrix = [[0] * self.col for _ in range(self.row)]
            for r in range(self.row):
                for c in range(self.col):
                    self.sumMatrix[r][c] = matrix[r][c]
            #for r in range(self.row):
            #    print(self.sumMatrix[r])
            for r in range(1, self.row):
                self.sumMatrix[r][0] += self.sumMatrix[r - 1][0]
            for c in range(1, self.col):
                self.sumMatrix[0][c] += self.sumMatrix[0][c - 1]
            for r in range(1, self.row):
                for c in range(1, self.col):
                    self.sumMatrix[r][c] += self.sumMatrix[r - 1][c] + self.sumMatrix[r][c - 1] - self.sumMatrix[r - 1][c - 1]
            #for r in range(self.row):
            #    print(self.sumMatrix[r])

    def sumRegion(self, row1, col1, row2, col2):
        total = self.sumMatrix[row2][col2]
        rowMinus = self.sumMatrix[row1 - 1][col2] if 0 < row1 else 0
        colMinus = self.sumMatrix[row2][col1 - 1] if 0 < col1 else 0
        rowColPlus = self.sumMatrix[row1 - 1][col1 - 1] if 0 < row1 and 0 < col1 else 0
        return total - rowMinus - colMinus + rowColPlus


matrix = [[3, 0, 1, 4, 2],
          [5, 6, 3, 2, 1],
          [1, 2, 0, 1, 5],
          [4, 1, 0, 1, 7],
          [1, 0, 3, 0, 5]]
n = NumMatrix(matrix)
data = [((2, 1, 4, 3), 8),
        ((1, 1, 2, 2), 11),
        ((1, 2, 2, 4), 12),
        ((0, 2, 2, 4), 19),
        ((1, 0, 2, 4), 26),
        ((0, 0, 2, 4), 36),
        ]
for (row1, col1, row2, col2), expected in data:
    real = n.sumRegion(row1, col1, row2, col2)
    print('sumRegion({}, {}, {}, {}), expected {}, real {}, result {}'.format(row1, col1, row2, col2, expected, real, expected == real))
