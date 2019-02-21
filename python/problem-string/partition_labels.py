#   https://leetcode.com/problems/partition-labels

#   https://leetcode.com/problems/partition-labels/solution


class Solution:
    #   runtime; 32ms, 62.68%
    #   memory; 10.7MB, 90.99%
    def partitionLabels(self, S):
        if S is None or 0 == len(S):
            return []

        d = {}
        for i, c in enumerate(S):
            if c in d:
                d[c][1] = i
            else:
                d[c] = [i, i]

        charSet, groupKeyDict, groupValDict = set(), {}, {}
        for i, c in enumerate(S):
            if c in charSet:
                continue
            charSet.add(c)
            minIdx, maxIdx = d[c]
            if minIdx in groupKeyDict:
                groupKey = groupKeyDict[minIdx]
                group = groupValDict[groupKey]
                groupValDict[groupKey] = [min(group[0], minIdx), max(group[1], maxIdx)]
                for j in range(min(group[1], maxIdx), max(group[1], maxIdx) + 1):
                    groupKeyDict[j] = groupKey
            else:
                for j in range(minIdx, maxIdx + 1):
                    groupKeyDict[j] = minIdx
                groupValDict[minIdx] = [minIdx, maxIdx]

        res = []
        for groupKey, (minIdx, maxIdx) in sorted(groupValDict.items(), key=lambda t: t[0]):
            res.append(maxIdx - minIdx + 1)
        return res


s = Solution()
data = [('ababcbacadefegdehijhklij', [9, 7, 8]),
        ]
for S, expected in data:
    real = s.partitionLabels(S)
    print('{}, expected {}, real {}, result {}'.format(S, expected, real, expected == real))
'''
    0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
    a b a b c b a c a d e  f  e  g  d  e  h  i  j  h  k  l  i  j
a   -----------------
b     ---------
c           -------
d                     ---------------
e                       -------
f                          -
g                                -
h                                         ----------
i                                            ----------------
j                                               ----------------
k                                                     -
l                                                         -
2번 이상 나오는 애들끼리는 모두 분리, 겹치는 애들끼리는 합치기
1번 나오는 게 어디에도 포함이 안 되는 경우는 분리, 하지만 2번 이상 나오는 데 겹치면 포함
a = [0, 2, 6, 8] = [0, 8]
b = [1, 3, 5]    = [1, 5] -> [0, 8]
c = [4, 7]       = [4, 7] -> [0, 8]
d = [9, 14]      = [9, 14] -> [9, 15]
e = [10, 12, 15] = [10, 15] -> merge [9, 15]
f = [11]         = [9, 15]
g = [13]         = [9, 15]
h = [16, 19]     = [16, 19] -> merge [16, 22]
i = [17, 22]     = [17, 22] -> merge [16, 22]
j = [18, 23]     = [18, 23] -> merge [16, 23]
k = [20]         = [18, 23]
l = [21]         = [18, 23]
[0, 8] = 8 - 0 + 1 = 9
[9, 15] = 15 - 9 + 1 = 7
[16, 23] = 23 - 16 + 1 = 8
'''
