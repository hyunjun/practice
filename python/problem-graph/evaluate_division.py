#   https://leetcode.com/problems/evaluate-division


from collections import defaultdict
from typing import List


class Solution:
    #   runtime; 52ms, 9.89%
    #   memory; 13.3MB, 5.35MB
    def calcEquation0(self, equations, values, queries):
        if equations is None or 0 == len(equations) or values is None or 0 == len(values) or queries is None or 0 == len(queries):
            return []

        nodes, edgeDict = set(), defaultdict(dict)
        for i, (s, e) in enumerate(equations):
            nodes.add(s)
            nodes.add(e)
            edgeDict[s][e] = values[i]
            edgeDict[e][s] = 1 / values[i]

        def calc(s, e):
            if s in edgeDict and e in edgeDict[s]:
                return edgeDict[s][e]
            q, visited = [(1.0, s)], set()
            while q:
                v, n = q.pop(0)
                visited.add(n)
                if n == e:
                    edgeDict[s][e] = v
                    edgeDict[e][s] = 1 / v
                    return v
                for c, vv in edgeDict[n].items():
                    if c in visited:
                        continue
                    q.append((vv * v, c))
            return -1

        ret = []
        for s, e in queries:
            if s not in nodes or e not in nodes:
                ret.append(-1.0)
            elif s == e:
                ret.append(1.0)
            else:
                ret.append(calc(s, e))
        return ret

    #   https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/557/week-4-september-22nd-september-28th/3474
    #   runtime; 28ms, 79.89%
    #   memory; 14.2MB
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        t = lambda: defaultdict(t)
        d, nodes = t(), set()
        for i, (src, dst) in enumerate(equations):
            d[src][dst] = values[i]
            d[dst][src] = 1 / values[i]
            nodes.add(src)
            nodes.add(dst)
            
        def getValue(src, dst):
            q, visited = [(src, 1.0)], set()
            while q:
                n, v = q.pop(0)
                if n == dst:
                    return v
                visited.add(n)
                for nn, vv in d[n].items():
                    if nn in visited:
                        continue
                    q.append((nn, vv * v))
            return -1.0
            
        res = []
        for src, dst in queries:
            if src not in nodes or dst not in nodes:
                res.append(-1.0)
            elif src == dst:
                res.append(1.0)
            else:
                res.append(getValue(src, dst))
        return res


s = Solution()
data = [([["a", "b"], ["b", "c"]], [2.0, 3.0], [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]], [6.0, 0.5, -1.0, 1.0, -1.0]),
        ([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]], [3.75000,0.40000,5.00000,0.20000]),
        ([["a","b"]], [0.5], [["a","b"],["b","a"],["a","c"],["x","y"]], [0.50000,2.00000,-1.00000,-1.00000]),
        ([["a","aa"]], [9.0], [["aa","a"],["aa","aa"]], [1/9.0, 1.0]),
        ]
for equations, values, queries, expect in data:
    real = s.calcEquation(equations, values, queries)
    print(f'{equations}, {values}, {queries}, expect {expect}, real {real}, result {expect == real}')
