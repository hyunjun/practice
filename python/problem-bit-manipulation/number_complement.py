#   https://leetcode.com/problems/number-complement

#   https://leetcode.com/problems/number-complement/discuss/151287/Python-code


class Solution:
    #   14.37%
    def findComplement(self, num):
        res = []
        while num:
            if num & 0x1:
                res.append('0')
            else:
                res.append('1')
            num >>= 1
        return int(''.join(res[::-1]), 2)


s = Solution()
data = [(5, 2),
        (1, 0),
        ]
for num, expected in data:
    real = s.findComplement(num)
    print('{}, expected {}, real {}, result {}'.format(num, expected, real, expected == real))
