#   https://www.youtube.com/watch?v=IWvbPIYQPFM


class Node:
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col
        self.up = None
        self.left = None

    def __str__(self):
        return '[{}][{}] color {}'.format(self.row, self.col, self.color)


class Solution:
    def fill(self, visited, grid, color, r, c, maxRow, maxCol):
        if r < 0 or c < 0 or maxRow <= r or maxCol <= c or visited[r][c] or color != grid[r][c]:
            return 0
        visited[r][c] = True
        return 1 + self.fill(visited, grid, color, r - 1, c, maxRow, maxCol) + self.fill(visited, grid, color, r, c - 1, maxRow, maxCol) + self.fill(visited, grid, color, r + 1, c, maxRow, maxCol) + self.fill(visited, grid, color, r, c + 1, maxRow, maxCol)

    def maxConnectedColorsRecur(self, grid):
        if grid is None or 0 == len(grid):
            return 0

        visited = []
        for i in range(len(grid)):
            visited.append([False] * len(grid[0]))

        maxCnt = 1
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if visited[row][col]:
                    continue
                cnt = self.fill(visited, grid, grid[row][col], row, col, len(grid), len(grid[0]))
                if maxCnt < cnt:
                    maxCnt = cnt
        return maxCnt

    def maxConnectedColorsIter(self, grid):
        if grid is None or 0 == len(grid):
            return 0

        nodes = []
        for row in range(len(grid)):
            nodes.append([None] * len(grid[0]))
            for col in range(len(grid[0])):
                nodes[row][col] = Node(grid[row][col], row, col)

        for row in range(1, len(grid)):
            if grid[row - 1][0] == grid[row][0]:
                nodes[row][0].up = nodes[row - 1][0]
        for col in range(1, len(grid[0])):
            if grid[0][col - 1] == grid[0][col]:
                nodes[0][col].left = nodes[0][col - 1]
        for row in range(1, len(grid)):
            for col in range(1, len(grid[0])):
                if grid[row][col] == grid[row - 1][col]:
                    nodes[row][col].up = nodes[row - 1][col]
                if grid[row][col] == grid[row][col - 1]:
                    nodes[row][col].left = nodes[row][col - 1]
        maxCnt = 0
        for row in range(len(grid) - 1, -1, -1):
            for col in range(len(grid[0]) - 1, -1, -1):
                if nodes[row][col] is None:
                    continue
                cnt, queue = 0, [nodes[row][col]]
                while queue:
                    node = queue[0]
                    del queue[0]
                    cnt += 1
                    if node.up:
                        queue.append(node.up)
                    if node.left:
                        queue.append(node.left)
                    nodes[node.row][node.col] = None
                if maxCnt < cnt:
                    maxCnt = cnt
        return maxCnt


s = Solution()

grid = [[0, 0, 1, 2],
        [0, 3, 0, 3],
        [2, 3, 3, 3]]
print(s.maxConnectedColorsRecur(grid))
print(s.maxConnectedColorsIter(grid))
