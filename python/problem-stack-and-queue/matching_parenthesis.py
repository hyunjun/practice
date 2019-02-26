#   https://www.interviewcake.com/question/python/matching-parens


def solution0(s, pos):
    stack, d = [], {}
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            openPos = stack.pop()
            d[openPos] = i
    return d[pos]


def solution1(s, pos):
    parCnt = 0
    for i in range(pos, len(s)):
        if s[i] == '(':
            parCnt += 1
        elif s[i] == ')':
            parCnt -= 1
        if 0 == parCnt:
            return i
    return -1


data = [("Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing.", 10, 79),
        ]
for s, pos, expected in data:
    real0 = solution0(s, pos)
    print('{}, {}, expected {}, real {}, result {}'.format(s, pos, expected, real0, expected == real0))
    real1 = solution1(s, pos)
    print('{}, {}, expected {}, real {}, result {}'.format(s, pos, expected, real1, expected == real1))
