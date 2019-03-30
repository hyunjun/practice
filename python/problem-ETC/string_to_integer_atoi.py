#   https://leetcode.com/problems/string-to-integer-atoi


class Solution:
    #   runtime; 56ms, 94.11%
    #   memory; 13.4MB, 5.00%
    def myAtoi(self, s):
        if s is None or 0 == len(s):
            return 0
        s = s.strip()
        if 0 == len(s):
            return 0
        isNegative = False
        if '-' == s[0]:
            isNegative = True
            s = s[1:]
        elif '+' == s[0]:
            s = s[1:]
        if 0 == len(s) or s[0] < '0' or '9' < s[0]:
            return 0
        r = 0
        while r < len(s) and '0' <= s[r] <= '9':
            r += 1
        s = s[:r]
        if '.' in s:
            n = float(s)
        else:
            n = int(s)
        if isNegative:
            n *= -1
        _min, _max = -2 ** 31, 2 ** 31 - 1
        if n < _min:
            n = _min
        elif _max < n:
            n = _max
        return n


s = Solution()
data = [('42', 42),
        ('   -42', -42),
        ('4193 with words', 4193),
        ('words and 987', 0),
        ('-91283472332', -2147483648),
        ('3.14159', 3.14159),
        ('-', 0),
        (' ', 0),
        ('  -0012a42', -12),
        ('+1', 1),
        ]
for _s, expected in data:
    real = s.myAtoi(_s)
    print('{}, expected {}, real {}, result {}'.format(_s, expected, real, expected == real))
