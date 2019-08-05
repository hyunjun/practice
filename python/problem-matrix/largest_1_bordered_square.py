#   https://leetcode.com/problems/largest-1-bordered-square

#   https://leetcode.com/problems/largest-1-bordered-square/discuss/351421/Python-DP-Solution-faster-than-100


from typing import List


class Solution:
    #   runtime; 592ms, 40.30%
    #   memory; 14.1MB, 100.00%
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        if grid is None or 0 == len(grid) or 0 == len(grid[0]):
            return 0
        maxSquare, R, C = 0, len(grid), len(grid[0])
        for r in range(R):
            for c in range(C):
                if 0 == grid[r][c]:
                    continue
                ones = 0
                while r + ones < R and c + ones < C and grid[r + ones][c] == 1 and grid[r][c + ones] == 1:
                    ones += 1
                ones -= 1
                for j in range(ones, -1, -1):
                    if all([1 == grid[r + j][c + k] for k in range(j + 1) if c + k < C]) \
                        and all([1 == grid[r + k][c + j] for k in range(j + 1) if r + k < R]):
                        maxSquare = max(maxSquare, (j + 1) * (j + 1))
        return maxSquare


s = Solution()
data = [([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 9),
        ([[1, 1, 1, 1], [1, 0, 1, 1], [1, 1, 1, 0]], 9),
        ([[1, 1, 0, 0], [1, 1, 1, 1], [1, 1, 1, 0]], 4),
        ([[1, 1, 0, 0], [1, 0, 1, 1], [1, 1, 1, 1]], 4),
        ([[1, 1, 0, 0]], 1),
        ([[1, 1], [1, 0]], 1),
        ([[1, 1, 1], [1, 0, 1], [1, 1, 0]], 1),
        ]
for grid, expected in data:
    real = s.largest1BorderedSquare(grid)
    for g in grid:
        print(g)
    print(f'expected {expected}, real {real}, result {expected == real}')
