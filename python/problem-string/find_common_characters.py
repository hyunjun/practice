#   https://leetcode.com/problems/find-common-characters


from collections import Counter

class Solution:
    #   runtime; 84ms, 100.00%
    #   memory; 11.2MB, 100.00%
    def commonChars(self, A):
        s = set(A[0])
        for i, a in enumerate(A):
            if 0 == i:
                continue
            s = s.intersection(set(a))
        cntDict = Counter([c for c in A[0] if c in s])
        for i, a in enumerate(A):
            if 0 == i:
                continue
            cntDict2 = Counter(a)
            for c in a:
                if c in s:
                    cntDict[c] = min(cntDict[c], cntDict2[c])
        res = []
        for c in A[0]:
            if 0 < cntDict[c]:
                res.append(c)
                cntDict[c] -= 1
        return res


s = Solution()
data = [(['bella', 'label', 'roller'], ['e', 'l', 'l']),
        (['cool', 'lock', 'cook'], ['c', 'o']),
        ]
for A, expected in data:
    real = s.commonChars(A)
    print('{}, expected {}, real {}, result {}'.format(A, expected, real, expected == real))
