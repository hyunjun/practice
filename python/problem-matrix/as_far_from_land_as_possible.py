#   https://leetcode.com/problems/as-far-from-land-as-possible


class Solution(object):
    #   runtime; 624ms, 52.72%
    #   memory; 11.9MB, 100.00%
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R, C = len(grid), len(grid[0])

        def isValid(r, c):
            if 0 <= r < R and 0 <= c < C:
                return True
            return False

        def hasNeighborOne(r, c):
            for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if isValid(nr, nc) and grid[nr][nc] == 1:
                    return True
            return False

        dist = [[0] * C for _ in range(R)]
        def getMinDist(r, c):
            minDist = float('inf')
            for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if isValid(nr, nc) and dist[nr][nc] > 0:
                    minDist = min(minDist, dist[nr][nc])
            return minDist

        for r in range(R):
            for c in range(C):
                if grid[r][c]:
                    continue
                if hasNeighborOne(r, c):
                    dist[r][c] = 1
                    continue
                minDist = getMinDist(r, c)
                if minDist != float('inf'):
                    dist[r][c] = minDist + 1

        for r in range(R - 1, -1, -1):
            for c in range(C - 1, -1, -1):
                if grid[r][c]:
                    continue
                if hasNeighborOne(r, c):
                    dist[r][c] = 1
                    continue
                minDist = getMinDist(r, c)
                if minDist != float('inf'):
                    dist[r][c] = minDist + 1

        maxDist = 0
        for r in range(R):
            for c in range(C):
                maxDist = max(maxDist, dist[r][c])
        if maxDist == 0:
            return -1
        return maxDist
