#   https://leetcode.com/problems/range-addition-ii

#   https://leetcode.com/problems/range-addition-ii/solution


class Solution:
    #   Memory Limit Exceeded
    def maxCount0(self, m, n, ops):
        M = [[0] * n for _ in range(m)]
        for op in ops:
            for r in range(m):
                if op[0] <= r:
                    continue
                for c in range(n):
                    if op[1] <= c:
                        continue
                    M[r][c] += 1
        maxVal, cnt = M[0][0], 0
        for r in range(m):
            for c in range(n):
                if maxVal == M[r][c]:
                    cnt += 1
        return cnt

    #   54.11%
    def maxCount(self, m, n, ops):
        if 0 == len(ops):
            return m * n
        minR = min([r for r, _ in ops])
        minC = min([c for _, c in ops])
        return minR * minC


s = Solution()
data = [(3, 3, [[2, 2], [3, 3]], 4),
        ]
for m, n, ops, expected in data:
    real = s.maxCount(m, n, ops)
    print('{}, {}, {}, expected {}, real {}, result {}'.format(m, n, ops, expected, real, expected == real))
