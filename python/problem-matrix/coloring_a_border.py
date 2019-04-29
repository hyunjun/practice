#   https://leetcode.com/problems/coloring-a-border


class Solution:
    #   runtime; 96ms, 96.21%
    #   memory; 13.4MB, 100.00%
    def colorBorder(self, grid, r0, c0, color):
        if grid is None or 0 == len(grid) or 0 == len(grid[0]):
            return grid
        R, C, orgC = len(grid), len(grid[0]), grid[r0][c0]

        def isBorder(r, c):
            if r == 0 or r == R - 1 or c == 0 or c == C - 1:
                return True
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if grid[nr][nc] != orgC:
                    return True
            return False

        def isValid(r, c):
            if r < 0 or R <= r or c < 0 or C <= c:
                return False
            return True

        borders, visited = [], set()
        def fill(r, c):
            #print('({}, {})'.format(r, c))
            if (r, c) in visited:
                return
            visited.add((r, c))
            if isBorder(r, c):
                borders.append((r, c))
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                #print('\tnext ({}, {})\tvisited {}\tisValid {}'.format(nr, nc, visited, isValid(nr, nc)))
                if (nr, nc) in visited or not isValid(nr, nc) or grid[nr][nc] != orgC:
                    continue
                fill(nr, nc)

        fill(r0, c0)

        for r, c in borders:
            grid[r][c] = color

        return grid


s = Solution()
data = [([[1,1],[1,2]], 0, 0, 3, [[3, 3], [3, 2]]),
        ([[1,2,2],[2,3,2]], 0, 1, 3, [[1, 3, 3], [2, 3, 3]]),
        ([[1,1,1],[1,1,1],[1,1,1]], 1, 1, 2, [[2, 2, 2], [2, 1, 2], [2, 2, 2]]),
        ]
for grid, r0, c0, color, expected in data:
    real = s.colorBorder(grid, r0, c0, color)
    print('{}, {}, {}, {}, expected {}, real {}, result {}'.format(grid, r0, c0, color, expected, real, expected == real))
