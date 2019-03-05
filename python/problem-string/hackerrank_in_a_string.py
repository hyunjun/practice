#   https://www.hackerrank.com/challenges/hackerrank-in-a-string


def hackerrankInString(s):
    if s is None or 0 == len(s):
        return 'NO'
    target, ti, ci = 'hackerrank', 0, 0
    while ci < len(s) and ti < len(target):
        if s[ci] == target[ti]:
            ti += 1
        ci += 1
    if ti == len(target):
        return 'YES'
    return 'NO'


data = [('haacckkerrannk', 'YES'),
        ('haacckkerannk', 'NO'),
        ('hereiamstackerrank', 'YES'),
        ('hackerworld', 'NO'),
        ('hhaacckkekraraannk', 'YES'),
        ('rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt', 'NO'),
        ]
for s, expected in data:
    real = hackerrankInString(s)
    print('{}, expected {}, real {}, result {}'.format(s, expected, real, expected == real))
