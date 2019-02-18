#   https://leetcode.com/problems/custom-sort-string


class Solution:
    #   runtime; 52ms, 20.33%
    #   memory; 12.5MB, 100.00%
    def customSortString(self, S, T):
        if S is None or 0 == len(S) or T is None or 0 == len(T):
            return ''
        orderDict, included, excluded = {c: i for i, c in enumerate(S)}, [], []
        for c in T:
            if c in orderDict:
                included.append(c)
            else:
                excluded.append(c)
        res = sorted(included, key=lambda c: orderDict[c]) + excluded
        return ''.join(res)


s = Solution()
data = [('cba', 'abcd', 'cbad'),
        ]
for S, T, expected in data:
    real = s.customSortString(S, T)
    print('{}, {}, expected {}, real {}, result {}'.format(S, T, expected, real, expected == real))
