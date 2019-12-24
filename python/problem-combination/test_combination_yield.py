#   https://leetcode.com/problems/iterator-for-combination/discuss/452186/Python-generator-yield-and-Python-built-in-cheat


class Combi:
    def __init__(self, s, n):
        self.gen = self.combi(s, n)
        self.buffer = next(self.gen, None)

    def combi(self, s, n):
        if 0 == n:
            yield ''
        elif len(s) == n:
            yield s
        elif n < len(s):
            for r in self.combi(s[1:], n - 1):
                yield s[0] + r
            for r in self.combi(s[1:], n):
                yield r

    def next(self):
        r = ''.join(self.buffer)
        self.buffer = next(self.gen, None)
        return r

    def hasNext(self):
        return self.buffer is not None


def combi(s, n):
    if 0 == n:
        yield ''
    elif n == len(s):
        yield s
    elif n < len(s):
        for r in combi(s[1:], n - 1):
            yield s[0] + r
        for r in combi(s[1:], n):
            yield r


c = combi('abc', 2)
print(next(c, None))
print(next(c, None))
print(next(c, None))
print(next(c, None))

c = Combi('123', 2)
while c.hasNext():
    print(c.next())
