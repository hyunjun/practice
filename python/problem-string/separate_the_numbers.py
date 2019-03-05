#   https://www.hackerrank.com/challenges/separate-the-numbers


def separateNumbers(s):
    if s is None or 0 == len(s):
        return 'NO'
    i = 0
    while i < len(s):
        cand = [int(s[:i + 1])]
        while len(''.join([str(num) for num in cand])) < len(s):
            cand.append(cand[-1] + 1)
        if 1 < len(cand) and s == ''.join([str(num) for num in cand]):
            return 'YES {}'.format(cand[0])
        i += 1
    return 'NO'


data = [('1234', 'YES 1'),
        ('91011', 'YES 9'),
        ('99100', 'YES 99'),
        ('101103', 'NO'),
        ('010203', 'NO'),
        ('13', 'NO'),
        ('1', 'NO'),
        ('99910001001', 'YES 999'),
        ('7891011', 'YES 7'),
        ('9899100', 'YES 98'),
        ('999100010001', 'NO'),
        ]
for s, expected in data:
    real = separateNumbers(s)
    print('{}, expected {}, real {}, result {}'.format(s, expected, real, expected == real))
