#   https://leetcode.com/problems/arranging-coins
#   5.44%


class Solution:
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


s = Solution()
data = [(5, 2), (8, 3)]
for n, expected in data:
    real = s.arrangeCoins(n)
    print('{}, expected {}, real {}, result {}'.format(n, expected, real, expected == real))
