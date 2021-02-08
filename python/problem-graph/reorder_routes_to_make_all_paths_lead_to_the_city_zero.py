#   https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero


from collections import defaultdict
from typing import List


class Solution:
    #   Wrong Answer
    def minReorder0(self, n: int, connections: List[List[int]]) -> int:
        if not (2 <= n <= 5 * 10 ** 4) or len(connections) != n - 1:
            return float('-inf')
        edgeDict = defaultdict(list)
        for s, d in connections:
            edgeDict[s].append(d)

        def move(v):
            if v == 0:
                return True
            for nv in edgeDict[v]:
                if move(nv):
                    return True
            return False

        cnt = 0
        for i in range(n):
            for v in edgeDict.copy()[i]:
                if move(v):
                    continue
                edgeDict[i].remove(v)
                edgeDict[v].append(i)
                cnt += 1
        return cnt

    #   runtime; 744ms, 99.85%
    #   memory; 37.7MB, 100.00%
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        if not (2 <= n <= 5 * 10 ** 4) or len(connections) != n - 1:
            return float('-inf')
        cnt, destinationSet = 0, set([0])
        for s, d in connections:
            if s in destinationSet and d not in destinationSet:
                cnt += 1
                destinationSet.add(d)
            elif s not in destinationSet and d in destinationSet:
                destinationSet.add(s)
        return cnt


s = Solution()
data = [(6, [[0,1],[1,3],[2,3],[4,0],[4,5]], 3),
        (5, [[1,0],[1,2],[3,2],[3,4]], 2),
        (3, [[1,0],[2,0]], 0),
        (10, [[0,1],[2,1],[3,2],[0,4],[5,1],[2,6],[5,7],[3,8],[8,9]], 6),
        ]
for n, connections, expect in data:
    real = s.minReorder(n, connections)
    print(f'{n} {connections} expect {expect} real {real} result {expect == real}')
