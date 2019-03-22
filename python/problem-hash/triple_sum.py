#   https://www.hackerrank.com/challenges/triple-sum


from collections import defaultdict

#   Timeout for 5/10 test cases
def triplets0(a, b, c):
    dicA, dicC, setB = defaultdict(int), defaultdict(int), set(b)
    for i in setB:
        for j in a:
            if j <= i:
                dicA[i] += 1
        for j in c:
            if j <= i:
                dicC[i] += 1
    print(dicA, dicC)
    cnt = 0
    for i in setB:
        cnt += dicA[i] * dicC[i]
    return cnt


def bSearch(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m][1] <= target and (m + 1 < len(arr) and target < arr[m + 1][1] or m == len(arr) - 1):
            return arr[m][0] + 1
        if target < arr[m][1]:
            r = m - 1
        else:
            l = m + 1
    return 0


def triplets(a, b, c):
    sortedA, sortedC = [(i, A) for i, A in enumerate(sorted(set(a)))], [(i, C) for i, C in enumerate(sorted(set(c)))]
    dicA, dicC, setB = {}, {}, set(b)
    for i in setB:
        dicA[i] = bSearch(sortedA, i)
        dicC[i] = bSearch(sortedC, i)
    cnt = 0
    for i in setB:
        cnt += dicA[i] * dicC[i]
    return cnt


data = [([1, 4, 5], [2, 3, 3], [1, 2, 3], 5),
        ([1, 3, 5, 7], [5, 7, 9], [7, 9, 11, 13], 12),
        ]
for a, b, c, expected in data:
    real = triplets(a, b, c)
    print('{}, {}, {}, expected {}, real {}, result {}'.format(a, b, c, expected, real, expected == real))
