#   https://leetcode.com/problems/convert-a-number-to-hexadecimal
#   85.58%

#   https://leetcode.com/problems/convert-a-number-to-hexadecimal/discuss/89261/easy-10-line-python-solution-with-inline-explanation


class Solution:
    d = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
         10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'
         }

    def twosComplement(self, num):
        #   https://en.wikipedia.org/wiki/Two%27s_complement#Converting_to_two's_complement_representation
        #mask = 2**(32 - 1)
        #return -(num & mask) + (num & ~mask)
        #bitint = int('{0:b}'.format(num))
        #return int(str(~bitint + 1), 2)
        res, mask = [], 0x1
        for i in range(32):
            if num & mask:
                res.append('1')
            else:
                res.append('0')
            mask <<= 1
        return int(''.join(res[::-1]), 2)

    def toHex(self, num):
        if 0 == num:
            return '0'
        if num < 0:
            num = self.twosComplement(num)
            print(num)
        res = []
        for i in range(7, -1, -1):
            tmp = 16 ** i
            dividend = num // tmp
            print('num {}, tmp {}, num // tmp {}'.format(num, tmp, dividend))
            res.append(Solution.d[dividend])
            num -= dividend * tmp
        for i, r in enumerate(res):
            if '0' != r:
                return ''.join(res[i:])
        return None


s = Solution()
data = [(26, '1a'), (4294967295, 'ffffffff'), (-1, 'ffffffff')]
for num, expected in data:
    real = s.toHex(num)
    print('{}, expected {}, real {}, result {}'.format(num, expected, real, expected == real))
