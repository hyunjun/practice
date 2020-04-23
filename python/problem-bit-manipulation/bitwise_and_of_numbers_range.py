#   https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3308


from functools import reduce


class Solution:
    #   Time Limit Exceeded
    def rangeBitwiseAnd0(self, m: int, n: int) -> int:
        if not (0 <= m < 2 ** 31) or not (0 <= n < 2 ** 31):
            return 0
        s, b = m, n
        if s > b:
            s, b = n, m
        if 0 == s:
            return 0
        return reduce(lambda a, b: a & b, range(s, b + 1))

    #   Time Limit Exceeded
    def rangeBitwiseAnd1(self, m: int, n: int) -> int:
        if not (0 <= m < 2 ** 31) or not (0 <= n < 2 ** 31):
            return 0
        s, b = m, n
        if s > b:
            s, b = n, m
        if 0 == s:
            return 0
        for i in range(s + 1, b + 1):
            s &= i
            if 0 == s:
                return 0
        return s

    #   runtime; 144ms
    #   memory; 14MB
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if not (0 <= m < 2 ** 31) or not (0 <= n < 2 ** 31):
            return 0
        s, b = m, n
        if s > b:
            s, b = n, m
        if 0 == s:
            return 0
        bitNums = [2 ** i if s <= 2 ** i < b else 0 for i in range(0, 32)]
        if all(bitNum == 0 for bitNum in bitNums):
            for i in range(s + 1, b + 1):
                s &= i
                if 0 == s:
                    return 0
            return s
        bitNums = [b for b in bitNums if b]
        ret = s
        for bitNum in bitNums:
            for i in range(s + 1, b + 1):
                i &= bitNum
                if 0 == i:
                    return 0
            ret &= i
        return ret


s = Solution()
data = [(2, 3, 2),
        (5, 7, 4),
        (0, 1, 0),
        (0, 2147483647, 0),
        (20000, 2147483647, 0),
        (600000000, 2147483645, 0),
        ]
for m, n, expected in data:
    real = s.rangeBitwiseAnd(m, n)
    print(f'{m} {n} expected {expected} real {real} result {expected == real}')
