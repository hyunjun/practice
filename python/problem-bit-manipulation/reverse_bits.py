#   https://leetcode.com/problems/reverse-bits


class Solution:
    # @param n, an integer
    # @return an integer
    #   33.75%
    def reverseBits0(self, n):
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

    #   https://leetcode.com/explore/featured/card/july-leetcoding-challenge/545/week-2-july-8th-july-14th/3388
    #   runtime; 44ms, 20.96%
    #   memory; 13.8MB, 47.76%
    def reverseBits(self, n: int) -> int:
        numStr = bin(n)[2:]
        numStr = '0' * (32 - len(numStr)) + numStr
        return int(numStr[::-1], 2)


s = Solution()
data = [(43261596, 964176192)]
for n, expected in data:
    real = s.reverseBits(n)
    print('{}, expected {}, real {}, result {}'.format(n, expected, real, expected == real))
