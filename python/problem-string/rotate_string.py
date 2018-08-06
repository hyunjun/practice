#   https://leetcode.com/problems/rotate-string

#   https://leetcode.com/problems/rotate-string/solution


class Solution:
    #   86.01%
    def rotateString(self, A, B):
        if (A is None or 0 == len(A)) and (B is None or 0 == len(B)):
            return True
        if A is None or 0 == len(A) or B is None or 0 == len(B) or len(A) != len(B):
            return False
        return B in 2 * A


s = Solution()
data = [('abcde', 'cdeab', True),
        ('abcde', 'abced', False),
        ('', '', True),
        ]
for A, B, expected in data:
    real = s.rotateString(A, B)
    print('{}, {}, expected {}, real {}, result {}'.format(A, B, expected, real, expected == real))
