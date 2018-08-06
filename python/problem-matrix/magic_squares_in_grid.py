#   https://leetcode.com/problems/magic-squares-in-grid

#   https://leetcode.com/problems/magic-squares-in-grid/solution


class Solution:
    #   52.54%
    def numMagicSquaresInside(self, grid):
        def isMagicSquare(r, c):
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    if grid[i][j] < 1 or 9 < grid[i][j]:
                        return False
            rSums = [sum([grid[r + i][c + j] for j in range(3)]) for i in range(3)]
            cSums = [sum([grid[r + i][c + j] for i in range(3)]) for j in range(3)]
            dSum0 = sum([grid[r + i][c + i] for i in range(3)])
            dSum1 = sum([grid[r + i][c + 2 - i] for i in range(3)])
            return rSums[0] == rSums[1] == rSums[2] == cSums[0] == cSums[1] == cSums[2] == dSum0 == dSum1
        cnt = 0
        for r in range(len(grid) - 2):
            for c in range(len(grid[0]) - 2):
                if isMagicSquare(r, c):
                    cnt += 1
        return cnt


s = Solution()
input1 = [[4,3,8,4],
          [9,5,1,9],
          [2,7,6,2]]
input2 = [[10,3,5],
          [1,6,11],
          [7,9,2]]
data = [(input1, 1),
        (input2, 0),
        ]
for grid, expected in data:
    real = s.numMagicSquaresInside(grid)
    print('{}, expected {}, real {}, result {}'.format(grid, expected, real, expected == real))
