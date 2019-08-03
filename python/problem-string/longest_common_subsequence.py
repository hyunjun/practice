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


s = Solution()
data = [('abcde', 'ace', 3),
        ('abcde', 'aec', 2),
        ('abc', 'abc', 3),
        ('abc', 'def', 0),
        ]
for text1, text2, expected in data:
    real = s.longestCommonSubsequence(text1, text2)
    print(f'{text1}, {text2}, expected {expected}, real {real}, result {expected == real}')
