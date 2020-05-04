#   https://leetcode.com/problems/number-complement

#   https://leetcode.com/problems/number-complement/discuss/151287/Python-code


class Solution:
    #   runtime; 44ms, 14.37%
    def findComplement0(self, num):
        res = []
        while num:
            if num & 0x1:
                res.append('0')
            else:
                res.append('1')
            num >>= 1
        return int(''.join(res[::-1]), 2)

    #   https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3319
    #   runtime; 24ms, 89.09%
    #   memory; 14MB
    def findComplement(self, num: int) -> int:
        return int(''.join(['0' if b == '1' else '1' for b in bin(num)[2:]]), 2)


s = Solution()
data = [(5, 2),
        (1, 0),
        ]
for num, expected in data:
    real = s.findComplement(num)
    print('{}, expected {}, real {}, result {}'.format(num, expected, real, expected == real))
