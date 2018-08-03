#   https://leetcode.com/problems/to-lower-case

#   https://leetcode.com/problems/to-lower-case/discuss/155292/One-line-solution-without-lower()-in-python3


class Solution:
    #   0.0%?
    def toLowerCase(self, str):
        if str is None or 0 == len(str):
            return str
        def toLower(c):
            if 'A' <= c <= 'Z':
                return chr(ord(c) + ord('a') - ord('A'))
            return c
        return ''.join([toLower(c) for c in str])


s = Solution()
data = [('Hello', 'hello'),
        ('here', 'here'),
        ('LOVELY', 'lovely'),
        ]
for str, expected in data:
    real = s.toLowerCase(str)
    print('{}, expected {}, real {}, result {}'.format(str, expected, real, expected == real))
