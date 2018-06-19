#   https://leetcode.com/problems/sum-of-two-integers

#   https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary:-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently


class Solution:

    #   Wrong Answer
    def getSum0(self, a, b):
        if 0 == a:
            return b
        if 0 == b:
            return a
        isANegative, isBNegative = False, False
        if a < 0:
            a = ~(a - 1)
            isANegative = True
        if b < 0:
            b = ~(b - 1)
            isBNegative = True
        carry, result = 0, 0
        if isANegative == isBNegative:
            for i in range(32):
                bits = sorted([a & 0x1, b & 0x1, carry])
                if bits == [1, 1, 1]:
                    carry = 1
                    result |= 0x1 << i
                elif bits == [0, 1, 1]:
                    carry = 1
                elif bits == [0, 0, 1]:
                    carry = 0
                    result |= 0x1 << i
                else:
                    carry = 0
                a >>= 1
                b >>= 1
        else:
            if isANegative:
                a, b = b, a
            print(a, b)
            for i in range(32):
                bitA, bitB = a & 0x1, b & 0x1
                result |= (carry ^ bitA ^ bitB) << i
                print('carry {}, {}, {}, {}'.format(carry, bitA, bitB, carry ^ bitA ^ bitB), result)
                if (0 == bitA and 1 == bitB) or (1 == carry and bitA == bitB):
                    carry = 1
                else:
                    carry = 0
                a >>= 1
                b >>= 1
        if isANegative & isBNegative:
            return -result
        return result

    #   https://stackoverflow.com/questions/37135106/what-is-good-way-to-negate-an-integer-in-binary-operation-in-python
    def __init__(self):
        self.BIT_LEN = 8
        self.NUM_INTS = 1 << self.BIT_LEN
        self.BIT_MASK = self.NUM_INTS - 1
        self.HIGH_BIT = 1 << (self.BIT_LEN - 1)

    def to2c(self, n):
        return n & self.BIT_MASK

    def from2c(self, bits):
        bits &= self.BIT_MASK
        if bits & self.HIGH_BIT:
            return bits - self.NUM_INTS
        return bits

    #   83.70%
    def getSum1(self, a, b):
        if 0 == a:
            return b
        if 0 == b:
            return a
        isANegative, isBNegative = False, False
        if a < 0:
            a = self.to2c(a)
            isANegative = True
        if b < 0:
            b = self.to2c(b)
            isBNegative = True
        carry, res = 0, 0
        for i in range(32):
            bitA, bitB = a & 0x1, b & 0x1
            bits = sorted([bitA, bitB, carry])
            if [1, 1, 1] == bits:
                carry = 1
                res |= 0x1 << i
            elif [0, 1, 1] == bits:
                carry = 1
            elif [0, 0, 1] == bits:
                carry = 0
                res |= 0x1 << i
            else:
                carry = 0
            a >>= 1
            b >>= 1
        return self.from2c(res)

    #   https://leetcode.com/problems/sum-of-two-integers/discuss/140525/Python-3
    def getSum(self, a, b):
        if a == -b:
            return 0
        if abs(a) > abs(b):
            a, b = b, a
        if a < 0:
            return -self.getSum(-a, -b)
        while b:
            c = a & b
            a ^= b
            b = c << 1
        return a


s = Solution()
data = [(1, 2, 3),
        (10, 20, 30),
        (-12, -8, -20),
        (14, -2, 12),
        (6, -3, 3),
        (0, -1, -1),
        (-1, -2, -3),
        (-14, 16, 2),
        (-16, 14, -2),
        (2147483647, -2147483648, -1),
        ]
for a, b, expected in data:
    real = s.getSum(a, b)
    print('{} + {}, expected {}, real {}, result {}'.format(a, b, expected, real, expected == real))
