#   https://leetcode.com/problems/minimum-window-substring

#   https://leetcode.com/problems/minimum-window-substring/solution


from collections import Counter
from collections import defaultdict


class Solution:
    #   Wrong Answer
    def minWindow0(self, s, t):
        if s is None or 0 == len(s) or t is None or 0 == len(t) or len(s) < len(t):
            return ''
        if t in s:
            return t
        d, minLen, minPair = {c: -1 for c in t}, None, [0, len(s) - 1]
        for i, c in enumerate(s):
            if c in d:
                d[c] = i
                if all([v != -1 for v in d.values()]) and len(d.values()) == len(set(d.values())):
                    curLen = max(d.values()) - min(d.values()) + 1
                    if minLen is None or curLen < minLen:
                        minLen, minPair = curLen, [min(d.values()), max(d.values())]
        if minLen is None:
            return ''
        return s[minPair[0]:minPair[1] + 1]

    #   runtime; 308ms, 18.56%
    #   memory; 12.8MB, 35.16%
    def minWindow1(self, s, t):
        if s is None or 0 == len(s) or t is None or 0 == len(t) or len(s) < len(t):
            return ''
        if t in s:
            return t
        d = {}
        for c in t:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        cntDict, start, end, minLen, minPair = {c: 0 for c in d.keys()}, -1, -1, None, [0, len(s) - 1]
        for i, c in enumerate(s):
            if c not in d:
                continue
            if -1 == start:
                start = i
            end = i
            cntDict[c] += 1
            if all([cnt <= cntDict[key] for key, cnt in d.items()]):
                while d[s[start]] < cntDict[s[start]]:
                    ns = start + 1
                    while s[ns] not in d.keys():
                        ns += 1
                    cntDict[s[start]] -= 1
                    start = ns
                if end - start <= minPair[1] - minPair[0]:
                    minLen, minPair = end - start + 1, [start, end]
        if minLen is None:
            return ''
        return s[minPair[0]:minPair[1] + 1]

    def minWindow2(self, s, t):
        if s is None or 0 == len(s) or t is None or 0 == len(t) or len(s) < len(t):
            return ''
        if t in s:
            return t
        minLen, si, ei, sIdxDict, sDict, tDict = float('inf'), None, None, defaultdict(list), Counter(), Counter(t)
        for i, c in enumerate(s):
            if c in tDict.keys():
                if sDict[c] == tDict[c]:
                    sIdxDict[c].pop(0)
                sIdxDict[c].append(i)
                st, et = float('inf'), float('inf')
                for v in sIdxDict.values():
                    st = min(st, min(v))
                    et = max(et, max(v))
                if et - st + 1 < minLen:
                    minLen, si, ei = et - st + 1, st, et
        return s[si:ei + 1]

    #   runtime; 504ms, 13.30%
    #   memory; 14.7MB, 5.55%
    def minWindow(self, s: str, t: str) -> str:
        if s is None or 0 == len(s):
            return ''
        if t is None or 0 == len(t):
            return ''
        d, tDict, indices, minCnt, minIndices = defaultdict(int), Counter(t), [], float('inf'), []
        for i, c in enumerate(s):
            if c in t:
                indices.append(i)
                d[c] += 1
                while d[s[indices[0]]] > tDict[s[indices[0]]]:
                    d[s[indices[0]]] -= 1
                    indices.pop(0)
                if all(d[c] >= cnt for c, cnt in tDict.items()) and indices[-1] - indices[0] + 1 < minCnt:
                    minCnt, minIndices = indices[-1] - indices[0] + 1, [indices[0], indices[-1]]
        if 0 == len(minIndices):
            return ''
        return s[minIndices[0]:minIndices[1] + 1]

'''
a d o b e c o d e b a n c
0     3   5       9 10  12
a     b   c       b a   c

b b a a
0 1 2 3
a b c가 다 채워지면 그 때부터는 하나 채워질 때마다 min, max 체크?
'''


solution = Solution()
data = [("ADOBECODEBANC", "ABC", "BANC"),
        ('a', 'aa', ''),
        ('a', 'b', ''),
        ('aa', 'aa', 'aa'),
        ('bbaa', 'aba', 'baa'),
        ("cabwefgewcwaefgcf", "cae", "cwae"),
        ("babb", "baba", ''),
        ('abc', 'ac', 'abc'),
        ]
for s, t, expected in data:
    real = solution.minWindow(s, t)
    print('{}, {}, expected {}, real {}, result {}'.format(s, t, expected, real, expected == real))
'''
    A D O B E C O D E B A  N C  d               curLen  minLen  minPair
    0     3   5       9 10  12  {A:0 B:0 C:0}           13      [0, 12]
i   0 1 2                       {A:0 B:0 C:0}
          3 4                   {A:0 B:3 C:0}
              5 6 7 8           {A:0 B:3 C:5}   6       6       [0, 5]
                      9         {A:0 B:9 C:5}   10      6
                        10 11   {A:10 B:9 C:5}  6
                            12  {A:10 B:9 C:12} 4       4       [9, 12]
    b b a a
    a b a

    A D O B E C O D E B A  N C  d               s   e   cntDict
    0     3   5       9 10  12  {A:1 B:1 C:1}   -1  -1  {A:0 B:0 C:0}
i   0 1 2                                       0   0   {A:1 B:0 C:0}
          3 4                                   0   3   {A:1 B:1 C:0}
              5 6 7 8                           0   5   {A:1 B:1 C:1}
                      9                         0   9   {A:1 B:2 C:1}
                        10                      0   10  {A:2 B:2 C:1}
                        10 11                   3   10  {A:1 B:2 C:1}
                            12                  3   12  {A:1 B:2 C:2}
                            12                  5   12  {A:1 B:1 C:2}
                            12                  9   12  {A:1 B:1 C:1}
'''
