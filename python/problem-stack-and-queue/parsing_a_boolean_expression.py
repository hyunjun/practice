#   https://leetcode.com/problems/parsing-a-boolean-expression


from functools import reduce


class Solution:
    #   runtime; 68ms, 58.95%
    #   memory; 13.4MB, 100.00%
    def parseBoolExpr(self, expression: str) -> bool:
        if expression is None or 0 == len(expression):
            return False;
        stack = []
        for e in expression:
            if ')' == e:
                bools = []
                while True:
                    t = stack.pop()
                    if '(' == t:
                        break
                    bools.append(t)
                op = stack.pop()
                if '!' == op:
                    stack.append((not bools[0]))
                elif '|' == op:
                    stack.append(reduce(lambda a, b: a or b, bools))
                elif '&' == op:
                    stack.append(reduce(lambda a, b: a and b, bools))
            elif ',' == e:
                continue
            elif 't' == e:
                stack.append(True)
            elif 'f' == e:
                stack.append(False)
            else:
                stack.append(e)
        return stack.pop()


s = Solution()
data = [('!(f)', True),
        ('|(f, t)', True),
        ('&(t, f)', False),
        ('|(&(t,f,t),!(t))', False),
        ]
for expression, expected in data:
    real = s.parseBoolExpr(expression)
    print(f'{expression}, expected {expected}, real {real}, result {expected == real}')
