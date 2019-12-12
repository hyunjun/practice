

class Solution:
    #   recursive
    def maxEqualSumLen0(self, s: str) -> int:
        if s is None or 0 == len(s):
            return 0

        def getMaxEqualSumLen(l):
            m = len(l) // 2
            if sum(l[:m]) == sum(l[m:]):
                return 2 * m
            return max(getMaxEqualSumLen(l[2:]), getMaxEqualSumLen(l[1:-1]), getMaxEqualSumLen(l[:-2]))

        l = list(int(c) for c in s)
        if len(l) % 2 == 0:
            return getMaxEqualSumLen(l)
        return max(getMaxEqualSumLen(l[:-1]), getMaxEqualSumLen(l[1:]))


solution = Solution()
data = [('142124', 6),  #   1 + 4 + 2 = 1 + 2 + 4
        ('9430723', 4), #   4 + 3 = 0 + 7
        ]
for s, expected in data:
    real = solution.maxEqualSumLen(s)
    print(f'{s}, expected {expected}, real {real}, result {expected == real}')
