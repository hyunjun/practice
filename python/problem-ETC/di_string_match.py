#   https://leetcode.com/problems/di-string-match


class Solution:
    #   128ms, 100.00%
    def diStringMatch(self, S):
        if len(S) < 1:
            return []
        if len(S) == 1:
            if S[0] == 'I':
                return [0, 1]
            return [1, 0]

        iNum, d, res = 0, len(S), []
        if S[0] == 'I':
            res.append(iNum)
            iNum += 1
        else:
            res.append(d)
            d -= 1
        for i in range(len(S) - 1):
            if S[i:i + 2] == 'II':
                res.append(iNum)
                iNum += 1
            elif S[i:i + 2] == 'ID':
                res.append(d)
                d -= 1
            elif S[i:i + 2] == 'DI':
                res.append(iNum)
                iNum += 1
            elif S[i:i + 2] == 'DD':
                res.append(d)
                d -= 1
        if S[len(S) - 1] == 'I':
            res.append(iNum)
        else:
            res.append(d)
        return res


s = Solution()
data = [('IDID', [0, 4, 1, 3, 2]),
        ('III', [0, 1, 2, 3]),
        ('DDI', [3, 2, 0, 1]),
        ]
for S, expected in data:
    real = s.diStringMatch(S)
    print('{}, expected {}, real {}, result {}'.format(S, expected, real, expected == real))
