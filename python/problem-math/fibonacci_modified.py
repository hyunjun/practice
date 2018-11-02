#   https://www.hackerrank.com/challenges/fibonacci-modified/problem


def fibonacciModified(t1, t2, n):
    ti, ti1 = t1, t2
    for i in range(n - 2):
        ti2 = ti + ti1 * ti1
        ti, ti1 = ti1, ti2
    return ti2


data = [(0, 1, 5, 5),
        (0, 1, 10, 84266613096281243382112),
        ]
for t1, t2, n, expected in data:
    real = fibonacciModified(t1, t2, n)
    print('{}, {}, {}, expected {}, real {}, result {}'.format(t1, t2, n, expected, real, expected == real))
