#   https://leetcode.com/problems/binary-number-with-alternating-bits

#   https://leetcode.com/problems/binary-number-with-alternating-bits/solution


class Solution:
    #   100.00%
    def hasAlternateBits(self, n):
        if n in [0, 1]:
            return True
        prev = None
        while n:
            if 1 == n & 0x1:
                if prev is not None and 1 == prev:
                    return False
                prev = 1
            else:
                if prev is not None and 0 == prev:
                    return False
                prev = 0
            n >>= 1
        return True


s = Solution()
data = [(5, True),
        (7, False),
        (11, False),
        (10, True),
        ]
for n, expected in data:
    real = s.hasAlternateBits(n)
    print('{}, expected {}, real {}, result {}'.format(n, expected, real, expected == real))
