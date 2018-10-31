#   https://leetcode.com/problems/valid-parentheses
#   https://www.hackerrank.com/challenges/ctci-balanced-brackets/problem


class Solution(object):
  def isValid(self, s):
    if s is None or 0 == len(s):
      return False

    stack = []
    # if an open parenthesis such as (, {, [, put it into the stack
    # if a close parenthesis such as ), }, ], pop from the stack, then check matching
    for c in s:
      if c in ['(', '{', '[']:
        stack.append(c)
        #print('stack {}'.format(stack))
      elif c in [')', '}', ']']:
        if 0 < len(stack):
          p = stack.pop()
        else:
          p = ''
        #print('p + c {}'.format(p + c))
        if p + c not in ['()', '{}', '[]']:
          return False
    if 0 < len(stack):
      return False
    return True


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
         ]
s = Solution()
for case, expected in cases:
  real = s.isValid(case)
  print('{}\texpected {}\treal {}\tresult {}'.format(case, expected, real, expected == real))
