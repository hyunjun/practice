#   날짜를 의미하는 1~31 숫자가 주어질 때
#   2일 이상 연속되는 날짜는 ~로 묶고
#   그렇지 않은 경우 ,로 연결하기
#   입력은 sorting되어 있지 않음


def convert(inp):
    days = [None] * 31
    for i in inp:
        days[i - 1] = i
    i, res = 0, []
    while i < 31:
        if days[i]:
            j = i + 1
            while j < 31 and days[j]:
                j += 1
            if i == j - 1:
                res.append(str(days[i]))
            else:
                res.append('{}~{}'.format(days[i], days[j - 1]))
            i = j
        else:
            i += 1
    return ','.join(res)


data = [([11, 2, 7, 6, 13, 17, 8, 9, 3, 5, 12], '2~3,5~9,11~13,17'),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31], '1~31'),
        ([1, 13, 31], '1,13,31'),
        ([1], '1'),
        ([31], '31'),
        ]
for inp, expected in data:
    real = convert(inp)
    print('{}, expected {}, real {}, result {}'.format(inp, expected, real, expected == real))
