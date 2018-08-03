#   https://leetcode.com/problems/1-bit-and-2-bit-characters

#   https://leetcode.com/problems/1-bit-and-2-bit-characters/solution


class Solution:
    #   Wrong Answer
    def isOneBitCharacter0(self, bits):
        return (1 == len(bits) and bits[0] == 0) or (1 < len(bits) and bits[-2:] == [0, 0])

    #   0.0%
    def isOneBitCharacter(self, bits):
        if 1 == len(bits):
            return bits[0] == 0
        elif 1 < len(bits):
            if bits[0] == 1:
                return self.isOneBitCharacter(bits[2:])
            return self.isOneBitCharacter(bits[1:])
        return False


s = Solution()
data = [([1, 0, 0], True),
        ([1, 1, 0], True),
        ([1, 1, 1, 0], False),
        ([1, 0, 0, 0, 1, 1, 0], True),
        ]
for bits, expected in data:
    real = s.isOneBitCharacter(bits)
    print('{}, expected {}, real {}, result {}'.format(bits, expected, real, expected == real))
