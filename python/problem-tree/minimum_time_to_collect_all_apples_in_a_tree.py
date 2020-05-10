#   https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree


from collections import defaultdict
from typing import List


class Solution:
    #   runtime; 1032ms, 33.33%
    #   memory; 62.5MB, 100.00%
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        if not (1 <= n <= 10 ** 5) or edges is None or len(edges) != n - 1 or hasApple is None or len(hasApple) != n:
            return 0
        edgeDict, parentDict = defaultdict(list), defaultdict(int)
        for s, d in edges:
            edgeDict[s].append(d)
            parentDict[d] = s
        parentDict[0] = None
        appleSet, q, edgeSet = set([i for i, apple in enumerate(hasApple) if apple]), [(None, 0)], set()
        while q:
            p, n = q.pop(0)
            if n in appleSet:
                pp = n
                while parentDict[pp] is not None:
                    edgeSet.add((parentDict[pp], pp))
                    pp = parentDict[pp]
            for nn in edgeDict[n]:
                q.append((n, nn))
        return len(edgeSet) * 2


s = Solution()
data = [(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,True,False,True,True,False], 8),
        (7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,True,False,False,True,False], 6),
        (7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,False,False,False,False,False], 0),
        (4, [[0,1],[1,2],[0,3]], [True,True,True,True], 6),
        ]
for n, edges, hasApple, expected in data:
    real = s.minTime(n, edges, hasApple)
    print(f'{n} {edges} {hasApple} expected {expected} real {real} result {expected == real}')
