#   https://www.hackerrank.com/challenges/pairs


#   Wrong Answer for 1/18 test cases
def pairs0(k, arr):
    res, s = set(), set()
    for a in arr:
        s.add(a)
    for a in arr:
        for t in [k - a, a - k]:
            if t in s:
                res.add((a, t))
                res.add((t, a))
    return int(len(res) // 2)


from collections import defaultdict

#   Wrong Answer for 1/18 test cases
def pairs1(k, arr):
    d = defaultdict(list)
    for i, a in enumerate(arr):
        d[a].append(i)
    res = set()
    for i, a in enumerate(arr):
        for t in [k - a, a - k]:
            if t in d:
                for j in d[t]:
                    if i == j:
                        continue
                    res.add((min(i, j), max(i, j)))
    return len(res)

def pairs(k, arr):
    cnt, sortedArr = 0, sorted(arr)
    s = set(sortedArr)
    for a in sortedArr:
        if a + k in s:
            cnt += 1
    return cnt


#   len(set(a) & set(x + k for x in a))
