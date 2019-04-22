#   https://leetcode.com/problems/matrix-cells-in-distance-order

#   https://leetcode.com/problems/matrix-cells-in-distance-order/discuss/279419/Python-one-liner-beats-100-in-time-and-space


class Solution:
    #   runtime; 364ms, 9.38%
    #   memory; 16.4MB, 100.00%
    def allCellsDistOrder(self, R, C, r0, c0):

        def isValid(_r, _c):
            if _r < 0 or _c < 0 or R <= _r or C <= _c:
                return False
            return True

        q, visited, ret = [(r0, c0)], set(), []
        while q:
            r, c = q.pop(0)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            ret.append([r, c])
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if (nr, nc) in visited:
                    continue
                if isValid(nr, nc):
                    q.append((nr, nc))
        return ret


s = Solution()
data = [(1, 2, 0, 0, [[0, 0], [0, 1]]),
        (2, 2, 0, 1, [[0, 1], [0, 0], [1, 1], [1, 0]]),
        (2, 3, 1, 2, [[1, 2], [0, 2], [1, 1], [0, 1], [1, 0], [0, 0]]),
        ]
for R, C, r0, c0, expected in data:
    real = s.allCellsDistOrder(R, C, r0, c0)
    print('{}, {}, {}, {}, expected {}, real {}, result {}'.format(R, C, r0, c0, expected, real, expected == real))
