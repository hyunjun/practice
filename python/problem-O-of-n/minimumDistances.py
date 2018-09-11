#   https://www.hackerrank.com/challenges/minimum-distances/problem


def minimumDistances(a):
    d, res = {}, len(a)
    for i, n in enumerate(a):
        if n in d:
            res = min(res, i - d[n])
        else:
            d[n] = i
    if res == len(a):
        return -1
    return res
