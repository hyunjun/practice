#   https://leetcode.com/problems/number-of-islands
#   15.98%


class Solution:
    def numIslands(self, grid):
        parents = {}
        def sink(r, c, i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and '1' == grid[i][j]:
                #print(r, c, i, j, grid[i][j])
                if (i, j) not in parents:
                    parents[(i, j)] = (r, c)
                grid[i][j] = '0'
                #map(sink, (r, r, r, r), (c, c, c, c), (i - 1, i, i, i + 1), (j, j - 1, j + 1, j))
                sink(r, c, i - 1, j)
                sink(r, c, i, j - 1)
                sink(r, c, i, j + 1)
                sink(r, c, i + 1, j)
        [sink(i, j, i, j) for i in range(len(grid)) for j in range(len(grid[0]))]
        #print(grid)
        #print(parents)
        for c, p in parents.items():
            child, parent = c, p
            #print(child, parent, parents[parent])
            while parent != parents[parent]:
                parent = parents[parent]
                #print('\t', parent, parents[parent])
            parents[child] = parent
        #print(parents)
        return len(set(parents.values()))

s = Solution()
from data import data
for i, (grid, expected) in enumerate(data):
    real = s.numIslands(grid)
    print('[{}], expected {}, real {}, result {}'.format(i, expected, real, expected == real))
