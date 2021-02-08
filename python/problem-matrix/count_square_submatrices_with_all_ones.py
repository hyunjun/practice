#   https://leetcode.com/problems/count-square-submatrices-with-all-ones

#   https://leetcode.com/problems/count-square-submatrices-with-all-ones/discuss/643429/Python-DP-Solution-%2B-Thinking-Process-Diagrams-(O(mn)-runtime-O(1)-space)


from typing import List


class Solution:
    #   runtime; 824ms, 32.37%
    #   memory; 14.8MB, 100.00%
    def countSquares0(self, matrix: List[List[int]]) -> int:
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

    #   Time Limit Exceeded
    def countSquares(self, matrix: List[List[int]]) -> int:
        if matrix is None or not (1 <= len(matrix) <= 300) or not (1 <= len(matrix[0]) <= 300):
            return 0
        R, C, visited, cnt = len(matrix), len(matrix[0]), set(), 0
        N = min(R, C)

        def isSquare(r, c, n):
            return all(matrix[y][x] == 1 for y in range(r, r + n) for x in range(c, c + n))

        for n in range(N, 0, -1):
            for r in range(R - n + 1):
                for c in range(C - n + 1):
                    if matrix[r][c] == 0:
                        continue
                    if isSquare(r, c, n):
                        cnt += 1
        return cnt

    #   https://leetcode.com/explore/featured/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3336
    #   runtime; 1116ms, 10.26%
    #   memory; 16.1MB
    def countSquares(self, matrix: List[List[int]]) -> int:
        if matrix is None or not (1 <= len(matrix) <= 300) or not (1 <= len(matrix[0]) <= 300):
            return 0
        R, C, visited, cnt = len(matrix), len(matrix[0]), set(), 0

        def isSquare(r, c, n):
            return all(matrix[y][x] == 1 for y in range(r, r + n) for x in range(c, c + n))

        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    continue
                N = min(R - r, C - c)
                cnt += 1
                for n in range(1, N):
                    if matrix[r + n][c + n] == 1 and all(matrix[rr][c + n] for rr in range(r, r + n)) and all(matrix[r + n][cc] for cc in range(c, c + n)):
                        cnt += 1
                    else:
                        break
        return cnt




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
