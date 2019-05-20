#   https://leetcode.com/problems/combinations


class Solution:
    #   recur 호출 전 length check if 추가로 속도 대폭 향상
    #   runtime; 844ms, 9.12% -> 144ms, 76.76%
    #   memory; 15MB, 50.86% -> 14.9MB, 76.47%
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
                    if k <= len(prev) + len(cur[i + 1:]):
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
