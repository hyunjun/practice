#   https://leetcode.com/problems/long-pressed-name

#   https://leetcode.com/problems/long-pressed-name/solution


class Solution:
    #   Wrong Answer
    def isLongPressedName0(self, name, typed):
        if (name is None or 0 == len(name)) and (typed is None or 0 == len(typed)):
            return True
        if (name is None or 0 == len(name)) or (typed is None or 0 == len(typed)):
            return False
        nIdxDict, nCntDict, tIdxDict, tCntDict = {}, {}, {}, {}
        for i, c in enumerate(name):
            if i in nIdxDict:
                nIdxDict[c].append(i)
            else:
                nIdxDict[c] = [i]
            if c in nCntDict:
                nCntDict[c] += 1
            else:
                nCntDict[c] = 1
        for i, c in enumerate(typed):
            if i in tIdxDict:
                tIdxDict[c].append(i)
            else:
                tIdxDict[c] = [i]
            if c in tCntDict:
                tCntDict[c] += 1
            else:
                tCntDict[c] = 1
        for c in name:
            if c not in tCntDict or nCntDict[c] > tCntDict[c]:
                return False
            for i, idx in enumerate(nIdxDict[c]):
                if idx > tIdxDict[c][i]:
                    return False
        return True

    #   40ms, 100.00%
    def isLongPressedName(self, name, typed):
        if (name is None or 0 == len(name)) and (typed is None or 0 == len(typed)):
            return True
        if (name is None or 0 == len(name)) or (typed is None or 0 == len(typed)):
            return False
        nIdx, tIdx = 0, 0
        while nIdx < len(name):
            nCnt, tCnt = 1, 0
            while nIdx + 1 < len(name) and name[nIdx] == name[nIdx + 1]:
                nCnt += 1
                nIdx += 1
            while tIdx < len(typed) and name[nIdx] == typed[tIdx]:
                tCnt += 1
                tIdx += 1
            if nCnt > tCnt:
                return False
            nIdx += 1
        return True


s = Solution()
data = [("alex", "aaleex", True),
        ("saeed", "ssaaedd", False),
        ("leelee", "lleeelee", True),
        ("laiden", "laiden", True),
        ("kikcxmvzi", "kiikcxxmmvvzz", False),
        ("znxnorutzt", "zznxxnnooruuzztt", False),
        ]
for name, typed, expected in data:
    real = s.isLongPressedName(name, typed)
    print('{}, {}, expected {}, real {}, result {}'.format(name, typed, expected, real, expected == real))
