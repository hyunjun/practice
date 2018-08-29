#   https://leetcode.com/problems/surface-area-of-3d-shapes

#   https://leetcode.com/problems/surface-area-of-3d-shapes/solution


class Solution:
    #   66.87%
    def surfaceArea(self, grid):
        if grid is None or 0 == len(grid) or grid[0] is None or 0 == len(grid[0]):
            return 0
        row, column, total = len(grid), len(grid[0]), 0
        for r in range(row):
            for c in range(column):
                cur = grid[r][c]
                if 0 == cur:
                    continue
                upper = min(grid[r - 1][c], cur) if 0 < r else 0
                lower = min(grid[r + 1][c], cur) if r < row - 1 else 0
                left = min(grid[r][c - 1], cur) if 0 < c else 0
                right = min(grid[r][c + 1], cur) if c < column - 1 else 0
                total += (cur * 4 + 2) - upper - lower - left - right
        return total


s = Solution()
data = [([[2]], 10),
        ([[1, 2], [3, 4]], 34),
        ([[1, 0], [0, 2]], 16),
        ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 32),
        ([[2, 2, 2], [2, 1, 2], [2, 2, 2]], 46),
        ]
for grid, expected in data:
    real = s.surfaceArea(grid)
    print('expected {}, real {}, result {}'.format(expected, real, expected == real))
