#   https://leetcode.com/problems/fibonacci-number


class Solution:
    #   runtime; 52ms, 34.18%
    #   memory; 6.4MB, 88.56%
    def fib(self, N):
        if 0 == N:
            return 0
        if 1 == N:
            return 1
        f_n, f_n_1, f_n_2 = None, 1, 0
        for i in range(2, N + 1):
            f_n = f_n_1 + f_n_2
            f_n_2 = f_n_1
            f_n_1 = f_n
        return f_n


s = Solution()
data = [(2, 1),
        (3, 2),
        (4, 3),
        ]
for N, expected in data:
    real = s.fib(N)
    print('{}, expected {}, real {}, result {}'.format(N, expected, real, expected == real))
