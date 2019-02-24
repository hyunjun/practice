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


s = Solution()
data = [([[1, 2], [3], [3], []], [[0, 1, 3], [0, 2, 3]]),
        ]
for graph, expected in data:
    real = s.allPathsSourceToTarget(graph)
    print('{}, expected {}, real {}, result {}'.format(graph, expected, real, expected == real))
