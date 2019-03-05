#   https://leetcode.com/problems/construct-quad-tree


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    #   runtime; 196ms, 36.23%
    #   memory; 14.9MB, 36.67%
    def construct(self, grid):
        if grid is None or 0 == len(grid) or 0 == len(grid[0]):
            return None
        ROW, COL = len(grid), len(grid[0])
        if 1 == ROW and 1 == COL:
            return Node(grid[0][0] == 1, True, None, None, None, None)
        if all([grid[r][c] == 0 for r in range(ROW) for c in range(COL)]):
            return Node(False, True, None, None, None, None)
        if all([grid[r][c] == 1 for r in range(ROW) for c in range(COL)]):
            return Node(True, True, None, None, None, None)
        topLeftGrid, topRightGrid, bottomLeftGrid, bottomRightGrid = [], [], [], []
        for r in range(ROW):
            if r < ROW // 2:
                topLeftGrid.append(grid[r][:COL // 2])
                topRightGrid.append(grid[r][COL // 2:])
            else:
                bottomLeftGrid.append(grid[r][:COL // 2])
                bottomRightGrid.append(grid[r][COL // 2:])
        print('top left')
        for r in range(len(topLeftGrid)):
            print(topLeftGrid[r])
        print('top right')
        for r in range(len(topRightGrid)):
            print(topRightGrid[r])
        print('bottom left')
        for r in range(len(bottomLeftGrid)):
            print(bottomLeftGrid[r])
        print('bottom right')
        for r in range(len(bottomRightGrid)):
            print(bottomRightGrid[r])
        return Node(True, False, self.construct(topLeftGrid), self.construct(topRightGrid), self.construct(bottomLeftGrid), self.construct(bottomRightGrid))


grid = [[1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        ]
s = Solution()
s.construct(grid)
