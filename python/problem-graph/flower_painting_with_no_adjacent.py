#   https://leetcode.com/problems/flower-planting-with-no-adjacent


from collections import defaultdict


class Solution:
    #   runtime; 196ms, 89.42%
    #   memory; 17.7MB, 100.00%
    def gardenNoAdj(self, N, paths):
        edgeDict = defaultdict(list)
        for s, d in paths:
            edgeDict[s].append(d)
            edgeDict[d].append(s)

        colors = [None] * N
        for n in range(1, N + 1):
            neighborColors = [colors[c - 1] for c in edgeDict[n] if colors[c - 1] is not None]
            for color in range(1, 5):
                if color in neighborColors:
                    continue
                colors[n - 1] = color
                break
        return colors


s = Solution()
data = [(3, [[1,2],[2,3],[3,1]], [1,2,3]),
        (4, [[1,2],[3,4]], [1,2,1,2]),
        (4, [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]], [1,2,3,4]),
        (1, [], [1]),
        ]
for N, paths, expected in data:
    real = s.gardenNoAdj(N, paths)
    print('{}, {}, expected {}, real {}, result {}'.format(N, paths, expected, real, expected == real))
