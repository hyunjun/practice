#   https://www.codela.io/challenges/5a5dd8ab9934dfb3614af731/check-if-two-expressions-are-same


def solution(expr1, expr2):

    def getParenIndices(expr):
        stack, indices = [], []
        for i, e in enumerate(expr):
            if '(' == e:
                stack.append((e, i))
            elif ')' == e:
                if stack[-1][0] == '(':
                    _, idx = stack.pop()
                    indices.append((idx, i))
        return indices

    def removeParen(expr, indices):
        for s, e in indices:
            if 0 < s and expr[s - 1] == '-':
                for i in range(s + 1, e):
                    if expr[i] == '+':
                        expr[i] = '-'
                    elif expr[i] == '-':
                        expr[i] = '+'
                if expr[s + 1] != '+' and expr[s + 1] != '-':
                    expr[s + 1] = '-' + expr[s + 1]
                expr[s - 1] = ''
            expr[s] = expr[e] = ''
        return expr

    expr1, expr2 = list(expr1), list(expr2)
    indices1, indices2 = getParenIndices(expr1), getParenIndices(expr2)
    removed1 = expr1
    if 0 < len(indices1):
        removed1 = removeParen(expr1, indices1)
    removed2 = expr2
    if 0 < len(indices2):
        removed2 = removeParen(expr2, indices2)
    if ''.join(removed1) == ''.join(removed2):
        return 'Yes'
    return 'No'


data = [('-(a+b+c)', '-a-b-c', 'Yes'),
        ('a-b-(c-d)', 'a-b-c-d', 'No'),
        ]
for expr1, expr2, expected in data:
    real = solution(expr1, expr2)
    print('{}, {}, expected {}, real {}, result {}'.format(expr1, expr2, expected, real, expected == real))
