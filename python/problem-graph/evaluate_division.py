#   https://leetcode.com/problems/evaluate-division


from collections import defaultdict


class Solution:
    def calcEquation(self, equations, values, queries):
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


s = Solution()
data = [([["a", "b"], ["b", "c"]], [2.0, 3.0], [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]], [6.0, 0.5, -1.0, 1.0, -1.0]),
        ]
for equations, values, queries, expected in data:
    real = s.calcEquation(equations, values, queries)
    print('{}, {}, {}, expected {}, real {}, result {}'.format(equations, values, queries, expected, real, expected == real))
