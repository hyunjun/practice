#   https://leetcode.com/problems/unique-paths-iii

#   https://leetcode.com/problems/unique-paths-iii/solution


class Solution:
    #   runtime; 60ms, 76.34%
    #   memory; 12.7MB, 100.00%
    def uniquePathsIII(self, grid):
        if grid is None or 0 == len(grid) or 0 == len(grid[0]):
            return 0

        R, C, sr, sc, totalWalk = len(grid), len(grid[0]), 0, 0, 0
        for r in range(R):
            for c in range(C):
                if -1 == grid[r][c]:
                    continue
                if 1 == grid[r][c]:
                    sr, sc = r, c
                totalWalk += 1

        res = set()
        def walk(paths, visited, r, c):
            paths.append((r, c))
            visited.add((r, c))
            if -1 != grid[r][c]:
                if 2 == grid[r][c]:
                    if totalWalk == len(paths):
                        res.add(''.join(['({},{})'.format(x, y) for x, y in paths]))
                else:
                    for nr, nc in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
                        if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited:
                            walk(paths, visited, nr, nc)
            paths.pop()
            visited.remove((r, c))

        walk([], set(), sr, sc)
        return len(res)


s = Solution()
data = [([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]], 2),
        ([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]], 4),
        ([[0, 1], [2, 0]], 0),
        ]
for grid, expected in data:
    real = s.uniquePathsIII(grid)
    print('{}, expected {}, real {}, result {}'.format(grid, expected, real, expected == real))
