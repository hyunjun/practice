#   https://leetcode.com/problems/check-if-word-is-valid-after-substitutions


class Solution:
    #   runtime; 36ms, 77.33%
    #   memory; 10.9MB, 100.00%
    def isValid(self, S):
        if S is None or 0 == len(S):
            return True
        if 'abc' not in S:
            return False
        return self.isValid(S.replace('abc', ''))


s = Solution()
data = [('aabcbc', True),
        ('abcabcababcc', True),
        ('abccba', False),
        ('cababc', False),
        ]
for S, expected in data:
    real = s.isValid(S)
    print('{}, expected {}, real {}, result {}'.format(S, expected, real, expected == real))
