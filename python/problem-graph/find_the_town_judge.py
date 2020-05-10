#   https://leetcode.com/problems/find-the-town-judge


from collections import defaultdict

class Solution:
    #   runtime; 92ms, 76.80%
    #   memory; 14.6MB, 100.00%
    def findJudge0(self, N, trust):
        if 0 == N or trust is None or 0 == len(trust):
            return -1
        #   1. graph edge relationships using defaultdict(list)
        #   2. for i in range(1, N + 1):
        #       if i not in edge:
        #           if every node except i has connection to i
        #               return i
        #   return -1
        edgeDict = defaultdict(set)
        for src, dst in trust:
            edgeDict[src].add(dst)
        for i in range(1, N + 1):
            if i in edgeDict:
                continue
            hasAllTrust = True
            for j in range(1, N + 1):
                if i == j:
                    continue
                if i not in edgeDict[j]:
                    hasAllTrust = False
                    break
            if hasAllTrust:
                return i
        return -1

    #   https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3325
    #   runtime; 776ms, 84.16%
    #   memory; 18.3MB
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not (1 <= N <= 1000) or trust is None or not (0 <= len(trust) <= 10000):
            return -1
        d = defaultdict(set)
        for a, b in trust:
            d[a].add(b)
        for i in range(1, N + 1):
            if i in d:
                continue
            isJudge = True
            for j in range(1, N + 1):
                if i == j:
                    continue
                if i not in d[j]:
                    isJudge = False
                    break
            if isJudge:
                return i
        return -1

s = Solution()
data = [(2, [[1, 2]], 2),
        (3, [[1, 3], [2, 3]], 3),
        (3, [[1, 3], [2, 3], [3, 1]], -1),
        (3, [[1, 2], [2, 3]], -1),
        ]
for N, trust, expected in data:
    real = s.findJudge(N, trust)
    print('{}, {}, expected {}, real {}, result {}'.format(N, trust, expected, real, expected == real))
