#   https://leetcode.com/problems/plus-one


from typing import List


class Solution:
    #   runtime; 36ms, 43.29%
    def plusOne0(self, digits):
        return [int(i) for i in str(int(''.join([str(d) for d in digits])) + 1)]

    #   https://leetcode.com/explore/featured/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3382
    #   runtime; 32ms, 70.54%
    #   memory; 13.7MB, 77.94%
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry
            if digits[i] == 10:
                carry, digits[i] = 1, 0
            else:
                carry = 0
        if carry == 1:
            digits.insert(0, 1)
        return digits


s = Solution()
data = [([1, 2, 3], [1, 2, 4]),
        ([4, 3, 2, 1], [4, 3, 2, 2]),
        ]
for digits, expect in data:
    real = s.plusOne(digits)
    print('{}, expect {}, real {}, result {}'.format(digits, expect, real, expect == real))
