#   https://leetcode.com/problems/reverse-integer/
#   78.62%

class Solution:
    MIN_INT = -2147483648
    MAX_INT = 2147483647

    def reverse(self, x):
        s = str(x)
        isNegative = False
        if s[0] == '-':
            isNegative = True
            s = s[1:]
        s = s[::-1]
        nonZeroIndex = 0
        while nonZeroIndex < len(s) and s[nonZeroIndex] == '0':
            nonZeroIndex += 1
        if nonZeroIndex == len(s):
            return 0
        s = s[nonZeroIndex:]
        if isNegative:
            s = '-' + s
        s = int(s)
        if Solution.MIN_INT <= s <= Solution.MAX_INT:
            return s
        return 0


cases = [(123, 321), (-123, -321), (120, 21), (-120, -21), (0, 0), (1534236469, 0)]
s = Solution()
for x, expected in cases:
    real = s.reverse(x)
    print('inp: {}\texpected: {}\treal: {}\tresult: {}'.format(x, expected, real, expected == real))
