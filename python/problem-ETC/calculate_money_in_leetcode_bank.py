#   https://leetcode.com/problems/calculate-money-in-leetcode-bank


class Solution:
    #   runtime; 28ms, 95.75%
    #   memory; 14.1MB, 91.51%
    def totalMoney(self, n: int) -> int:
        a, b = n // 7, n % 7
        return 28 * a + 7 * (a - 1) * a // 2 + a * b + b * (b + 1) // 2


s = Solution()
data = [(4, 10),
        (10, 37),
        (20, 96),
        ]
for n, expect in data:
    real = s.totalMoney(n)
    print(f'{n} expect {expect} real {real} result {expect == real}')
