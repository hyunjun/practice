#   https://leetcode.com/problems/count-square-submatrices-with-all-ones


from typing import List


class Solution:
    #   runtime; 824ms, 32.37%
    #   memory; 14.8MB, 100.00%
    def countSquares(self, matrix: List[List[int]]) -> int:
        if matrix is None or 0 == len(matrix) or 0 == len(matrix[0]):
            return 0
        tot, R, C = 0, len(matrix), len(matrix[0])
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    continue
                maxLen = min(R - r, C - c)
                tot += 1
                for l in range(1, maxLen):
                    if all(matrix[rr][c + l] == 1 for rr in range(r, r + l + 1)) and all(matrix[r + l][cc] == 1 for cc in range(c, c + l + 1)):
                        tot += 1
                    else:
                        break
        return tot


matrix1 = [[0,1,1,1],
           [1,1,1,1],
           [0,1,1,1]
           ]
matrix2 = [[1,0,1],
           [1,1,0],
           [1,1,0]
           ]
s = Solution()
data = [(matrix1, 15),
        (matrix2, 7),
        ]
for matrix, expected in data:
    for m in matrix:
        print(m)
    real = s.countSquares(matrix)
    print(f'expected {expected}, real {real}, result {expected == real}')
