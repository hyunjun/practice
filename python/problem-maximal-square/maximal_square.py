#   https://leetcode.com/problems/maximal-square/description/
#   6.23%

class Solution:
    def getMaximalSquare(self, matrix, r, c):
        result = 1
        rr = r + 1
        cc = c + 1
        while rr < len(matrix) and matrix[rr][c] == '1' and cc < len(matrix[0]) and matrix[r][cc] == '1':
            hasZero = False
            for rrr in range(r + 1, rr):
                if matrix[rrr][cc] == '0':
                    hasZero = True
            for ccc in range(c + 1, cc + 1):
                if matrix[rr][ccc] == '0':
                    hasZero = True
            if hasZero:
                break
            result += 1
            rr += 1
            cc += 1
        return result * result

    def maximalSquare(self, matrix):
        if matrix is None or 0 == len(matrix) or 0 == len(matrix[0]):
            return 0

        result = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == '1':
                    result = max(result, self.getMaximalSquare(matrix, r, c))
        return result


matrix0 = [ ['1', '0', '1', '0', '0'],
            ['1', '0', '1', '1', '1'],
            ['1', '1', '1', '1', '1'],
            ['1', '0', '0', '1', '0']
          ]
matrix1 = [ ['0', '0', '0'],
            ['0', '0', '0'],
            ['0', '0', '0']
          ]
matrix2 = [ ['1', '1', '1'],
            ['1', '1', '1'],
            ['1', '1', '1']
          ]
matrix3 = [ ['0', '0', '0', '1', '0', '1', '1', '1'],
            ['0', '1', '1', '0', '0', '1', '0', '1'],
            ['1', '0', '1', '1', '1', '1', '0', '1'],
            ['0', '0', '0', '1', '0', '0', '0', '0'],
            ['0', '0', '1', '0', '0', '0', '1', '0'],
            ['1', '1', '1', '0', '0', '1', '1', '1'],
            ['1', '0', '0', '1', '1', '0', '0', '1'],
            ['0', '1', '0', '0', '1', '1', '0', '0'],
            ['1', '0', '0', '1', '0', '0', '0', '0']
          ]

s = Solution()
print(s.maximalSquare(matrix0))
print(s.maximalSquare(matrix1))
print(s.maximalSquare(matrix2))
print(s.maximalSquare(matrix3))
