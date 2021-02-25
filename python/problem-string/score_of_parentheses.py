#   https://leetcode.com/problems/score-of-parentheses

#   https://leetcode.com/problems/score-of-parentheses/solution


class Solution:
    #   runtime; 36ms, 81.00%
    #   memory; 12.5MB, 100.00%
    def scoreOfParentheses0(self, S):
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

    #   https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3651
    #   runtime: 20ms, 99.39%
    #   memory: 14.3MB
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        for c in S:
            if c == '(':
                stack.append(c)
            else:
                if 0 < len(stack) and stack[-1] == '(':
                    stack.pop()
                    stack.append(1)
                else:
                    num = 0
                    while 0 < len(stack) and stack[-1] != '(':
                        num += stack.pop()
                    if 0 < len(stack) and stack[-1] == '(':
                        stack.pop()
                        num *= 2
                    stack.append(num)
        return sum(stack)


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
