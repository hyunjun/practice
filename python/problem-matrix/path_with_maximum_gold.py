#   https://leetcode.com/problems/path-with-maximum-gold


class Solution:
    #   runtime; 1996ms, 21.13%
    #   memory; 12.7MB, 100.00%
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        def isValid(r, c):
            if r < 0 or R <= r or c < 0 or C <= c or grid[r][c] == 0:
                return False
            return True

        self.acc = 0
        def gather(acc, visited, r, c):
            if (r, c) in visited:
                return
            visited.add((r, c))
            acc += grid[r][c]
            self.acc = max(self.acc, acc)
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if isValid(nr, nc):
                    gather(acc, visited, nr, nc)
            visited.remove((r, c))
            acc -= grid[r][c]

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    continue
                gather(0, set(), r, c)

        return self.acc


s = Solution()
data = [([[0,6,0],[5,8,7],[0,9,0]], 24),
        ([[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]], 28),
        ([[1,0,7,0,0,0],[2,0,6,0,1,0],[3,5,6,7,4,2],[4,3,1,0,2,0],[3,0,5,0,20,0]], 60),
        ]
for grid, expected in data:
    for g in grid:
        print(g)
    real = s.getMaximumGold(grid)
    print(f'{grid}, expected {expected}, real {real}, result {expected == real}')
