#   https://leetcode.com/problems/daily-temperatures

#   https://leetcode.com/problems/daily-temperatures/solution


class Solution:
    #   runtime; 1172ms, 6.60%
    #   memory; 14.5MB, 25.78%
    def dailyTemperatures(self, T):
        if T is None or 0 == len(T):
            return []
        d = {}
        for i, t in enumerate(T):
            if t in d:
                d[t].append(i)
            else:
                d[t] = [i]
        res = []
        for i, t in enumerate(T):
            indices = d[t]
            d[t].remove(i)
            if 0 == len(d[t]):
                del d[t]
            nIdx = None
            for n in range(t + 1, 101):
                if n in d:
                    indices = d[n]
                    if nIdx is None:
                        nIdx = indices[0] - i
                    else:
                        nIdx = min(nIdx, indices[0] - i)
            if nIdx is None:
                res.append(0)
            else:
                res.append(nIdx)
        return res


s = Solution()
data = [([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ]
for T, expected in data:
    real = s.dailyTemperatures(T)
    print('{}, expected {}, real {}, result {}'.format(T, expected, real, expected == real))
