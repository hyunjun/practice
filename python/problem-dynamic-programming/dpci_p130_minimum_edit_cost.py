

class Solution:
    def minEditNum(self, s1: str, s2: str) -> int:
        if (s1 is None or 0 == len(s1)) and (s2 is None or 0 == len(s2)):
            return 0
        if s1 is None or 0 == len(s1):
            return len(s2)
        if s2 is None or 0 == len(s2):
            return len(s1)

        R, C = len(s1), len(s2)
        grid = [[0] * (C + 1) for _ in range(R + 1)]
        for r in range(1, R + 1):
            for c in range(1, C + 1):
                if s1[r - 1] == s2[c - 1]:
                    grid[r][c] = 1 + grid[r - 1][c - 1]
                else:
                    grid[r][c] = max(grid[r - 1][c], grid[r][c - 1])
        return max(R, C) - grid[-1][-1]


s = Solution()
data = [('COMPUTER', 'COMMUTER', 1),
        ('SPORT', 'SORT', 1),
        ('CAT', 'CAR', 1),
        ('SUNDAY', 'SATURDAY', 3),
        ]
for s1, s2, expected in data:
    real = s.minEditNum(s1, s2)
    print(f'{s1} {s2} expected {expected} real {real} result {expected == real}')
