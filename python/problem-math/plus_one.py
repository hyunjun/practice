#   https://leetcode.com/problems/plus-one
#   99.94%


class Solution:
    def plusOne(self, digits):
        return [int(i) for i in str(int(''.join([str(d) for d in digits])) + 1)]


s = Solution()
data = [([1, 2, 3], [1, 2, 4]), ([4, 3, 2, 1], [4, 3, 2, 2])]
for digits, expected in data:
    real = s.plusOne(digits)
    print('{}, expected {}, real {}, result {}'.format(digits, expected, real, expected == real))
