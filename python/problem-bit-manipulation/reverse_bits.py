#   https://leetcode.com/problems/reverse-bits
#   33.75%


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bits, bit = [], 0x1
        for i in range(32):
            print('bit {}, n & bit {}'.format(bit, n & bit))
            if 0 == n & bit:
                bits.append('0')
            else:
                bits.append('1')
            bit <<= 1
        print(bits)
        return int(''.join(bits), 2)


s = Solution()
data = [(43261596, 964176192)]
for n, expected in data:
    real = s.reverseBits(n)
    print('{}, expected {}, real {}, result {}'.format(n, expected, real, expected == real))
