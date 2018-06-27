# https://leetcode.com/problems/number-of-islands


class Node:
    def __init__(self, row, col):
        self.row, self.col, self.visited = row, col, False
        self.up, self.right, self.left, self.down = None, None, None, None

    def __str__(self):
        return '[{}][{}] {}'.format(self.row, self.col, self.visited)


class Solution(object):
    #   Time Limit Exceeded
    def numIslands(self, grid):
        if grid is None or 0 == len(grid) or 0 == len(grid[0]):
            return 0

        maxRow, maxCol = len(grid), len(grid[0])
        nodes = []
        for row in range(maxRow):
            nodes.append([None] * maxCol)

        for row in range(maxRow):
            for col in range(maxCol):
                if '1' == grid[row][col]:
                    nodes[row][col] = Node(row, col)

        for row in range(maxRow):
            for col in range(maxCol):
                if '1' == grid[row][col]:
                    if 0 < row and '1' == grid[row - 1][col]:
                        nodes[row][col].up = nodes[row - 1][col]
                    if 0 < col and '1' == grid[row][col - 1]:
                        nodes[row][col].left = nodes[row][col - 1]
                    if col < maxCol - 1 and '1' == grid[row][col + 1]:
                        nodes[row][col].right = nodes[row][col + 1]
                    if row < maxRow - 1 and '1' == grid[row + 1][col]:
                        nodes[row][col].down = nodes[row + 1][col]

        cnt = 0
        for row in range(maxRow):
            for col in range(maxCol):
                if nodes[row][col] is None or nodes[row][col].visited:
                    continue
                queue = [nodes[row][col]]
                while queue:
                    node = queue[0]
                    node.visited = True
                    del queue[0]
                    if node.up and not node.up.visited:
                        queue.append(node.up)
                    if node.left and not node.left.visited:
                        queue.append(node.left)
                    if node.right and not node.right.visited:
                        queue.append(node.right)
                    if node.down and not node.down.visited:
                        queue.append(node.down)
                cnt += 1

        return cnt


s = Solution()
from data import data
for i, (grid, expected) in enumerate(data):
    real = s.numIslands(grid)
    print('[{}], expected {}, real {}, result {}'.format(i, expected, real, expected == real))
