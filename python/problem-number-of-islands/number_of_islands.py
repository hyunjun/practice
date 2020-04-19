# https://leetcode.com/problems/number-of-islands
# Union Find는 아직 어떻게 적용할지 모르겠음

'''
# 기본적으로 내 생각과 같지만 훨씬 멋진 방법
def numIslands(self, grid):
    def sink(i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
            grid[i][j] = '0'
            map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))
            return 1
        return 0
    return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))
'''
class Solution(object):

    # 27.74%
    def numIslands0(self, grid):
        def spread(r, c, val):
            if visited[r][c] == 1:
                return
            visited[r][c] = 1
            if grid[r][c] == '0':
                boards[r][c] = -1
                return
            boards[r][c] = min(boards[r][c], val)
            if 0 < r:
                spread(r - 1, c, boards[r][c])
            if 0 < c:
                spread(r, c - 1, boards[r][c])
            if r + 1 < rows:
                spread(r + 1, c, boards[r][c])
            if c + 1 < cols:
                spread(r, c + 1, boards[r][c])

        if grid is None or 0 == len(grid) or 0 == len(grid[0]):
            return 0

        cols, rows = len(grid[0]), len(grid)
        #print(cols, rows)
        boards, visited = [], []
        row_mul = (cols // 10 + 1) * 10
        for r in range(rows):
            cur = []
            for c in range(cols):
                cur.append(r * row_mul + c)
            boards.append(cur)
            cur = []
            for c in range(cols):
                cur.append(0)
            visited.append(cur)
        #print(boards)
        #print(visited)

        if grid[0][0] == '0':
            boards[0][0] = -1

        for r in range(rows):
            for c in range(cols):
                spread(r, c, boards[r][c])
        #print(boards)

        result = []
        for r in range(rows):
            for c in range(cols):
                if -1 != boards[r][c] and boards[r][c] not in result:
                    result.append(boards[r][c])

        return len(result)


    #   https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3302/
    #   runtime; 180ms, 13.65%
    #   memory; 14.9MB
    def numIslands(self, grid):
        if grid is None or 0 == len(grid) or 0 == len(grid[0]):
            return 0

        cnt, R, C = 0, len(grid), len(grid[0])

        def isValidLand(r, c):
            if (0 <= r < R) and (0 <= c < C) and grid[r][c] == '1':
                return True
            return False

        def fill(r, c, n):
            if not isValidLand(r, c):
                return
            grid[r][c] = n
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                fill(nr, nc, n)

        for r in range(R):
            for c in range(C):
                if not isValidLand(r, c):
                    continue
                fill(r, c, '-1')
                cnt += 1
        return cnt


s = Solution()
from data import data
for i, (grid, expected) in enumerate(data):
    real = s.numIslands(grid)
    print(f'[{i}], expected {expected}, real {real}, result {expected == real}')
