#   https://www.hackerrank.com/challenges/ctci-fibonacci-numbers


def fibonacci0(n):
    if 0 == n:
        return 0
    if 1 == n:
        return 1
    nn, n1, n0 = None, 1, 0
    for i in range(2, n + 1):
        nn = n1 + n0
        n1, n0 = nn, n1
    return nn

def fibonacci(n):
    if 0 == n:
        return 0
    if 1 == n:
        return 1
    def fib(m):
        nn, n1, n0 = None, 1, 0
        for i in range(2, m + 1):
            nn = n1 + n0
            yield nn
            n1, n0 = nn, n1
    res, f = None, fib(n)
    while 0 <= n - 2:
        res = next(f)
        n -= 1
    return res


data = [(0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (12, 144),
        (17, 1597),
        ]
for n, expected in data:
    real = fibonacci(n)
    print('{}, expected {}, real {}, result {}'.format(n, expected, real, expected == real))
