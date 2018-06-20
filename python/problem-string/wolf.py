#   http://community.topcoder.com/stat?c=problem_statement&pm=12778&rd=15705


def initWolfDict():
    return {'w': 0, 'o': 0, 'l': 0, 'f': 0}


def isValid(s):
    if s is None or 0 == len(s):
        return False

    d = initWolfDict()
    for i, c in enumerate(s):
        if 0 < i and s[i - 1] == 'f' and c != 'f':
            if 1 < len(set(d.values())):
                return False
            d = initWolfDict()
        d[c] += 1
    if d != {} and 1 < len(set(d.values())):
        return False
    return True


data = [("wolf", True),
        ("wwolfolf", False),
        ("wolfwwoollffwwwooolllfffwwwwoooollllffff", True),
        ("flowolf", False),
        ]
for s, expected in data:
    real = isValid(s)
    print('{}, expected {}, real {}, result {}'.format(s, expected, real, expected == real))

'''
wolf
i   c   d
0   w   w 0 o 0 l 0 f 0
        w 1
1   o       o 1
2   l           l 1
3   f               f 1
4

wwolfolf
i   c   d
0   w   w 1 o 0 l 0 f 0
1   w   w 2
2   o       o 1
3   l           l 1
4   f               f 1
'''
