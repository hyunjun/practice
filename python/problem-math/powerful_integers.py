#   https://leetcode.com/problems/powerful-integers

#   https://leetcode.com/problems/powerful-integers/solution


from itertools import product

class Solution:
    #   Time Limit Exceeded
    def powerfulIntegers0(self, x, y, bound):
        def getMax(n):
            i = 0
            while n ^ i <= bound:
                i += 1
            return i
        s, xMax, yMax = set(), getMax(x), getMax(y)
        for i, j in product(range(xMax), range(yMax)):
            c = x ** i + y ** j
            if c <= bound:
                s.add(c)
        return list(s)

    #   904ms, 3.16%
    def powerfulIntegers(self, x, y, bound):
        def getMax(n):
            i = 0
            while n ^ i <= bound:
                i += 1
            return i
        s, xMax, yMax = set(), getMax(x), getMax(y)
        for i in range(xMax):
            c1 = x ** i
            if bound <= c1:
                break
            for j in range(yMax):
                c2 = y ** j
                if bound <= c2:
                    break
                c = c1 + c2
                if c <= bound:
                    s.add(c)
        return list(s)


s = Solution()
data = [(2, 3, 10, [2, 3, 4, 5, 7, 9, 10]),
        (3, 5, 15, [2, 4, 6, 8, 10, 14]),
        (4, 100, 100, [17, 2, 5, 65]),
        (40, 40, 10000, [3200, 1601, 2, 1640, 41, 80]),
        ]
for x, y, bound, expected in data:
    real = s.powerfulIntegers(x, y, bound)
    print('{}, {}, {}, expected {}, real {}, result {}'.format(x, y, bound, expected, real, sorted(expected) == sorted(real)))
