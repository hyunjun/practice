#   https://leetcode.com/problems/factorial-trailing-zeroes
#   98.31%


def factorial(n):
    if n <= 0:
        return None
    if n == 1:
        return 1
    result = n
    for i in range(n - 1, 1, -1):
        result *= i
    return result


class Solution:
    def trailingZeroes(self, n):
        cnt, fiveTimes = 0, 5
        while fiveTimes <= n:
            cnt += n // fiveTimes
            fiveTimes *= 5
        return cnt


s = Solution()
data = [(3, 0), (5, 1), (10, 2), (20, 4), (30, 7)]
for n, expected in data:
    real = s.trailingZeroes(n)
    print('{}, (factorial({}) = {}), expected {}, real {}, result {}'.format(n, n, factorial(n), expected, real, expected == real))
