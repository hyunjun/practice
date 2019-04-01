#   https://leetcode.com/problems/binary-prefix-divisible-by-5


class Solution:
    #   Time Limit Exceeded
    def prefixDivBy5_0(self, A):
        res = []
        for i in range(len(A)):
            n = int(''.join([str(A[j]) for j in range(i + 1)]), 2)
            res.append(True if 0 == n % 5 else False)
        return res

    #   runtime; 360ms, 23.05%
    #   memory; 16.4MB, 100.00%
    def prefixDivBy5(self, A):
        res, prev = [], 0
        for i in range(len(A)):
            n = prev + A[i]
            res.append(True if 0 == n % 5 else False)
            prev = n * 2
        return res


s = Solution()
data = [([0, 1, 1], [True, False, False]),
        ([1, 1, 1], [False, False, False]),
        ([0, 1, 1, 1, 1, 1], [True, False, False, False, True, False]),
        ([1, 1, 1, 0, 1], [False, False, False, False, False]),
        ]
for A, expected in data:
    real = s.prefixDivBy5(A)
    print('{}, expected {}, real {}, result {}'.format(A, expected, real, expected == real))
