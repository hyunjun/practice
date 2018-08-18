#   https://leetcode.com/problems/minimum-path-sum


class Solution:
    def minPathSum0(self, grid):
        if grid is None or 0 == len(grid) or grid[0] is None or 0 == len(grid[0]):
            return 0
        row, column = len(grid), len(grid[0])
        listOfLists = [[None] * column for _ in range(row)]
        for r in range(row):
            for c in range(column):
                listOfLists[r][c] = [grid[r][c]]
        for r in range(1, row):
            listOfLists[r][0].extend(listOfLists[r - 1][0])
        for c in range(1, column):
            listOfLists[0][c].extend(listOfLists[0][c - 1])
        for r in range(1, row):
            for c in range(1, column):
                upListSum = sum(listOfLists[r - 1][c])
                leftListSum = sum(listOfLists[r][c - 1])
                if upListSum < leftListSum:
                    listOfLists[r][c].extend(listOfLists[r - 1][c])
                else:
                    listOfLists[r][c].extend(listOfLists[r][c - 1])
        return sum(listOfLists[row - 1][column - 1])

    #   40.41%
    def minPathSum(self, grid):
        if grid is None or 0 == len(grid) or grid[0] is None or 0 == len(grid[0]):
            return 0
        row, column = len(grid), len(grid[0])
        sumGrid = [[None] * column for _ in range(row)]
        for r in range(row):
            for c in range(column):
                sumGrid[r][c] = grid[r][c]
        for r in range(1, row):
            sumGrid[r][0] += sumGrid[r - 1][0]
        for c in range(1, column):
            sumGrid[0][c] += sumGrid[0][c - 1]
        for r in range(1, row):
            for c in range(1, column):
                upSum = sumGrid[r - 1][c]
                leftSum = sumGrid[r][c - 1]
                if upSum < leftSum:
                    sumGrid[r][c] += upSum
                else:
                    sumGrid[r][c] += leftSum
        return sumGrid[row - 1][column - 1]


s = Solution()
inp1 = [[1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]]
data = [(inp1, 7),
        ]
for inp, expected in data:
    real = s.minPathSum(inp)
    print('expected {}, real {}, result {}'.format(expected, real, expected == real))
