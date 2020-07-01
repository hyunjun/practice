#   https://leetcode.com/problems/arranging-coins


class Solution:
    #   5.44%
    def arrangeCoins(self, n):
        if n <= 0:
            return n
        i = 1
        while True:
            _sum = i * (i + 1) // 2
            if n < _sum:
                return i - 1
            i += 1
        return None

    #   https://leetcode.com/explore/featured/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3377
    #   runtime; 1324ms, 19.62%
    #   memory; 14.1MB, 5.10%
    def arrangeCoins(self, n: int) -> int:
        if n <= 0:
            return 0
        m = 1
        while m * (m + 1) // 2 <= n:
            m += 1
        return m - 1


s = Solution()
data = [(5, 2),
        (8, 3),
        ]
for n, expected in data:
    real = s.arrangeCoins(n)
    print('{}, expected {}, real {}, result {}'.format(n, expected, real, expected == real))
