#   https://leetcode.com/problems/fibonacci-number


class Solution:
    #   runtime; 52ms, 34.18%
    #   memory; 6.4MB, 88.56%
    def fib0(self, N):
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

    #   https://leetcode.com/explore/featured/card/recursion-i/255/recursion-memoization/1661
    #   runtime; 28ms, 75.49%
    #   memory; 13.7MB
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1
        n0, n1, n = 0, 1, 1
        for _ in range(2, N + 1):
            n = n0 + n1
            n0 = n1
            n1 = n
        return n

s = Solution()
data = [(2, 1),
        (3, 2),
        (4, 3),
        ]
for N, expected in data:
    real = s.fib(N)
    print('{}, expected {}, real {}, result {}'.format(N, expected, real, expected == real))
