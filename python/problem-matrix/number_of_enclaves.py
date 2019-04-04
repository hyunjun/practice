#   https://leetcode.com/problems/number-of-enclaves


class Solution:
    #   runtime; 172ms, 36.58%
    #   memory; 15.5MB, 100.00%
    def numEnclaves(self, A):
        if A is None or 0 == len(A) or 0 == len(A[0]):
            return 0
        R, C = len(A), len(A[0])
        if 1 == R or 1 == C:
            return 0
        for r in range(1, R - 1):
            for c in range(1, C - 1):
                if 1 == A[r][c]:
                    A[r][c] = 2

        def change2to1(row, col):
            if 0 == row or R - 1 == row or 0 == col or C - 1 == col or 2 != A[row][col]:
                return
            A[row][col] = 1
            for _r, _c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                change2to1(_r, _c)

        for c in range(1, C - 1):
            if A[0][c] == 1 and A[1][c] == 2:
                change2to1(1, c)
            if A[R - 1][c] == 1 and A[R - 2][c] == 2:
                change2to1(R - 2, c)
        for r in range(1, R - 1):
            if A[r][0] == 1 and A[r][1] == 2:
                change2to1(r, 1)
            if A[r][C - 1] == 1 and A[r][C - 2] == 2:
                change2to1(r, C - 2)

        ret = 0
        for r in range(1, R - 1):
            for c in range(1, C - 1):
                if 2 == A[r][c]:
                    ret += 1
        return ret


s = Solution()
data = [([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]], 3),
        ([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]], 0),
        ]
for A, expected in data:
    real = s.numEnclaves(A)
    print('{}, expected {}, real {}, result {}'.format(A, expected, real, expected == real))
