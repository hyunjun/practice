#   https://leetcode.com/problems/projection-area-of-3d-shapes

#   https://leetcode.com/problems/projection-area-of-3d-shapes/solution


class Solution:
    def projectionArea(self, grid):
        row, column = len(grid), len(grid[0])
        area = 0
        for r in range(row):
            for c in range(column):
                if grid[r][c]:
                    area += 1
        for r in range(row):
            area += max(grid[r])
        for c in range(column):
            maxRow = grid[0][c]
            for r in range(1, row):
                maxRow = max(maxRow, grid[r][c])
            area += maxRow
        return area


s = Solution()
data = [([[2]], 5),
        ([[1, 2], [3, 4]], 17),
        ([[1, 0], [0, 2]], 8),
        ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 14),
        ([[2, 2, 2], [2, 1, 2], [2, 2, 2]], 21),
        ]
for grid, expected in data:
    real = s.projectionArea(grid)
    print('{}, expected {}, real {}, result {}'.format(grid, expected, real, expected == real))
