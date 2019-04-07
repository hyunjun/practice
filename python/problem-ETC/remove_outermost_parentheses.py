#   https://leetcode.com/problems/remove-outermost-parentheses


class Solution:
    #   runtime; 48ms, 100.00%
    #   memory; 13.3MB, 100.00%
    def removeOuterParentheses(self, S):
        if S is None or 0 == len(S):
            return ''
        pNum, pNums = -1, []
        for c in S:
            if '(' == c:
                pNum += 1
                pNums.append(pNum)
            else:
                pNums.append(pNum)
                pNum -= 1
        res = []
        for i, c in enumerate(S):
            if 0 < pNums[i]:
                res.append(c)
        return ''.join(res)


s = Solution()
data = [('(()())(())', '()()()'),
        ('(()())(())(()(()))', '()()()()(())'),
        ('()()', ''),
        ]
for S, expected in data:
    real = s.removeOuterParentheses(S)
    print('{}, expected {}, real {}, result {}'.format(S, expected, real, expected == real))
