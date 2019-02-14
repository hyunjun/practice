#   https://leetcode.com/problems/redundant-connection

#   https://leetcode.com/problems/redundant-connection/solution


from collections import defaultdict

class Solution:
    #   runtime; 216ms, 2.69%
    #   memory; 11.5MB, 100.00%
    def findRedundantConnection(self, edges):
        if edges is None or 0 == len(edges):
            return []

        def connectedNodes(node, edgeDict):
            visited, q = set([node]), [node]
            while q:
                n = q.pop(0)
                if n in visited and edgeDict[n].intersection(visited) == edgeDict[n]:
                    break
                visited.add(n)
                visited.union(edgeDict[n])
                for c in edgeDict[n]:
                    if c not in visited:
                        q.append(c)
            return visited

        edgeDict, res = defaultdict(set), []
        for a, b in edges:
            s = connectedNodes(a, edgeDict)
            if b in s:
                res = [a, b]
            edgeDict[a].add(b)
            edgeDict[b].add(a)
        return res


s = Solution()
data = [([[1, 2], [1, 3], [2, 3]], [2, 3]),
        ([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]], [1, 4]),
        ]
for edges, expected in data:
    real = s.findRedundantConnection(edges)
    print('{}, expected {}, real {}, result {}'.format(edges, expected, real, expected == real))
