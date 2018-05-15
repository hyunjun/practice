#   https://leetcode.com/problems/isomorphic-strings
#   38.03%


class Solution:
    def isIsomorphic(self, s, t):
        if s == t:
            return True
        if s is None or 0 == len(s) or t is None or 0 == len(t):
            return False
        d = {}
        for i, c in enumerate(s):
            if c in d:
                if d[c] != t[i]:
                    return False
            else:
                if t[i] in d.values():
                    return False
                d[c] = t[i]
        return True


solution = Solution()
data = [('egg', 'add', True),
        ('foo', 'bar', False),
        ('paper', 'title', True),
        ('ab', 'aa', False)
        ]
for s, t, expected in data:
    real = solution.isIsomorphic(s, t)
    print('{}, {}, expected {}, real {}, result {}'.format(s, t, expected, real, expected == real))
