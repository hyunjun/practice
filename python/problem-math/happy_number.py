#   https://leetcode.com/problems/happy-number
#   21.14%


import math


class Solution:
    def isHappy(self, n):
        digitSum, digitSumSet = 0, set()
        while 1 != digitSum:
            digitSum = 0
            while 0 < n:
                digitSum += (int)(math.pow(n % 10, 2))
                n //= 10
            print(digitSum)
            if digitSum in digitSumSet:
                return False
            digitSumSet.add(digitSum)
            n = digitSum
        return True


s = Solution()
data = [(19, True), (29, False)]
for num, expected in data:
    real = s.isHappy(num)
    print('{}, expected {}, real {}, result {}'.format(num, expected, real, expected == real))
