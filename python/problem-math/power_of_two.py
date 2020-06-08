#   https://leetcode.com/problems/power-of-two

#   https://leetcode.com/problems/power-of-two/discuss/131043/python-bitwise-solution-beat-97
#   https://leetcode.com/problems/power-of-two/discuss/676846/Math-or-Bit-or-Recursive-or-1-Line-Code-or-Detailed-Explanations


import math


class Solution:
    #   runtime; 44ms, 72.31%
    def isPowerOfTwo0(self, n):
        if n <= 0:
            return False
        times = 1
        print('n {} times {}'.format(n, times))
        while times < n and n % times == 0:
            times *= 2
            print('n {} times {}'.format(n, times))
        print('n {} times {}'.format(n, times))
        return n % times == 0

    #   https://leetcode.com/explore/featured/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3354
    #   runtime; 28ms, 82.51%
    #   memory; 13.8MB
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return 2 ** int(math.log(n, 2)) == n


s = Solution()
data = [(0, False),
        (1, True),
        (16, True),
        (-16, False),
        (218, False),
        ]
for n, expected in data:
    real = s.isPowerOfTwo(n)
    print('{}, expected {}, real {}, result {}'.format(n, expected, real, expected == real))
