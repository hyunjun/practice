#   https://leetcode.com/problems/hamming-distance

#   https://leetcode.com/problems/hamming-distance/discuss/144971/simple-python-answer
#   https://leetcode.com/problems/hamming-distance/discuss/144245/Simple-Python-3-Solution


class Solution:
    #   49.53%
    def hammingDistance0(self, x, y):
        n, cnt, b = x ^ y, 0, 0x1
        for i in range(32):
            if 1 == n & 0x1:
                cnt += 1
            n >>= 1
        return cnt

    #   https://leetcode.com/explore/featured/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3381
    #   runtime; 40ms, 16.11%
    #   memory; 13.8MB, 55.96%
    def hammingDistance(self, x: int, y: int) -> int:
        cnt, x, y = 0, bin(x)[2:], bin(y)[2:]
        if len(x) < len(y):
            x = '0' * (len(y) - len(x)) + x
        elif len(x) > len(y):
            y = '0' * (len(x) - len(y)) + y
        for i in range(len(y)):
            if x[i] != y[i]:
                cnt += 1
        return cnt
            

s = Solution()
data = [(1, 4, 2),
        (5, 11, 3),
        (11, 23, 3),
        (2947, 3391, 7),
        ]
for x, y, expected in data:
    real = s.hammingDistance(x, y)
    print('{}, {}, expected {}, real {}, result {}'.format(x, y, expected, real, expected == real))
