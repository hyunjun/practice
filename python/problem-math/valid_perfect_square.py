#   https://leetcode.com/problems/valid-perfect-square
#   96.63%

#   https://leetcode.com/problems/valid-perfect-square/discuss/111844/Only-three-lines-in-python

import math


class Solution:

    #   Runtime Error   Memory Error
    def isPerfectSquare0(self, num):
        if 0 == num:
            return False
        if 1 == num:
            return True
        for i in range(2, num // 2 + 1):
            if 2.0 == math.log(num, i):
                return True
        return False

    #   Wrong Answer for (100, True)
    def isPerfectSquare1(self, num):
        if 0 == num:
            return False
        if 1 == num:
            return True
        i = num // 2
        mini, maxi, s = 2, num // 2, set()
        while i not in s and mini <= i <= maxi:
            cand = math.log(num, i)
            s.add(i)
            print('i {}, math.log({}, {}) = {}'.format(i, num, i, cand))
            if 2.0 == cand:
                return True
            elif 2.0 < cand:
                i = (i + maxi) // 2
                if i in s:
                    i = (i + maxi) // 2
            else:
                i = (mini + i) // 2
                if i in s:
                    i = (mini + i) // 2
        return False

    #   runtime; 30ms, 9.88%
    def isPerfectSquare2(self, num):
        if 0 == num:
            return False
        if 1 == num:
            return True
        mini, maxi, s = 2, num // 2, set()
        i = maxi
        minCand, maxCand = math.log(num, mini), math.log(num, maxi)
        print('{} -> min cand {}, {} -> max cand {}'.format(mini, minCand, maxi, maxCand))
        while i not in s and mini <= i <= maxi:
            cand = math.log(num, i)
            s.add(i)
            print('i {}, math.log({}, {}) = {}'.format(i, num, i, cand))
            if 2.0 == cand:
                return True
            elif 2.0 < cand:
                mini = i
                i = (i + maxi) // 2
                if i in s:
                    mini = i
                    i = (i + maxi) // 2
            else:
                maxi = i
                i = (mini + i) // 2
                if i in s:
                    maxi = i
                    i = (mini + i) // 2
        return False

    #   https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3324
    #   runtime; 28ms, 75.96%
    #   memory; 13.6MB
    def isPerfectSquare(self, num: int) -> bool:
        if num < 1:
            return False
        if num == 1:
            return True
        l, r = 1, num // 2
        while l <= r:
            m = (l + r) // 2
            cand = m ** 2
            if cand == num:
                return True
            if cand < num:
                l = m + 1
            else:
                r = m - 1
        return False


s = Solution()
data = [(4, True), (9, True), (16, True), (14, False), (100, True), (2147483647, False)]
#data = [(4, True)]
for num, expected in data:
    real = s.isPerfectSquare(num)
    print('{}, expected {}, real {}, result {}'.format(num, expected, real, expected == real))
