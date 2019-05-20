#   https://leetcode.com/problems/combinations


class Solution:
    #   runtime; 844ms, 9.12%
    #   memory; 15MB, 50.86%
    def combine(self, n, k):
        if n == 0 or k == 0:
            return []

        self.res = []
        def recur(prev, cur):
            if len(prev) == k:
                self.res.append(prev)
            else:
                for i, c in enumerate(cur):
                    prev.append(c)
                    recur(prev[:], cur[i + 1:])
                    prev.pop()
        recur([], [i for i in range(1, n + 1)])
        return self.res


s = Solution()
data = [(4, 2, [[2,4], [3,4], [2,3], [1,2], [1,3], [1,4]]),
        ]
for n, k, expected in data:
    real = s.combine(n, k)
    print('{}, {}, expected {}, real {}, result {}'.format(n, k, expected, real, sorted(expected) == sorted(real)))
