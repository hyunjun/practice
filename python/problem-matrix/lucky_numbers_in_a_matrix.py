#   https://leetcode.com/problems/lucky-numbers-in-a-matrix


from typing import List


class Solution:
    #   runtime; 144ms, 36.36%
    #   memory; 13.3MB, 100.00%
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        if matrix is None or 0 == len(matrix) or 0 == len(matrix[0]):
            return []
        R, C = len(matrix), len(matrix[0])
        nums = [[None] * C for _ in range(R)]
        for r in range(R):
            i, minRow = 0, matrix[r][0]
            for c in range(C):
                if matrix[r][c] < minRow:
                    i, minRow = c, matrix[r][c]
            nums[r][i] = minRow
        for c in range(C):
            j, maxCol = 0, matrix[0][c]
            for r in range(R):
                if maxCol < matrix[r][c]:
                    j, maxCol = r, matrix[r][c]
            if maxCol == nums[j][c]:
                return [maxCol]
        return []


s = Solution()
data = [([[3,7,8],[9,11,13],[15,16,17]], [15]),
        ([[1,10,4,2],[9,3,8,7],[15,16,17,12]], [12]),
        ([[7,8],[1,2]], [7]),
        ]
for matrix, expected in data:
    real = s.luckyNumbers(matrix)
    for m in matrix:
        print(m)
    print(f'expected {expected} real {real} result {expected == real}')
