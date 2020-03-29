#   https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix


from typing import List


class Solution:
    #   runtime; 120ms, 93.43% -> 124ms, 82.09%
    #   memory; 14.8MB, 100.00% -> 14.9MB, 100.00%
    #   if grid[r][0] < 0 추가 후 오히려 늦어짐
    def countNegatives(self, grid: List[List[int]]) -> int:
        if grid is None or not (1 <= len(grid) <= 100) or not (1 <= len(grid[0]) <= 100):
            return 0
        cnt, R, C = 0, len(grid), len(grid[0])
        for r in range(R):
            if grid[r][-1] >= 0:
                continue
            if grid[r][0] < 0:
                cnt += C
                continue
            for c in range(C - 1, -1, -1):
                if grid[r][c] >= 0:
                    break
                cnt += 1
        return cnt


s = Solution()
grid1 = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
grid2 = [[3,2],[1,0]]
grid3 = [[1,-1],[-1,-1]]
grid4 = [[-1]]
data = [(grid1, 8),
        (grid2, 0),
        (grid3, 3),
        (grid4, 1),
        ]
for grid, expected in data:
    for g in grid:
        print(g)
    real = s.countNegatives(grid)
    print(f'expected {expected} real {real} result {expected == real}')
