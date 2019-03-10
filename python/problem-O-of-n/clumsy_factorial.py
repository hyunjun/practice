#   https://leetcode.com/problems/clumsy-factorial


class Solution:
    #   runtime; 72ms, 100.00%
    #   memory; 13.1MB, 100.00%
    def clumsy(self, N):
        if N <= 1:
            return N
        opIdx, cur, res = 0, N, []
        for i in range(N - 1, 0, -1):
            opIdx %= 4
            if 0 == opIdx:
                cur *= i
            elif 1 == opIdx:
                cur = (int)(cur / i)
            elif 2 == opIdx:
                cur += i
            elif 3 == opIdx:
                res.append(cur)
                cur = -i
            print(cur, res)
            opIdx += 1
        res.append(cur)
        print(res)
        return sum(res)


s = Solution()
data = [(4, 7),
        (10, 12),
        ]
for N, expected in data:
    real = s.clumsy(N)
    print('{}, expected {}, real {}, result {}'.format(N, expected, real, expected == real))
