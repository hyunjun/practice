#   https://leetcode.com/problems/generate-parentheses
#   60.53%
#   https://discuss.leetcode.com/topic/17510/4-7-lines-python

class Solution:
    def generateParenthesis(self, n):
        if n <= 0:
            return ['']
        if n == 1:
            return ['()']

        items, res = [('(', 1, 0)], set()
        while 0 < len(items):
            item = items.pop()
            parenthesis, openCnt, closeCnt = item
            if openCnt == n:
                res.add(parenthesis + (')' * (n - closeCnt)))
            else:
                if openCnt == closeCnt:
                    items.append((parenthesis + '(', openCnt + 1, closeCnt))
                elif openCnt > closeCnt:
                    items.append((parenthesis + '(', openCnt + 1, closeCnt))
                    items.append((parenthesis + ')', openCnt, closeCnt + 1))
        return list(res)


cases = [(0, ['']), (1, ['()']), (2, ['()()', '(())']),
         (3, ['((()))', '(()())', '(())()', '()(())', '()()()']),
         (4, ['(((())))','((()()))','((())())','((()))()','(()(()))','(()()())','(()())()','(())(())','(())()()','()((()))','()(()())','()(())()','()()(())','()()()()'])
        ]
s = Solution()
for n, expected in cases:
    real = s.generateParenthesis(n)
    print('{}\texpected {}\treal {}\tresult {}'.format(n, expected, real, sorted(expected) == sorted(real)))
