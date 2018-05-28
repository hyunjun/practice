#   https://leetcode.com/problems/ugly-number
#   90.36%


class Solution:
    def isUgly(self, num):
        if num < 1:
            return False
        for d in [2, 3, 5]:
            while num % d == 0:
                num //= d
        return 1 == num


s = Solution()
data = [(0, False), (1, True), (6, True), (8, True), (14, False)]
for num, expected in data:
    real = s.isUgly(num)
    print('{}, expected {}, real {}, result {}'.format(num, expected, real, expected == real))
