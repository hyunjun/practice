#   https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses


class Solution:
    #   runtime; 32ms, 77.88%
    #   memory; 14.1MB, 100.00%
    def maxDepth(self, s: str) -> int:
        stack, depth, maxDepth = [], 0, 0
        for c in s:
            if c == '(':
                depth += 1
                maxDepth = max(maxDepth, depth)
                stack.append(c)
            elif c == ')':
                if 0 < len(stack) and stack[-1] == '(':
                    depth -= 1
                    stack.pop()
        if 0 == len(stack):
            return maxDepth
        return 0


solution = Solution()
data = [("(1+(2*3)+((8)/4))+1", 3),
        ("(1)+((2))+(((3)))", 3),
        ("1+(2*3)/(2-1)", 1),
        ("1", 0),
        ]
for s, expect in data:
    real = solution.maxDepth(s)
    print(f'{s} expect {expect} real {real} result {expect == real}')
