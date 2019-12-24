#   https://leetcode.com/problems/iterator-for-combination/discuss/452186/Python-generator-yield-and-Python-built-in-cheat


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


f = combi('abc', 2)
print(next(f, None))
print(next(f, None))
print(next(f, None))
print(next(f, None))
