#   https://leetcode.com/problems/unique-paths-iii

#   https://leetcode.com/problems/unique-paths-iii/solution


from typing import List


class Solution:
    #   runtime; 60ms, 76.34%
    #   memory; 12.7MB, 100.00%
    def uniquePathsIII0(self, grid):
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

    #   https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3466
    #   runtime; 92ms, 29.81%
    #   memory; 19.4MB
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        pathLen, sr, sc = 0, None, None
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    sr, sc = r, c
                if grid[r][c] != -1:
                    pathLen += 1
        cnt, queue = 0, [(set(), (sr, sc))]
        while queue:
            visited, point = queue.pop(0)
            if point in visited:
                continue
            visited.add(point)
            if grid[point[0]][point[1]] == 2:
                if len(visited) == pathLen:
                    cnt += 1
                continue
            for nr, nc in [(point[0] + 1, point[1]), (point[0] - 1, point[1]), (point[0], point[1] + 1), (point[0], point[1] - 1)]:
                if not (0 <= nr < R) or not (0 <= nc < C) or grid[nr][nc] == -1:
                    continue
                queue.append((visited.copy(), (nr, nc)))
        return cnt


s = Solution()
data = [([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]], 2),
        ([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]], 4),
        ([[0, 1], [2, 0]], 0),
        ]
for grid, expected in data:
    real = s.uniquePathsIII(grid)
    print('{}, expected {}, real {}, result {}'.format(grid, expected, real, expected == real))
