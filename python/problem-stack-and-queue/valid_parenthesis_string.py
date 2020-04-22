#   https://leetcode.com/problems/valid-parenthesis-string

#   https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3301


from collections import Counter


class Solution:
    #   Time Limit Exceeded
    def checkValidString0(self, s: str) -> bool:
        if s is None or 0 == len(s):
            return True
        if not (1 <= len(s) <= 100):
            return False

        def isClosingFirst(subStr):
            if 0 == len(subStr):
                return False
            if subStr[0] == ')':
                return True
            i = 0
            while i < len(subStr) and subStr[i] == '*':
                i += 1
            if i < len(subStr) and subStr[i] == ')':
                return True
            return False

        while '()' in s:
            s = s.replace('()', '')
        if isClosingFirst(s):
            return False

        if all(c != '*' for c in s):
            stack = []
            for c in s:
                if c == '(':
                    stack.append(c)
                else:
                    if 0 < len(stack) and stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
            return 0 == len(stack)

        idx = s.index('*')
        return self.checkValidString(s[:idx] + s[idx + 1:]) or \
            self.checkValidString([c if i != idx else '(' for i, c in enumerate(s)]) or \
            self.checkValidString([c if i != idx else ')' for i, c in enumerate(s)])

    #   https://leetcode.com/problems/valid-parenthesis-string/discuss/591687/Python-solution-BEAT-99.99-Easy-to-understand
    #   runtime; 28ms, 73.26%
    #   memory; 13.8MB
    def checkValidString(self, s: str) -> bool:
        if s is None or 0 == len(s):
            return True
        if not (1 <= len(s) <= 100):
            return False

        lStack, sStack = [], []
        for i, c in enumerate(s):
            if c == '(':
                lStack.append(i)
            elif c == '*':
                sStack.append(i)
            else:
                if 0 == len(lStack) and 0 == len(sStack):
                    return False
                if 0 < len(lStack):
                    lStack.pop()
                else:
                    sStack.pop()
        while lStack and sStack:
            if lStack[-1] > sStack[-1]:
                return False
            else:
                lStack.pop()
                sStack.pop()
        return len(lStack) == 0



solution = Solution()
data = [('', True),
        ('()', True),
        ('(*)', True),
        ('(*))', True),
        ('*((**))*()', True),
        ('(((()))())))*))())()(**(((())(()(*()((((())))*())(())*(*(()(*)))()*())**((()(()))())(*(*))*))())', False),
        ('(()())*)))())*)*(*()*()))())())((*)((((((())))())*))**)))()*))()))))()()))*)()(*(())((()((()**()()', False),
        ('(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())', False),
        ]
for s, expected in data:
    real = solution.checkValidString(s)
    print(f'{s} expected {expected} real {real} result {expected == real}')
'''
( )
* * * *
'''
