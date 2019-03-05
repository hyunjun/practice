#   https://www.hackerrank.com/challenges/mars-exploration


def marsExploration(s):
    if s is None or 0 == len(s):
        return 0
    cnt = 0
    for i in range(2, len(s), 3):
        if s[i - 2] != 'S':
            cnt += 1
        if s[i - 1] != 'O':
            cnt += 1
        if s[i] != 'S':
            cnt += 1
    return cnt


data = [('SOSSPSSQSSOR', 3),
	('SOSSOT', 1),
	('SOSSOSSOS', 0),
	]
for s, expected in data:
    real = marsExploration(s)
    print('{}, expected {}, real {}, result {}'.format(s, expected, real, expected == real))
