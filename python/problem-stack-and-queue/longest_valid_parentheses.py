#   https://leetcode.com/problems/longest-valid-parentheses

#   https://leetcode.com/problems/longest-valid-parentheses/solution


class Solution:
    #   runtime; 48ms, 73.14%
    #   memory; 14.3MB, 5.55%
    def longestValidParentheses(self, s: str) -> int:
        if s is None or 0 == len(s):
            return 0
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append((c, i))
            else:
                if 0 < len(stack) and stack[-1][0] == '(':
                    stack.pop()
                else:
                    stack.append((c, i))
        prevNone, cnt, l = -1, 0, list(s)
        for _, i in stack:
            curLen = i - prevNone - 1
            cnt = max(cnt, curLen)
            prevNone = i
        curLen = len(s) - prevNone - 1
        cnt = max(cnt, curLen)
        return cnt


solution = Solution()
data = [('(()', 2),
        (')()())', 4),
        ('()()', 4),
        ('(())()', 6),
        ('((())()((()()()()()(((((())))()()()', 14),
        ]
for s, expected in data:
    real = solution.longestValidParentheses(s)
    print(f'{s} expected {expected} real {real} result {expected == real}')
