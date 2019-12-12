

class Solution:
    def maxPalindromeLen(self, s: str) -> int:
        if s is None or 0 == len(s):
            return 0

        R = C = len(s)
        rStr, grid = s[::-1], [[0] * (C + 1) for _ in range(R + 1)]
        for r in range(1, R + 1):
            for c in range(1, C + 1):
                if s[c - 1] == rStr[r - 1]:
                    grid[r][c] = 1 + grid[r - 1][c - 1]
                else:
                    grid[r][c] = max(grid[r - 1][c], grid[r][c - 1])
        return grid[-1][-1]


solution = Solution()
data = [('BBABCBCAB', 7),
        ]
for s, expected in data:
    real = solution.maxPalindromeLen(s)
    print(f'{s} expected {expected} real {real} result {expected == real}')
