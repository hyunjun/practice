#   https://www.geeksforgeeks.org/check-two-expressions-brackets


def removeParenthesis(exp):
    rangeStack, l, r = [], 0, len(exp) - 1
    while l < r:
        while l < len(exp) and exp[l] != '(':
            l += 1
        while 0 < r and exp[r] != ')':
            r -= 1
        if l < r and exp[l] == '(' and exp[r] == ')':
            if 0 < l and exp[l - 1] == '-':
                rangeStack.append((l, r))
                exp[l - 1] = None
            exp[l], exp[r] = None, None
        l += 1
        r -= 1
    while rangeStack:
        l, r = rangeStack.pop()
        for i in range(l, r):
            if exp[i] is None:
                continue
            if ord('a') <= ord(exp[i]) <= ord('z'):
                if exp[i - 1] is None:
                    exp[i - 1] = '-'
                elif exp[i - 1] == '+':
                    exp[i - 1] = '-'
                elif exp[i - 1] == '-':
                    exp[i - 1] = '+'
    return [e for e in exp if e is not None]

def areSameExpressions(exp1, exp2):
    if exp1 and exp2 is None or exp1 is None and exp2:
        return False
    if exp1 == exp2:
        return True
    exp1 = removeParenthesis(list(exp1))
    exp2 = removeParenthesis(list(exp2))
    return ''.join(exp1) == ''.join(exp2)


data = [("-(a+b+c)", "-a-b-c", True),
        ("-(c+b+a)", "-c-b-a", True),
        ("a-b-(c-d)", "a-b-c-d", False),
        ('-(a+b-(c+d))', '-a-b+c+d', True),
        ]
for exp1, exp2, expected in data:
    real = areSameExpressions(exp1, exp2)
    print('{} == {}, expected {}, real {}, result {}'.format(exp1, exp2, expected, real, expected == real))
'''
-(a+b-(c+d))
-
a+b-(c+d)
-(c+d)
a+b-c-d
-a-b+c+d

-a-b+(c+d)
-a-b+c+d
'''
