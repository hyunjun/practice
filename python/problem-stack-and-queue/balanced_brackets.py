#   https://www.hackerrank.com/challenges/balanced-brackets


def isBalanced(s):
    def isPair(o, c):
        if o == '{' and c == '}' or o == '[' and c == ']' or o == '(' and c == ')':
            return True
        return False

    i, stack = 0, []
    while i < len(s):
        if i + 1 < len(s) and isPair(s[i], s[i + 1]):
            i += 2
            continue
        if 0 < len(stack) and isPair(stack[-1], s[i]):
            stack.pop()
            i += 1
            continue
        stack.append(s[i])
        i += 1
    if len(stack) == 0:
        return 'YES'
    return 'NO'


data = [('{[()]}', 'YES'),
        ('{[(])}', 'NO'),
        ('{{([])}}', 'YES'),
        ('{{)[](}}', 'NO'),
        ('{{[[(())]]}}', 'YES'),
        ('{(([])[])[]}', 'YES'),
        ('{(([])[])[]]}', 'NO'),
        ('{(([])[])[]}[]', 'YES'),
        ]
for s, expected in data:
    real = isBalanced(s)
    print('{}, expected {}, real {}, result {}'.format(s, expected, real, expected == real))
