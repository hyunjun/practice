# https://leetcode.com/problems/sqrtx


class Solution:
    def mySqrt0(self, x):
        if x == 0 or x == 1:
            return x
        if x == 2 or x == 3:
            return 1

        for i in range(2, x // 2 + 1):
            if i * i == x:
                return i
            if x < i * i:
                return i - 1
        return i

    def mySqrt1(self, x):
        def _mysqrt_recur(l, r, target):
            mid = (l + r) / 2
            if abs(mid * mid - target) < 0.00001:
                return mid
            elif mid * mid < target:
                return _mysqrt_recur(mid, r, target)
            return _mysqrt_recur(l, mid, target)
        return _mysqrt_recur(0, x, x)

    #   96ms, 21.33%
    def mySqrt(self, x):
        if 0 == x or 1 == x:
            return x
        l, r = 0, x
        while True:
            mid = (l + r) / 2
            if abs(mid * mid - x) < 0.00001:
                break
            if mid * mid < x:
                l = mid
            else:
                r = mid
        return int(mid)


class Solution2:
    # newton's method
    def mySqrt(self, x):
        r = x
        while r * r > x:
            r = (r + x / r) / 2
        return r


s, s2 = Solution(), Solution2()
for x in [2, 3, 4, 9, 8, 5, 15, 98, 10000092, 2147395599]:
  expected, real = s2.mySqrt(x), s.mySqrt(x)
  print('{}\texpected {}\treal {}\tresult {}'.format(x, expected, real, expected == real))
