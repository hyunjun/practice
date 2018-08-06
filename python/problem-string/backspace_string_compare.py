#   https://leetcode.com/problems/backspace-string-compare

#   https://leetcode.com/problems/backspace-string-compare/solution


class Solution:
    #   66.82%
    def backspaceCompare(self, S, T):
        def applyBackspace(s):
            i, stack = 0, []
            while i < len(s):
                if '#' == s[i]:
                    if stack:
                        stack.pop()
                else:
                    stack.append(s[i])
                i += 1
            return ''.join(stack)

        return applyBackspace(S) == applyBackspace(T)


s = Solution()
data = [('ab#c', 'ad#c', True),
        ('ab##', 'c#d#', True),
        ('a##c', '#a#c', True),
        ('a#c', 'b', False),
        ]
for S, T, expected in data:
    real = s.backspaceCompare(S, T)
    print('{}, {}, expected {}, real {}, result {}'.format(S, T, expected, real, expected == real))
