#   https://www.hackerrank.com/challenges/two-characters


from collections import Counter
from collections import defaultdict

def alternate(s):
    if s is None or 0 == len(s):
        return 0
    consecutiveSet = set()
    for i, c in enumerate(s):
        if 0 == i:
            continue
        if s[i - 1] == c:
            consecutiveSet.add(c)
    #print(consecutiveSet)

    def isAlternating(cand):
        for i, c in enumerate(cand):
            if 0 == i:
                continue
            if cand[i - 1] == c:
                return False
        return True

    cntDict = Counter([c for c in s if c not in consecutiveSet])
    cntCharDict = defaultdict(list)
    for c, cnt in cntDict.items():
        cntCharDict[cnt].append(c)
    sortedCntCharList = sorted(cntCharDict.items(), key=lambda t: t[0], reverse=True)
    #print(sortedCntCharList)
    for i, (cnt1, charList1) in enumerate(sortedCntCharList):
        for j, (cnt2, charList2) in enumerate(sortedCntCharList):
            if j < i or 1 < abs(cnt1 - cnt2):
                continue
            for ch1 in charList1:
                for ch2 in charList2:
                    if ch1 == ch2:
                        continue
                    cand = [c for c in s if c == ch1 or c == ch2]
                    #print(cand)
                    if isAlternating(cand):
                        return len(cand)
    return 0


data = [('abaacdabd', 4),
        ('beabeefeab', 5),
        ('asdcbsdcagfsdbgdfanfghbsfdab', 8),
        ('asvkugfiugsalddlasguifgukvsa', 0),
        ]
for s, expected in data:
    real = alternate(s)
    print('{}, expected {}, real {}, result {}'.format(s, expected, real, expected == real))
