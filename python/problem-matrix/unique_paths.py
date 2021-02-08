#   https://leetcode.com/problems/unique-paths


class Solution:
    #   https://leetcode.com/explore/featured/card/june-leetcoding-challenge/543/week-5-june-29th-june-30th/3375
    #   runtime; 32ms, 57.17%
    #   memory; 13.7MB, 82.14%
    def uniquePaths(self, m: int, n: int) -> int:
        if 1 == m and 1 == n:
            return 1
        if not (1 <= m <= 100) or not (1 <= n <= 100):
            return 0
        board = [[0] * m for _ in range(n)]
        for i in range(1, n):
            board[i][0] = 1
        for j in range(1, m):
            board[0][j] = 1
        for i in range(1, n):
            for j in range(1, m):
                board[i][j] = board[i - 1][j] + board[i][j - 1]
        return board[-1][-1]


s = Solution()
data = [(1, 1, 1),
        (3, 2, 3),
        (7, 3, 28),
        ]
for m, n, expect in data:
    real = s.uniquePaths(m, n)
    print(f'{m} {n} expect {expect} real {real} result {expect == real}')
