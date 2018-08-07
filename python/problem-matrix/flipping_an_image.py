#   https://leetcode.com/problems/flipping-an-image

#   https://leetcode.com/problems/flipping-an-image/solution


class Solution:
    #   11.23%
    def flipAndInvertImage(self, A):
        row, column = len(A), len(A[0])
        for r in range(row):
            i, j = 0, column - 1
            while i < j:
                A[r][i], A[r][j] = A[r][j], A[r][i]
                i += 1
                j -= 1
            for c in range(column):
                A[r][c] = 0 if 1 == A[r][c] else 1
        return A


s = Solution()
data = [([[1,1,0],[1,0,1],[0,0,0]], [[1,0,0],[0,1,0],[1,1,1]]),
        ([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]], [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]),
        ]
for A, expected in data:
    real = s.flipAndInvertImage(A)
    print('{}, expected {}, real {}, result {}'.format(A, expected, real, expected == real))
