#   https://leetcode.com/problems/buddy-strings

#   https://leetcode.com/problems/buddy-strings/solution


class Solution:
    #   5.15%
    def buddyStrings(self, A, B):
        if (A is None or 0 == len(A)) and (B is None or 0 == len(B)) or len(A) != len(B):
            return False

        def indices(s):
            d = {}
            for i, c in enumerate(s):
                if c in d:
                    d[c].add(i)
                else:
                    d[c] = set([i])
            return d

        dA, dB = indices(A), indices(B)
        if set(dA.keys()) != set(dB.keys()):
            return False

        cnt = 0
        for c, idxSet in dA.items():
            bIdxSet = dB[c]
            if len(idxSet) != len(bIdxSet):
                return False
            cnt += len(idxSet - bIdxSet)
        if 2 == cnt:
            return True

        for c, idxSet in dA.items():
            bIdxSet = dB[c]
            if idxSet == bIdxSet and 2 <= len(idxSet) and 2 <= len(bIdxSet):
                return True

        return False


s = Solution()
data = [('ab', 'ba', True),
        ('ab', 'ab', False),
        ('ab', 'ac', False),
        ('aa', 'aa', True),
        ('aaaaaaabc', 'aaaaaaacb', True),
        ('', 'aa', False),
        ('aaaaaaabbcc', 'aaaaaaabcbc', True),
        ]
for A, B, expected in data:
    real = s.buddyStrings(A, B)
    print('{}, {}, expected {}, real {}, result {}'.format(A, B, expected, real, expected == real))
