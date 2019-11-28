#   https://leetcode.com/problems/max-area-of-island

#   https://leetcode.com/problems/max-area-of-island/solution


class Solution:
    #   13.85%
    def maxAreaOfIsland0(self, grid):
        if grid is None or 0 == len(grid) or grid[0] is None or 0 == len(grid[0]):
            return 0
        row, column = len(grid), len(grid[0])
        visited, maxArea = set(), 0

        def getArea(r, c):
            if r < 0 or row <= r or c < 0 or column <= c or 0 == grid[r][c] or (r, c) in visited:
                return 0
            visited.add((r, c))
            positions = [(r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)]
            areas = [0, 0, 0, 0]
            for i, pos in enumerate(positions):
                areas[i] = getArea(pos[0], pos[1])
            return 1 + sum(areas)

        for r in range(row):
            for c in range(column):
                if 0 == grid[r][c] or (r, c) in visited:
                    continue
                maxArea = max(maxArea, getArea(r, c))
        return maxArea

    #   72.15%
    def maxAreaOfIsland1(self, grid):
        if grid is None or 0 == len(grid) or grid[0] is None or 0 == len(grid[0]):
            return 0
        row, column = len(grid), len(grid[0])

        parentDict = {}
        for r in range(row):
            for c in range(column):
                if 0 == grid[r][c]:
                    continue
                lParent, uParent = None, None
                if 0 <= c - 1 and 1 == grid[r][c - 1]:
                    lParent = parentDict[r * column + c - 1]
                    while lParent != parentDict[lParent]:
                        lParent = parentDict[lParent]
                if 0 <= r - 1 and 1 == grid[r - 1][c]:
                    uParent = parentDict[(r - 1) * column + c]
                    while uParent != parentDict[uParent]:
                        uParent = parentDict[uParent]
                k = r * column + c
                if lParent is None and uParent is None:
                    parentDict[k] = k
                elif lParent is None:
                    parentDict[k] = uParent
                elif uParent is None:
                    parentDict[k] = lParent
                else:
                    parentDict[k] = parentDict[max(lParent, uParent)] = min(lParent, uParent)
        #    print([' 0' if 0 == grid[r][c] else '{:02d}'.format(parentDict[r * column + c]) for c in range(column)])
        #print()
        #for r in range(row):
        #    print([' 0' if 0 == grid[r][c] else '{:02d}'.format(parentDict[r * column + c]) for c in range(column)])

        countDict = {}
        for k, parent in parentDict.items():
            while parent != parentDict[parent]:
                parent = parentDict[parent]
            if parent in countDict:
                countDict[parent] += 1
            else:
                countDict[parent] = 1
        #print(countDict)
        if 0 == len(countDict.values()):
            return 0
        return max([v for v in countDict.values()])

    #   runtime; 132ms, 47.81%
    #   memory; 15.5MB, 5.88%
    def maxAreaOfIsland(self, grid):
        if grid is None or 0 == len(grid) or grid[0] is None or 0 == len(grid[0]):
            return 0
        maxArea, row, column = 0, len(grid), len(grid[0])

        def getArea(r, c):
            if r < 0 or row <= r or c < 0 or column <= c or 0 == grid[r][c]:
                return 0
            grid[r][c] = 0
            return 1 + sum([getArea(nr, nc) for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]])

        for r in range(row):
            for c in range(column):
                if 0 == grid[r][c]:
                    continue
                maxArea = max(maxArea, getArea(r, c))

        return maxArea


s = Solution()
ex1 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,1,1,0,0,0],
       [0,1,1,0,1,0,0,0,0,0,0,0,0],
       [0,1,0,0,1,1,0,0,1,0,1,0,0],
       [0,1,0,0,1,1,0,0,1,1,1,0,0],
       [0,0,0,0,0,0,0,0,0,0,1,0,0],
       [0,0,0,0,0,0,0,1,1,1,0,0,0],
       [0,0,0,0,0,0,0,1,1,0,0,0,0]]
ex2 = [[0,0,0,0,0,0,0,0]]
ex3 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,1,1,0,0,0],
       [0,1,1,0,1,0,0,0,0,0,1,0,0],
       [0,1,0,0,1,1,0,0,1,0,1,0,0],
       [0,1,0,0,1,1,0,0,1,1,1,0,0],
       [0,0,0,0,0,0,0,0,0,0,1,0,0],
       [0,0,0,0,0,0,0,1,1,1,0,0,0],
       [0,0,0,0,0,0,0,1,1,0,0,0,0]]
ex4 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,1,1,1,0,0],
       [0,1,1,0,1,0,0,0,0,0,1,0,0],
       [0,1,0,0,1,1,0,0,1,0,1,0,0],
       [0,1,0,0,1,1,0,0,1,1,1,0,0],
       [0,0,0,0,0,0,0,0,0,0,1,0,0],
       [0,0,0,0,0,0,0,1,1,1,0,0,0],
       [0,0,0,0,0,0,0,1,1,0,0,0,0]]
ex5 = [[0,1,1,1,1,1,1,1],
       [0,0,0,0,1,0,0,1],
       [1,0,0,0,0,0,0,0],
       [0,0,1,1,1,0,1,0],
       [0,0,0,1,0,0,0,1],
       [0,1,1,1,0,0,0,1],
       [0,0,1,0,1,1,0,1],
       [0,1,0,1,0,1,1,1],
       [1,0,1,0,1,1,1,0],
       [0,1,1,0,1,0,0,0]]
data = [(ex1, 6),
        (ex2, 0),
        (ex3, 7),
        (ex4, 12),
        (ex5, 12),
        ]
for grid, expected in data:
    real = s.maxAreaOfIsland(grid)
    print('expected {}, real {}, result {}'.format(expected, real, expected == real))
