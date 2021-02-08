#   https://leetcode.com/problems/perfect-squares


from collections import defaultdict
import math


class Solution:
    #   Time Limit Exceeded
    def numSquares0(self, n: int) -> int:

        d = defaultdict(int)
        def squares(m):
            if m < 0:
                return -1
            if m == 0:
                return 0
            if m in d:
                return d[m]
            sqrtNum = int(math.sqrt(m))
            if m == sqrtNum ** 2:
                d[m] = 1
                return 1
            subSum = float('inf')
            for x in range(sqrtNum, 1, -1):
                nextSum = squares(m - x ** 2)
                if nextSum < 0 or subSum < 1 + nextSum:
                    continue
                subSum = 1 + nextSum
            d[m] = subSum
            return subSum

        return squares(n)

    def numSquares1(self, n: int) -> int:

        q = [(n, 0)]
        while q:
            num, count = q.pop(0)
            if 0 == num:
                return count
            sqrtNum = int(math.sqrt(num))
            for x in range(sqrtNum, 1, -1):
                q.append((num - x ** 2, count + 1))
        return -1

    def numSquares2(self, n: int) -> int:

        d = defaultdict(int)
        def squares(m):
            if m < 4:
                return m
            if m in d:
                return d[m]
            cnt = m
            for i in range(int(math.sqrt(m)), 0, -1):
                cnt = min(cnt, squares(m - i ** 2) + 1)
            d[m] = cnt
            return cnt

        return squares(n)

    #   https://leetcode.com/problems/perfect-squares/discuss/707517/Python-no-DP-O(N)
    #   runtime; 88ms, 93.44%
    #   memory; 13.8MB, 89.56%
    def numSquares(self, n: int) -> int:
        if n < 4:
            return n

        i, d = 1, set()
        while i ** 2 <= n:
            d.add(i ** 2)
            i += 1

        if n in d:
            return 1

        for num in d:
            if n - num in d:
                return 2

        for n1 in d:
            for n2 in d:
                if n - n1 - n2 in d:
                    return 3

        return 4


s = Solution()
data = [(1, 1),
        (4, 1),
        (12, 3),
        (13, 2),
        (194, 2),
        (1868, 3),
        (6366, 3),
        (6616, 3),
        ]
for n, expect in data:
    real = s.numSquares(n)
    print(f'{n} expect {expect} real {real} result {expect == real}')
