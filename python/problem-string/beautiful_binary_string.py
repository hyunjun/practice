#   https://www.hackerrank.com/challenges/beautiful-binary-string


def beautifulBinaryString(b):
    i, l, cnt = 0, list(b), 0
    print(b)
    for i in range(len(b) - 4):
        if '0' == l[i] and '1' == l[i + 1] and '0' == l[i + 2] and '1' == l[i + 3] and '0' == l[i + 4]:
            l[i + 2] = '1'
            cnt += 1
    for i in range(len(b) - 2):
        if '0' == l[i] and '1' == l[i + 1] and '0' == l[i + 2]:
            l[i + 1] = '0'
            cnt += 1
    print(''.join(l), cnt)
    return cnt

data = [('0101010', 2),
        ('01100', 0),
        ('0100101010', 3),
        ]
for b, expected in data:
    real = beautifulBinaryString(b)
    print('{}, expected {}, real {}, result {}'.format(b, expected, real, expected == real))
