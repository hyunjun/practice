#   https://leetcode.com/problems/hamming-distance
#   49.53%

#   https://leetcode.com/problems/hamming-distance/discuss/144971/simple-python-answer
#   https://leetcode.com/problems/hamming-distance/discuss/144245/Simple-Python-3-Solution


class Solution:
    def hammingDistance(self, x, y):
        n, cnt, b = x ^ y, 0, 0x1
        for i in range(32):
            if 1 == n & 0x1:
                cnt += 1
            n >>= 1
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
