#   https://leetcode.com/problems/unique-paths-ii

#   https://leetcode.com/problems/unique-paths-ii/solution


from typing import List


class Solution:
    #   Time Limit Exceeded
    def uniquePathsWithObstacles0(self, obstacleGrid):
        R, C = len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1
        def move(row, column):
            if 1 == obstacleGrid[row][column]:
                return
            if row == R and column == C:
                self.cnt += 1
            else:
                if row < R:
                    move(row + 1, column)
                if column < C:
                    move(row, column + 1)

        self.cnt = 0
        move(0, 0)
        return self.cnt

    #   44ms, 45.71%
    def uniquePathsWithObstacles1(self, obstacleGrid):
        R, C = len(obstacleGrid), len(obstacleGrid[0])
        if 1 == R and 1 == C:
            if 0 == obstacleGrid[0][0]:
                return 1
        if 1 == obstacleGrid[0][0]:
            return 0
        counts = [[0] * C for _ in range(R)]
        for r in range(1, R):
            if 1 == obstacleGrid[r][0]:
                break
            counts[r][0] = 1
        for c in range(1, C):
            if 1 == obstacleGrid[0][c]:
                break
            counts[0][c] = 1
        for r in range(1, R):
            for c in range(1, C):
                if 1 == obstacleGrid[r][c]:
                    continue
                if 0 == obstacleGrid[r - 1][c] and 0 == obstacleGrid[r][c - 1]:
                    counts[r][c] = counts[r - 1][c] + counts[r][c - 1]
                elif 0 == obstacleGrid[r - 1][c]:
                    counts[r][c] = counts[r - 1][c]
                elif 0 == obstacleGrid[r][c - 1]:
                    counts[r][c] = counts[r][c - 1]
        return counts[R - 1][C - 1]

    #   https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3723
    #   runtime; 40ms, 77.01%
    #   memory; 14.2MB, 94.86%
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        R, C = len(obstacleGrid), len(obstacleGrid[0])
        paths = [[0] * C for _ in range(R)]
        for r in range(R):
            if obstacleGrid[r][0] == 1:
                break
            paths[r][0] = 1
        for c in range(C):
            if obstacleGrid[0][c] == 1:
                break
            paths[0][c] = 1
        for r in range(1, R):
            for c in range(1, C):
                if obstacleGrid[r][c] == 1:
                    continue
                paths[r][c] = paths[r - 1][c] + paths[r][c - 1]
        return paths[-1][-1]


s = Solution()
data = [([[0,0,0], [0,1,0], [0,0,0]], 2),
        ([[0,1], [0,0]], 1),
        ([[0]], 1),
        ([[1, 0]], 0),
        ([[0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0],[1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,1],[0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0],[0,0,0,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0],[1,0,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0],[0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0],[0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0],[0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0],[0,1,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,1],[1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,1,1,0,1,0,0,0,0,1,1],[0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,1],[1,1,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0]], 1637984640),
        ]
for grid, expected in data:
    real = s.uniquePathsWithObstacles(grid)
    print('expected {}, real {}, result {}'.format(expected, real, expected == real))
