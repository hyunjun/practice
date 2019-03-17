#   https://www.hackerrank.com/challenges/find-the-nearest-clone


from collections import defaultdict

def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    edgeDict = defaultdict(list)
    for i, src in enumerate(graph_from):
        edgeDict[src].append(graph_to[i])
        edgeDict[graph_to[i]].append(src)
    sameValNodes = set()
    for i, _id in enumerate(ids):
        if _id == val:
            sameValNodes.add(i + 1)
    if len(sameValNodes) < 2:
        return -1
    minDist, visited, distDict, q = float('inf'), set(), defaultdict(int), [(0, None, 1)]
    while q:
        dist, prevNodeWithSameVal, n = q.pop(0)
        if prevNodeWithSameVal is not None and n in sameValNodes:
            minDist = min(minDist, abs(dist - distDict[prevNodeWithSameVal]))
        visited.add(n)
        distDict[n] = dist
        for neighbor in edgeDict[n]:
            if neighbor in visited:
                continue
            q.append((dist + 1, n if n in sameValNodes else prevNodeWithSameVal, neighbor))
    if minDist == float('inf'):
        dists = [d for n, d in distDict.items() if n in sameValNodes]
        for i, d in enumerate(dists):
            for j in range(i + 1, len(dists)):
                minDist = min(minDist, d + dists[j])
    if minDist == float('inf'):
        return -1
    return minDist


data = [(4, [1, 1, 4], [2, 3, 2], [1, 2, 1, 1], 1, 1),
        (4, [1, 1, 4], [2, 3, 2], [1, 2, 3, 4], 2, -1),
        (5, [1, 1, 2, 3], [2, 3, 4, 5], [1, 2, 3, 3, 2], 2, 3),
        ]
for graph_nodes, graph_from, graph_to, ids, val, expected in data:
    real = findShortest(graph_nodes, graph_from, graph_to, ids, val)
    print('{}, {}, {}, {}, {}, expected {}, real {}, result {}'.format(graph_nodes, graph_from, graph_to, ids, val, expected, real, expected == real))
