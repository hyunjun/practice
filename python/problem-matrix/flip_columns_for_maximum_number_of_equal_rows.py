#   https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows


from typing import List
from collections import defaultdict


class Solution:
    #   runtime; 316ms, 41.47%
    #   memory; 14.2MB, 100.00%
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        if matrix is None or 0 == len(matrix) or 0 == len(matrix[0]):
            return 0
        grouped = defaultdict(int)
        for row in matrix:
            grouped[' '.join(str(i) for i, v in enumerate(row) if v == row[0])] += 1
        return max(grouped.values())


s = Solution()
data = [([[0, 1], [1, 1]], 1),
        ([[0, 1], [1, 0]], 2),
        ([[0, 0, 0], [0, 0, 1], [1, 1, 0]], 2),
        ([[0, 0, 0], [0, 0, 1], [0, 1, 0]], 1),
        ([[0, 0, 1], [0, 1, 0], [1, 0, 0]], 1),
        ]
for matrix, expected in data:
    for row in matrix:
        print(row)
    real = s.maxEqualRowsAfterFlips(matrix)
    print(f'expected {expected}, real {real}, result {expected == real}')
