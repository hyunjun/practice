

from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        if grid is None or 0 == len(grid) or 0 == len(grid[0]):
            return 0

        R, C = len(grid), len(grid[0])
        cost = [[0] * C for _ in range(R)]
        cost[0][0] = grid[0][0]
        for r in range(1, R):
            cost[r][0] = cost[r - 1][0] + grid[r][0]
        for c in range(1, C):
            cost[0][c] = cost[0][c - 1] + grid[0][c]
        for r in range(1, R):
            for c in range(1, C):
                cost[r][c] = min(cost[r - 1][c], cost[r][c - 1]) + grid[r][c]
        return cost[-1][-1]


s = Solution()
data = [([[1, 3, 5, 8], [4, 2, 1, 7], [4, 3, 2, 3]], 12),
        ]
for grid, expected in data:
    for g in grid:
        print(g)
    real = s.minCost(grid)
    print(f'expected {expected} real {real} result {expected == real}')

