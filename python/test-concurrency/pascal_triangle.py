#   https://www.johndcook.com/blog/2020/02/04/odd-numbers-in-pascals-triangle/


def pascal_triangle(n):
    if 0 == n:
        return [1]
    if 1 == n:
        return [1, 1]
    l = [1, 1]
    for i in range(2, n + 1):
        m = len(l) // 2
        l.insert(m, l[m])
        if len(l) % 2 == 0:
            l[m] += l[m - 1]
            lStart = m - 1
        else:
            lStart = m
        for i in range(lStart, 0, -1):
            l[i] += l[i - 1]
        for i in range(m + 1, len(l) - 1):
            l[i] += l[i + 1]
    return l


for i in range(7):
    print(pascal_triangle(i))
