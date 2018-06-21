def minimum1(l):
    if l is None or len(l) == 0:
        return None
    length = len(l)
    if 1 == length:
        return l[0]
    return min(minimum1(l[:length // 2]), minimum1(l[length // 2:]))


def minimum2(l):
    if l is None or len(l) == 0:
        return None
    li = 0
    ri = len(l) - 1
    mi = (li + ri) // 2
    while li < mi and mi < ri:
        if l[mi] > l[li]:
            li = mi
        if l[mi] < l[ri]:
            ri = mi
        mi = (li + ri) // 2
    return l[ri]


if __name__ == '__main__':
    l = [ 3, 4, 5, 1, 2 ]
    print(minimum1(l))
    print(minimum2(l))
