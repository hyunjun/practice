#   https://www.interviewcake.com/question/python/recursive-string-permutations


def permutation(s):
    res = set()
    if s is None or 0 == len(s):
        return res

    def permutation(prev, w):
        if 0 == len(w):
            res.add(''.join(prev))
        else:
            for i, c in enumerate(w):
                prev.append(c)
                permutation(prev, w[:i] + w[i + 1:])
                prev.pop()
    permutation([], s)

    return res


for w in sorted(permutation('abcd')):
    print(w)
