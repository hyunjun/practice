#   https://leetcode.com/problems/minimum-falling-path-sum

#   https://leetcode.com/problems/minimum-falling-path-sum/solution


class Solution:
    #   runtime; 56ms, 45.27%
    #   memory; 11.1MB, 60.32%
    def minFallingPathSum(self, A):
        if A is None or 0 == len(A) or 0 == len(A[0]):
            return 0
        ROW, COL = len(A), len(A[0])
        dp = [[0] * COL for _ in range(ROW)]
        for i in range(COL):
            dp[0][i] = A[0][i]
        for r in range(ROW):
            if 0 == r:
                continue
            for c in range(COL):
                cand = [dp[r - 1][c]]
                if 0 <= c - 1:
                    cand.append(dp[r - 1][c - 1])
                if c + 1 < COL:
                    cand.append(dp[r - 1][c + 1])
                dp[r][c] = A[r][c] + min(cand)
        return min(dp[ROW - 1])


s = Solution()
data = [([[1,2,3],[4,5,6],[7,8,9]], 12),
        ]
for A, expected in data:
    real = s.minFallingPathSum(A)
    print('{}, expected {}, real {}, result {}'.format(A, expected, real, expected == real))
