#   https://leetcode.com/problems/max-area-of-island

#   https://leetcode.com/problems/max-area-of-island/solution


class Solution:
    #   13.85%
    def maxAreaOfIsland(self, grid):
        if grid is None or 0 == len(grid) or grid[0] is None or 0 == len(grid[0]):
            return 0
        row, column = len(grid), len(grid[0])
        visited, maxArea = set(), 0

        def getArea(r, c):
            if r < 0 or row <= r or c < 0 or column <= c or 0 == grid[r][c] or (r, c) in visited:
                return 0
            visited.add((r, c))
            positions = [(r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)]
            areas = [0, 0, 0, 0]
            for i, pos in enumerate(positions):
                areas[i] = getArea(pos[0], pos[1])
            return 1 + sum(areas)

        for r in range(row):
            for c in range(column):
                if 0 == grid[r][c] or (r, c) in visited:
                    continue
                maxArea = max(maxArea, getArea(r, c))
        return maxArea


s = Solution()
ex1 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]
ex2 = [[0,0,0,0,0,0,0,0]]
data = [(ex1, 6),
        (ex2, 0),
        ]
for grid, expected in data:
    real = s.maxAreaOfIsland(grid)
    print('expected {}, real {}, result {}'.format(expected, real, expected == real))
