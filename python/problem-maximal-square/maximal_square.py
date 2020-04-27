#   https://leetcode.com/problems/maximal-square


from typing import List


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

    #   6.23%
    def maximalSquare0(self, matrix):
        if matrix is None or 0 == len(matrix) or 0 == len(matrix[0]):
            return 0

        result = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == '1':
                    result = max(result, self.getMaximalSquare(matrix, r, c))
        return result

    #   https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3312
    #   runtime 320ms, 20.39%
    #   memory; 14.6MB
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix is None or 0 == len(matrix) or 0 == len(matrix[0]):
            return 0
        R, C, maxSqrSize = len(matrix), len(matrix[0]), 0

        def getMaxSqrSize(r, c):
            d = 1
            while r + d < R and c + d < C:
                isSquare = True
                if matrix[r + d][c + d] == '0':
                    isSquare = False
                    break
                if not isSquare:
                    break
                for nr in range(r, r + d):
                    if matrix[nr][c + d] == '0':
                        isSquare = False
                        break
                if not isSquare:
                    break
                for nc in range(c, c + d):
                    if matrix[r + d][nc] == '0':
                        isSquare = False
                        break
                if not isSquare:
                    break
                d += 1
            return d ** 2

        for r in range(R):
            for c in range(C):
                if '0' == matrix[r][c]:
                    continue
                maxSqrSize = max(maxSqrSize, getMaxSqrSize(r, c))

        return maxSqrSize


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
data = [(matrix0, 4),
        (matrix1, 0),
        (matrix2, 9),
        (matrix3, 1),
        ]
for matrix, expected in data:
    real = s.maximalSquare(matrix)
    print(f'expected {expected} real {real} result {expected == real}')
