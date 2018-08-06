#   https://leetcode.com/problems/toeplitz-matrix

#   https://leetcode.com/problems/toeplitz-matrix/solution


class Solution:
    #   8.35%
    def isToeplitzMatrix(self, matrix):
        if matrix is None or 0 == len(matrix) or matrix[0] is None or 0 == len(matrix[0]):
            return False
        row, column = len(matrix), len(matrix[0])
        def isAllTheSame(r, c):
            val = matrix[r][c]
            i, j = r + 1, c + 1
            while i < row and j < column:
                if val != matrix[i][j]:
                    return False
                i += 1
                j += 1
            return True
        if not isAllTheSame(0, 0):
            return False
        for i in range(1, row):
            if not isAllTheSame(i, 0):
                return False
        for j in range(1, column):
            if not isAllTheSame(0, j):
                return False
        return True


s = Solution()
matrix1 = [[1, 2, 3, 4],
           [5, 1, 2, 3],
           [9, 5, 1, 2]
           ]
matrix2 = [[1, 2],
           [2, 2]
           ]
data = [(matrix1, True),
        (matrix2, False),
        ]
for matrix, expected in data:
    real = s.isToeplitzMatrix(matrix)
    print('expected {}, real {}, result {}'.format(expected, real, expected == real))
