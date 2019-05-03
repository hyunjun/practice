#   https://www.hackerrank.com/challenges/kruskalmstrsub

#   https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2


#   Wrong Answer for 2/6
def kruskals0(g_nodes, g_from, g_to, g_weight):
    edges = []
    for i, weight in enumerate(g_weight):
        edges.append((g_from[i], g_to[i], weight))
    sortedEdges = sorted(edges, key=lambda t: t[2])

    idx, total, visited = 0, 0, set()
    while len(visited) != g_nodes and idx < len(edges):
        s, t, w = sortedEdges[idx]
        if s not in visited or t not in visited:
            total += w
            visited.add(s)
            visited.add(t)
        idx += 1

    return total


from collections import defaultdict


#   Wrong Answer for 1/6
def kruskals1(g_nodes, g_from, g_to, g_weight):
    edges = []
    for i, weight in enumerate(g_weight):
        edges.append((g_from[i], g_to[i], weight))
    sortedEdges = sorted(edges, key=lambda t: t[2])

    connected = defaultdict(set)
    def hasCycle(s, t):
        q, visited = [s], set()
        while q:
            n = q.pop(0)
            if n == t:
                return True
            visited.add(n)
            for c in connected[n]:
                if c in visited:
                    continue
                q.append(c)
        return False

    idx, total, visited = 0, 0, set()
    while len(visited) != g_nodes and idx < len(edges):
        s, t, w = sortedEdges[idx]
        if not hasCycle(s, t) and not hasCycle(t, s):
            total += w
            visited.add(s)
            visited.add(t)
            connected[s].add(t)
            connected[t].add(s)
        idx += 1

    return total


#   Timeout for 2/6
#   Not kruskal, prim's algorithm
def kruskals(g_nodes, g_from, g_to, g_weight):
    vSet, edgeDict = set(), defaultdict(dict)
    for i, weight in enumerate(g_weight):
        edgeDict[g_from[i]][g_to[i]] = weight
        edgeDict[g_to[i]][g_from[i]] = weight
        vSet.add(g_from[i])
        vSet.add(g_to[i])

    numV = len(vSet)
    edgeNum, selected = 1, [False] * (numV + 1)
    total, selected[1] = 0, True
    while edgeNum < numV:
        curMin, r, c = float('inf'), 0, 0
        for i in range(1, numV + 1):
            if selected[i]:
                for j in range(1, numV + 1):
                    if not selected[j] and i in edgeDict and j in edgeDict[i] and 0 < edgeDict[i][j]:
                        if edgeDict[i][j] < curMin:
                            curMin, r, c = edgeDict[i][j], i, j
        #print('{} - {}: {}'.format(r, c, edgeDict[r][c]))
        selected[c] = True
        total += edgeDict[r][c]
        edgeNum += 1

    return total


data = [(4, [1, 1, 4, 2, 3, 3], [2, 3, 1, 4, 2, 4], [5, 3, 6, 7, 4, 5], 12),
        (5, [1, 1, 1, 1, 2, 3, 4], [2, 3, 4, 5, 3, 4, 5], [20, 50, 70, 90, 30, 40, 60], 150),
        ]
for g_nodes, g_from, g_to, g_weight, expected in data:
    real = kruskals(g_nodes, g_from, g_to, g_weight)
    print('{}, {}, {}, {}, expected {}, real {}, result {}'.format(g_nodes, g_from, g_to, g_weight, expected, real, expected == real))
