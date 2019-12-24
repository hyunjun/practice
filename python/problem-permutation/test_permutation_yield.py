

class Perm:
    def __init__(self, s):
        self.gen = self.perm(s)
        self.buffer = next(self.gen, None)

    def perm(self, s):
        if 1 == len(s):
            yield s
        else:
            for i, c in enumerate(s):
                for r in self.perm(s[:i] + s[i + 1:]):
                    yield c + r

    def next(self):
        r = ''.join(self.buffer)
        self.buffer = next(self.gen, None)
        return r

    def hasNext(self):
        return self.buffer is not None


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

p = Perm('123')
while p.hasNext():
    print(p.next())
