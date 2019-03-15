#   https://www.hackerrank.com/challenges/marcs-cakewalk


import math

def marcsCakewalk(calorie):
    return int(sum([math.pow(2, i) * c for i, c in enumerate(sorted(calorie, reverse=True))]))


data = [([1, 3, 2], 11),
        ([7, 4, 9, 6], 79),
        ]
for calorie, expected in data:
    real = marcsCakewalk(calorie)
    print('{}, expected {}, real {}, result {}'.format(calorie, expected, real, expected == real))
