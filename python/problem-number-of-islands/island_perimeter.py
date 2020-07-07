#   https://leetcode.com/problems/island-perimeter


from typing import List


class Solution:
    #   65.52%
    def islandPerimeter0(self, grid):
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

    #   https://leetcode.com/explore/featured/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3383
    #   runtime; 772ms, 23.60%
    #   memory; 14MB, 64.55%
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        cnt, R, C = 0, len(grid), len(grid[0])
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    continue
                for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if not (0 <= nr < R) or not (0 <= nc < C) or grid[nr][nc] == 0:
                        cnt += 1
        return cnt


s = Solution()
grid0 = [[0,1,0,0],
         [1,1,1,0],
         [0,1,0,0],
         [1,1,0,0]]
data = [(grid0, 16),
        ([[1, 1, 1, 1, 0]], 10),
        ([[1]], 4),
        ]
for grid, expected in data:
    real = s.islandPerimeter(grid)
    print('expected {}, real {}, result {}'.format(expected, real, expected == real))
