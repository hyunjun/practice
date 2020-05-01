#   https://leetcode.com/explore/featured/card/recursion-i/256/complexity-analysis/2380


class Solution:
    #   runtime; 244ms
    #   memory; 13.7MB
    def myPow(self, x: float, n: int) -> float:
        if not (-100 < x < 100) or not (-2 ** 31 <= n <= 2 ** 31 - 1):
            return 0
        if n == 0:
            return 0 if x == 0 else 1
        if x == 1:
            return 1
        if x == -1:
            return 1 if n % 2 == 0 else -1
        if n < 0:
            x, n = 1 / x, -n
        res = 1
        for _ in range(n):
            res *= x
            if -0.00001 < res < 0.00001:
                return 0
        return res


s = Solution()
data = [(2.0, 10, 1024.0),
        (2.1, 3, 9.26100),
        (2.0, -2, 0.25),
        (-2.0, 2, 4),
        (0.00001, 2147483647, 0),
        ]
for x, n, expected in data:
    real = s.myPow(x, n)
    print(f'{x} {n} expected {expected} real {real} result {expected == real}')
