#   https://leetcode.com/problems/happy-number


import math


class Solution:
    #   21.14%
    def isHappy0(self, n):
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

    #   https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3284
    #   runtime; 36ms, 42.10%
    #   memory; 13.8MB
    def isHappy(self, n: int) -> bool:
        res, s = 0, set()
        while res != 1:
            res = 0
            for c in str(n):
                c = int(c)
                res += c * c
            if res in s:
                return False
            s.add(res)
            n = res
        return True


s = Solution()
data = [(19, True), (29, False)]
for num, expected in data:
    real = s.isHappy(num)
    print('{}, expected {}, real {}, result {}'.format(num, expected, real, expected == real))
