#   https://leetcode.com/problems/longest-arithmetic-sequence

#   https://leetcode.com/problems/longest-arithmetic-sequence/discuss/422759/python-dp


from collections import defaultdict
from typing import List


class Solution:
    #   Wrong Answer
    def longestArithSeqLength0(self, A: List[int]) -> int:
        if not (2 <= len(A) <= 2000):
            return 0

        def getSeqLen(acc, diff, nums):
            print(acc, diff, nums)
            if len(nums) < 2:
                return len(acc) + len(nums)
            subRes = 0
            for i, n in enumerate(nums):
                if 0 == i:
                    continue
                if n - nums[0] == diff:
                    acc.append(nums[0])
                    curRes = getSeqLen(acc, diff, nums[i:])
                    subRes = max(subRes, curRes)
                    acc.pop()
            return subRes

        res = 0
        for i, a in enumerate(A):
            if 0 == i:
                continue
            for j in range(i, len(A)):
                subRes = getSeqLen([A[i - 1]], A[j] - A[i - 1], A[j:])
                res = max(res, subRes)
        return res

    #   Wrong Answer
    def longestArithSeqLength1(self, A: List[int]) -> int:
        if not (2 <= len(A) <= 2000):
            return 0

        d = {}
        for i, a in enumerate(A):
            for j in range(i + 1, len(A)):
                diff = a - A[j]
                if diff in d:
                    d[diff].append([a, A[j]])
                else:
                    d[diff] = [[a, A[j]]]
        res = 0
        for diff, diffLists in d.items():
            cnt = 1
            for i, (s, d) in enumerate(diffLists):
                if 0 == i:
                    continue
                if s == diffLists[i - 1][1]:
                    cnt += 1
                else:
                    cnt = 1
                res = max(res, cnt)
        return res + 1

    #   Wrong Answer
    def longestArithSeqLength2(self, A: List[int]) -> int:
        if not (2 <= len(A) <= 2000):
            return 0

        d = {}
        for i, a in enumerate(A):
            for j in range(i + 1, len(A)):
                diff = a - A[j]
                if diff not in d:
                    d[diff] = {}
                d[diff][a] = A[j]
        res = 0
        for diff, diffDict in sorted(d.items(), key=lambda t: -len(t[1])):
            if diff == 0:
                continue
            subRes, visited = 0, set()
            if len(diffDict) < res:
                break
            for s, d in diffDict.items():
                if s in visited:
                    continue
                cur, p = 1, s
                while p in diffDict:
                    visited.add(p)
                    p = diffDict[p]
                    cur += 1
                subRes = max(subRes, cur)
            res = max(res, subRes)
        return res

    def longestArithSeqLength3(self, A: List[int]) -> int:
        if not (2 <= len(A) <= 2000):
            return 0

        d = defaultdict(dict)
        for i, n in enumerate(A):
            for j in range(i + 1, len(A)):
                diff = A[j] - n
                d[diff][(n, i)] = (A[j], j)
        res = 0
        for diff, nDict in sorted(d.items(), key=lambda t:t[0]):
            if len(nDict) < 6:
                continue
            print(f'{diff} {sorted(nDict.items(), key=lambda t: t[1])}')
        #for s, e in sorted(d[2].items(), key=lambda t:t[1]):
        #    print(f'{s} -> {e}')
        for diff, nDict in d.items():
            for s, e in nDict.items():
                c, cnt, visited = s, 1, set()
                l = []
                while c in nDict and c not in visited:
                    visited.add(c)
                    l.append(c)
                    c = nDict[c]
                    cnt += 1
                #if 1 < len(visited):
                #    print(l, nDict[l[-1]])
                res = max(res, cnt)
        return res

    #   runtime; 1364ms, 60.60%
    #   memory; 12.7MB, 100.00%
    def longestArithSeqLength(self, A: List[int]) -> int:
        if not (2 <= len(A) <= 2000):
            return 0

        #print(sorted(Counter(A).items(), key=lambda t: (t[1], t[0]), reverse=True))
        res, d = 0, defaultdict(list)
        for i, n in enumerate(A):
            d[n].append(i)
        #print(sorted(d.items(), key=lambda t: t[0]))
        for i, n in enumerate(A):
            for j in range(i + 1, len(A)):
                cnt, diff = 1, A[j] - n
                nextNum, curIdx = n + diff, i
                #l = []
                #l.append(f'{diff}: {n} {curIdx} -> {nextNum}')
                while nextNum in d:
                    hasNextIdx = False
                    for idx in d[nextNum]:
                        if curIdx < idx:
                            curIdx, hasNextIdx = idx, True
                            break
                    if not hasNextIdx:
                        break
                    nextNum += diff
                    #l.append(f'{nextNum - diff} {curIdx} -> {nextNum}')
                    cnt += 1
                #if diff == 2:
                #    print(l)
                res = max(res, cnt)
        return res


s = Solution()
data = [([3, 6, 9, 12], 4),
        ([9, 4, 7, 2, 10], 3),
        ([20, 1, 15, 3, 10, 5, 8], 4),
        ([44,46,22,68,45,66,43,9,37,30,50,67,32,47,44,11,15,4,11,6,20,64,54,54,61,63,23,43,3,12,51,61,16,57,14,12,55,17,18,25,19,28,45,56,29,39,52,8,1,21,17,21,23,70,51,61,21,52,25,28], 6),
        ([12,28,13,6,34,36,53,24,29,2,23,0,22,25,53,34,23,50,35,43,53,11,48,56,44,53,31,6,31,57,46,6,17,42,48,28,5,24,0,14,43,12,21,6,30,37,16,56,19,45,51,10,22,38,39,23,8,29,60,18], 4),
        ]
for A, expected in data:
    real = s.longestArithSeqLength(A)
    print(f'{A} expected {expected} real {real} result {expected == real}')
