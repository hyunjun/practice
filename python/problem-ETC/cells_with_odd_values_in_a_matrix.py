#   https://leetcode.com/problems/cells-with-odd-values-in-a-matrix


class Solution(object):
    #   runtime; 36ms, 52.66%
    #   memory; 11.7MB, 100.00%
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        matrix = [[0 for _ in range(m)] for _ in range(n)]
        for r, c in indices:
            for col in range(m):
                matrix[r][col] += 1
            for row in range(n):
                matrix[row][c] += 1
        return sum([1 if matrix[r][c] % 2 == 1 else 0 for r in range(n) for c in range(m)])


s = Solution()
data = [(2, 3, [[0,1],[1,1]], 6),
        (2, 2, [[1,1],[0,0]], 0),
        ]
for n, m, indices, expected in data:
    real = s.oddCells(n, m, indices)
    print(f'{n}, {m}, {indices}, expected {expected}, real {real}, result {expected == real}')
