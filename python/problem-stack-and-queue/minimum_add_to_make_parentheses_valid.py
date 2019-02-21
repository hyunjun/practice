#   https://leetcode.com/problems/minimum-add-to-make-parentheses-valid

#   https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/solution


class Solution:
    #   runtime; 24ms, 80.32%
    #   memory; 10.8MB, 27.42%
    def minAddToMakeValid(self, S):
        if S is None or 0 == len(S):
            return 0
        stack = []
        for p in S:
            if '(' == p:
                stack.append(p)
            else:
                if 0 < len(stack) and '(' == stack[-1]:
                    stack.pop()
                else:
                    stack.append(p)
        return len(stack)


s = Solution()
data = [('())', 1),
        ('(((', 3),
        ('()', 0),
        ('()))((', 4),
        ]
for S, expected in data:
    real = s.minAddToMakeValid(S)
    print('{}, expected {}, real {}, result {}'.format(S, expected, real, expected == real))
