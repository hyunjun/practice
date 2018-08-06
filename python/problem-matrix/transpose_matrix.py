#   https://leetcode.com/problems/transpose-matrix

#   https://leetcode.com/problems/transpose-matrix/solution


class Solution:
    #   10.05%
    def transpose(self, A):
        row, column = len(A), len(A[0])
        res = []
        [res.append([None] * row) for i in range(column)]
        for r in range(row):
            for c in range(column):
                res[c][r] = A[r][c]
        return res


s = Solution()
data = [([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 4, 7], [2, 5, 8], [3, 6, 9]]),
        ([[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]]),
        ]
for A, expected in data:
    real = s.transpose(A)
    print('{}, expected {}, real {}, result {}'.format(A, expected, real, expected == real))
