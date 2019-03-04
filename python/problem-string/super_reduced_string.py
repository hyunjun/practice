#   https://www.hackerrank.com/challenges/reduced-string


#   Wrong Answer
def superReducedString0(s):
    if s is None or 0 == len(s):
        return 'Empty String'
    if len(s) < 2 or len(set(s)) == len(s):
        return s
    l = list(s)
    for i, c in enumerate(l):
        if 0 == i:
            continue
        if l[i - 1] == l[i]:
            l[i - 1] = l[i] = ''
    return superReducedString(''.join(l))

#   Timeout
def superReducedString1(s):
    if s is None or 0 == len(s):
        return 'Empty String'
    while len(set(s)) != len(s):
        l = list(s)
        for i, c in enumerate(l):
            if 0 == i:
                continue
            if l[i - 1] == l[i]:
                l[i - 1] = l[i] = ''
        s = ''.join(l)
    if s is None or 0 == len(s):
        return 'Empty String'
    return s

#   Wrong Answer
def superReducedString2(s):
    if s is None or 0 == len(s):
        return 'Empty String'
    if len(s) < 2:
        return s
    i, strList = 1, list(s)
    while i < len(s):
        l, r = i - 1, i
        while 0 <= l and r < len(s) and strList[l] == strList[r]:
            strList[l] = strList[r] = ''
            l -= 1
            r += 1
        i = r + 1
    s = ''.join(strList)
    if s is None or 0 == len(s):
        return 'Empty String'
    return s

def superReducedString(s):
    i, stack = 0, []
    for i, c in enumerate(s):
        if 0 == len(stack) or stack[-1] != c:
            stack.append(c)
        else:
            stack.pop()
    s = ''.join(stack)
    if s is None or 0 == len(s):
        return 'Empty String'
    return s


data = [('aaabccddd','abd'),
        ('aa', 'Empty String'),
        ('baab', 'Empty String'),
        ('aaabcccdddb', 'abcdb'),
        ]
for s, expected in data:
    real = superReducedString(s)
    print('{}, expected {}, real {}, result {}'.format(s, expected, real, expected == real))
