#   https://leetcode.com/problems/longest-common-subsequence


class Solution:
    #   runtime; 376ms, 92.11%
    #   memory; 21.6MB, 100.00%
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 is None or 0 == len(text1) or text2 is None or 0 == len(text2):
            return 0
        C, R = len(text1), len(text2)
        table = [[0] * (C + 1) for _ in range(R + 1)]
        for r in range(R):
            for c in range(C):
                if text1[c] == text2[r]:
                    table[r + 1][c + 1] = table[r][c] + 1
                else:
                    table[r + 1][c + 1] = max(table[r][c + 1], table[r + 1][c])
        return table[-1][-1]

    #   https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3311
    #   runtime; 412ms, 84.48%
    #   memory; 21.5MB
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 is None or text2 is None or not (1 <= len(text1) <= 1000) or not (1 <= len(text2) <= 1000):
            return 0
        R, C = len(text1) + 1, len(text2) + 1
        grid = [[0] * C for _ in range(R)]
        for r in range(1, R):
            for c in range(1, C):
                if text1[r - 1] == text2[c - 1]:
                    grid[r][c] = grid[r - 1][c - 1] + 1
                else:
                    grid[r][c] = max(grid[r - 1][c], grid[r][c - 1])
        return grid[-1][-1]


s = Solution()
data = [('abcde', 'ace', 3),
        ('abcde', 'aec', 2),
        ('abc', 'abc', 3),
        ('abc', 'def', 0),
        ]
for text1, text2, expected in data:
    real = s.longestCommonSubsequence(text1, text2)
    print(f'{text1}, {text2}, expected {expected}, real {real}, result {expected == real}')
