#   https://leetcode.com/problems/all-paths-from-source-to-target

#   https://leetcode.com/problems/all-paths-from-source-to-target/solution


class Solution:
    #   runtime; 196ms, 32.10%
    #   memory; 13.3MB, 5.17%
    def allPathsSourceToTarget(self, graph):
        res, q = [], [([], 0)]
        while q:
            path, node = q.pop(0)
            path.append(node)
            if 0 == len(graph[node]):
                res.append(path)
            for neighbor in graph[node]:
                q.append((path[:], neighbor))
        return res

    #   https://leetcode.com/explore/featured/card/july-leetcoding-challenge/547/week-4-july-22nd-july-28th/3400
    #   runtime; 104ms, 87.01%
    #   memory; 15.4MB, 34.87%
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []

        def paths(acc, n):
            if 0 < len(acc) and acc[0] == 0 and n == len(graph) - 1:
                acc.append(n)
                res.append(acc[:])
                acc.pop()
            else:
                for m in graph[n]:
                    acc.append(n)
                    paths(acc[:], m)
                    acc.pop()
        paths([], 0)
        return res


s = Solution()
data = [([[1, 2], [3], [3], []], [[0, 1, 3], [0, 2, 3]]),
        ([[4,3,1],[3,2,4],[3],[4],[]], [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]),
        ]
for graph, expected in data:
    real = s.allPathsSourceToTarget(graph)
    print('{}, expected {}, real {}, result {}'.format(graph, expected, real, expected == real))
