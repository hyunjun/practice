#   https://leetcode.com/problems/island-perimeter
#   65.52%


class Solution:
    def islandPerimeter(self, grid):
        def numPerimeters(r, c):
            num = 0
            if r == 0 or 0 == grid[r - 1][c]:
                num += 1
            if c == 0 or 0 == grid[r][c - 1]:
                num += 1
            if c == len(grid[0]) - 1 or 0 == grid[r][c + 1]:
                num += 1
            if r == len(grid) - 1 or 0 == grid[r + 1][c]:
                num += 1
            return num

        if grid is None or 0 == len(grid) or 0 == len(grid[0]):
            return 0
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if 0 == grid[r][c]:
                    continue
                res += numPerimeters(r, c)
        return res


s = Solution()
grid0 = [[0,1,0,0],
         [1,1,1,0],
         [0,1,0,0],
         [1,1,0,0]]
data = [(grid0, 16),
        ]
for grid, expected in data:
    real = s.islandPerimeter(grid)
    print('expected {}, real {}, result {}'.format(expected, real, expected == real))
