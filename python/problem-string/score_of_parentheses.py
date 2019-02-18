#   https://leetcode.com/problems/score-of-parentheses

#   https://leetcode.com/problems/score-of-parentheses/solution


class Solution:
    #   runtime; 36ms, 81.00%
    #   memory; 12.5MB, 100.00%
    def scoreOfParentheses(self, S):
        if S is None or 0 == len(S):
            return 0
        stack = []
        for p in S:
            if '(' == p:
                stack.append(p)
            else:
                if '(' == stack[-1]:
                    stack.pop()
                    stack.append(1)
                else:
                    n = stack.pop()
                    while '(' != stack[-1]:
                        n += stack.pop()
                    if '(' == stack[-1]:
                        n *= 2
                        stack.pop()
                    stack.append(n)
        res = 0
        while stack:
            res += stack.pop()
        return res


s = Solution()
data = [('()', 1),
        ('(())', 2),
        ('()()', 2),
        ('(()(()))', 6),
        ('(()((())))', 10),
        ('(()()())', 6),
        ]
for S, expected in data:
    real = s.scoreOfParentheses(S)
    print('{}, expected {}, real {}, result {}'.format(S, expected, real, expected == real))
