#   https://leetcode.com/problems/shift-2d-grid


from typing import List


class Solution:
    #   runtime; 176ms, 57.85%
    #   memory; 12.8MB, 100.00%
    def shiftGrid0(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if grid is None or 0 == len(grid) or 0 == len(grid[0]):
            return []

        R, C = len(grid), len(grid[0])
        total, shifted = R * C, [[None] * C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                idx = r * C + c + k
                if total <= idx:
                    idx %= total
                nr, nc = idx // C, idx % C
                shifted[nr][nc] = grid[r][c]
        return shifted

    #   runtime; 164ms, 85.25%
    #   memory; 12.7MB, 100.00%
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if grid is None or 0 == len(grid) or 0 == len(grid[0]):
            return []

        R, C = len(grid), len(grid[0])
        total, shifted = R * C, [[None] * C for _ in range(R)]
        idx = k
        if total <= idx:
            idx %= total
        nr, nc = idx // C, idx % C
        for r in range(R):
            for c in range(C):
                shifted[nr][nc] = grid[r][c]
                nc += 1
                if nc == C:
                    nr += 1
                    nc = 0
                if nr == R:
                    nr = 0
        return shifted


s = Solution()
data = [([[1,2,3],[4,5,6],[7,8,9]], 1, [[9,1,2],[3,4,5],[6,7,8]]),
        ([[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], 4, [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]),
        ([[1,2,3],[4,5,6],[7,8,9]], 9, [[1,2,3],[4,5,6],[7,8,9]]),
        ]
for grid, k, expected in data:
    for g in grid:
        print(g)
    real = s.shiftGrid(grid, k)
    print(f'{k}, expected {expected}, real {real}, result {expected == real}')
