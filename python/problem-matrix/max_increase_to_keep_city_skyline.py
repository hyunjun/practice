#   https://leetcode.com/problems/max-increase-to-keep-city-skyline


class Solution(object):
    #   runtime; 52ms, 90.48%
    #   memory; 11.7MB, 88.89%
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R, C = len(grid), len(grid[0])
        topView, leftView = [0] * C, [0] * R
        for r in range(R):
            leftView[r] = max(grid[r])
        for c in range(C):
            topView[c] = max([grid[r][c] for r in range(R)])
        _sum = 0
        for r in range(R):
            for c in range(C):
                _sum += min(topView[c], leftView[r]) - grid[r][c]
        return _sum


s = Solution()
data = [([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]], 35),
        ]
for grid, expected in data:
    for g in grid:
        print(g)
    real = s.maxIncreaseKeepingSkyline(grid)
    print(f'expected {expected}, real {real}, result {expected == real}')
