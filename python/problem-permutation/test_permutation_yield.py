

def perm(s):
    if 1 == len(s):
        yield s
    else:
        for i, c in enumerate(s):
            for r in perm(s[:i] + s[i + 1:]):
                yield c + r


p = perm('abc')
print(next(p, None))
print(next(p, None))
print(next(p, None))
print(next(p, None))
print(next(p, None))
print(next(p, None))
print(next(p, None))
