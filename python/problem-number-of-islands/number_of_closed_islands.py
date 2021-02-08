#   https://leetcode.com/problems/number-of-closed-islands


from typing import List


class Solution:
    #   runtime; 264ms, 5.19%
    #   memory; 14.2MB, 100.00%
    def closedIsland(self, grid: List[List[int]]) -> int:
        if grid is None or not (1 <= len(grid) <= 100) or not (1 <= len(grid[0]) <= 100):
            return 0

        R, C = len(grid), len(grid[0])

        def fill(r, c, n):
            if not (0 <= r < R) or not (0 <= c < C) or grid[r][c] != 0:
                return
            grid[r][c] = n
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                fill(nr, nc, n)

        #   change not closed land into -1
        for r in range(R):
            for c in [0, C - 1]:
                if grid[r][c] == 0:
                    fill(r, c, -1)
        for r in [0, R - 1]:
            for c in range(C):
                if grid[r][c] == 0:
                    fill(r, c, -1)

        #   check the number of islands
        ret = 0
        for r in range(1, R - 1):
            for c in range(1, C - 1):
                if grid[r][c] == 0:
                    fill(r, c, -1)
                    ret += 1

        return ret


s = Solution()
island1 = [[1,1,1,1,1,1,1,0],
           [1,0,0,0,0,1,1,0],
           [1,0,1,0,1,1,1,0],
           [1,0,0,0,0,1,0,1],
           [1,1,1,1,1,1,1,0]
           ]
island2 = [[0,0,1,0,0],
           [0,1,0,1,0],
           [0,1,1,1,0]
           ]
island3 = [[1,1,1,1,1,1,1],
           [1,0,0,0,0,0,1],
           [1,0,1,1,1,0,1],
           [1,0,1,0,1,0,1],
           [1,0,1,1,1,0,1],
           [1,0,0,0,0,0,1],
           [1,1,1,1,1,1,1]
           ]
data = [(island1, 2),
        (island2, 1),
        (island3, 2),
        ]
for grid, expected in data:
    for g in grid:
        print(g)
    real = s.closedIsland(grid)
    print(f'expected {expected} real {real} result {expected == real}')
