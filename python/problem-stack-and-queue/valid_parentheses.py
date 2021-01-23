#   https://leetcode.com/problems/valid-parentheses


#   https://www.hackerrank.com/challenges/ctci-balanced-brackets/problem


class Solution(object):
    #   runtime; 45ms, 8.05%
    def isValid0(self, s):
        if s is None or 0 == len(s):
            return False

        stack = []
        # if an open parenthesis such as (, {, [, put it into the stack
        # if a close parenthesis such as ), }, ], pop from the stack, then check matching
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            elif c in [')', '}', ']']:
                if 0 < len(stack):
                    p = stack.pop()
                else:
                    p = ''
                if p + c not in ['()', '{}', '[]']:
                    return False
        if 0 < len(stack):
            return False
        return True

    #   runtime; 24ms, 91.22%
    #   memory; 13.9MB, 5.22%
    def isValid1(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                isMatched = False
                if 0 < len(stack):
                    for l, r in [('(', ')'), ('{', '}'), ('[', ']')]:
                        if stack[-1] == l and c == r:
                            stack.pop()
                            isMatched = True
                            break
                if not isMatched:
                    stack.append(c)
        return 0 == len(stack)

    #   https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3610
    #   runtime; 28ms, 84.62%
    #   memory; 14.4MB, 37.08%
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            elif 0 < len(stack):
                for _o, _c in [('(', ')'), ('{', '}'), ('[', ']')]:
                    if c == _c:
                        if stack[-1] == _o:
                            stack.pop()
                        else:
                            stack.append(c)
            else:
                return False
        return 0 == len(stack)


cases = [("[", False),
         ("]", False),
         ("()", True),
         ("()[]{}", True),
         ("([{}])", True),
         ("(]", False),
         ("([)]", False),
         ("{[()]}", True),
         ("{[(])}", False),
         ("{{[[(())]]}}", True),
         ("(])", False),
         ]
s = Solution()
for case, expected in cases:
  real = s.isValid(case)
  print('{}\texpected {}\treal {}\tresult {}'.format(case, expected, real, expected == real))
