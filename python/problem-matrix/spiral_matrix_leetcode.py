#   https://leetcode.com/problems/spiral-matrix

#   https://leetcode.com/problems/spiral-matrix/solution


class Solution:
    #   7.26%
    def spiralOrder(self, matrix):
        if matrix is None or 0 == len(matrix) or matrix[0] is None or 0 == len(matrix[0]):
            return []
        row, column, res = len(matrix), len(matrix[0]), []
        r, c, direction = 0, 0, 1
        upper, lower, right, left = 0, row - 1, column - 1, 0
        while len(res) < row * column:
            if 1 == direction:
                for c in range(left, right + 1):
                    res.append(matrix[r][c])
                c = right
                upper += 1
                direction <<= 1
            elif 2 == direction:
                for r in range(upper, lower + 1):
                    res.append(matrix[r][c])
                r = lower
                right -= 1
                direction <<= 1
            elif 4 == direction:
                for c in range(right, left - 1, -1):
                    res.append(matrix[r][c])
                c = left
                lower -= 1
                direction <<= 1
            elif 8 == direction:
                for r in range(lower, upper - 1, -1):
                    res.append(matrix[r][c])
                r = upper
                left += 1
                direction = 1
        return res


s = Solution()
matrix1 = [[ 1, 2, 3 ],
           [ 4, 5, 6 ],
           [ 7, 8, 9 ]]
matrix2 = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12]]
matrix3 = [[1, 2, 3, 4, 5],
           [6, 7, 8, 9, 10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20]]
data = [(matrix1, [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        (matrix2, [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
        (matrix3, [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]),
        ]
for matrix, expected in data:
    real = s.spiralOrder(matrix)
    print('expected {}, real {}, result {}'.format(expected, real, expected == real))
