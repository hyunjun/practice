#   https://leetcode.com/problems/base-7

#   https://leetcode.com/problems/base-7/discuss/155385/Python-24-ms


class Solution:
    #   0.0%
    def convertToBase7(self, num):
        if -7 < num < 7:
            return str(num)
        isNegative = False
        if num < 0:
            isNegative = True
            num = -num
        seven = 1
        while seven <= num:
            seven *= 7
        seven //= 7
        res = []
        while 0 < seven:
            a, b = divmod(num, seven)
            res.append(str(a))
            seven //= 7
            num = b
        if isNegative:
            res.insert(0, '-')
        return ''.join(res)


s = Solution()
data = [(100, '202'),
        (-7, '-10'),
        ]
for num, expected in data:
    real = s.convertToBase7(num)
    print('{}, expected {}, real {}, result {}'.format(num, expected, real, expected == real))
