#   https://www.hackerrank.com/challenges/dijkstrashortreach

#   https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7


from collections import defaultdict


#   Timeout 2/9, Wrong Answer 1/9
def shortestReach0(n, edges, s):
    edgeDict = defaultdict(list)
    for src, dst, weight in edges:
        edgeDict[src].append((dst, weight))
        edgeDict[dst].append((src, weight))
    distDict = {i: -1 for i in range(1, n + 1)}
    distDict[s] = 0
    visited = set()

    def getNext():
        retNode, minDist = 0, float('inf')
        for node, dist in distDict.items():
            if node not in visited and -1 < dist < minDist:
                retNode, minDist = node, dist
        return retNode

    while len(visited) < n:
        node = getNext()
        visited.add(node)
        for c, w in edgeDict[node]:
            if -1 == distDict[c]:
                distDict[c] = distDict[node] + w
            else:
                distDict[c] = min(distDict[c], distDict[node] + w)
    return [distDict[i] for i in range(1, n + 1) if i != s]


#   Wrong Answer 1/9
def shortestReach(n, edges, s):
    edgeDict = defaultdict(list)
    for src, dst, weight in edges:
        edgeDict[src].append((dst, weight))
        edgeDict[dst].append((src, weight))
    distDict = {i: float('inf') for i in range(1, n + 1)}
    distDict[s] = 0
    visited = set()

    def getNext():
        retNode, minDist = 0, float('inf')
        for node, dist in distDict.items():
            if node not in visited and dist < minDist:
                retNode, minDist = node, dist
        return retNode

    for _ in range(n):
        node = getNext()
        visited.add(node)
        for c, w in edgeDict[node]:
            if c in visited:
                continue
            distDict[c] = min(distDict[c], distDict[node] + w)
    return [distDict[i] if distDict[i] != float('inf') else -1 for i in range(1, n + 1) if i != s]



data = [(4, [[1, 2, 24], [1, 4, 20], [3, 1, 3], [4, 3, 12]], 1, [24, 3, 15]),
        (5, [[1, 2, 5], [2, 3, 6], [3, 4, 2], [1, 3, 15]], 1, [5, 11, 13, -1]),
        ]
for n, edges, s, expected in data:
    real = shortestReach(n, edges, s)
    print('{}, {}, {}, expected {}, real {}, result {}'.format(n, edges, s, expected, real, expected == real))
