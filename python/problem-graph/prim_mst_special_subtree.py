#   https://www.hackerrank.com/challenges/primsmstsub


from collections import defaultdict


#   Timeout for 3/7
def prims(n, edges, start):
    '''
    while # of edges < # of vertices - 1
        for r in range(V):
            for c in range(V)
                get min edge
    '''
    edgeDict = defaultdict(dict)
    for src, dst, weight in edges:
        edgeDict[src][dst] = weight
        edgeDict[dst][src] = weight

    selected, numEdges = [False] * (n + 1), 0
    total, selected[1] = 0, True
    while numEdges < n - 1:
        curMin, r, c = float('inf'), 0, 0
        for i in range(1, n + 1):
            if selected[i]:
                for j in range(1, n + 1):
                    if not selected[j] and i in edgeDict and j in edgeDict[i] and 0 < edgeDict[i][j]:
                        if edgeDict[i][j] < curMin:
                            curMin, r, c = edgeDict[i][j], i, j
        selected[c] = True
        total += edgeDict[r][c]
        numEdges += 1
    return total


data = [(5, [[1, 2, 3], [1, 3, 4], [4, 2, 6], [5, 2, 2], [2, 3, 5], [3, 5, 7]], 1, 15),
        ]
for n, edges, start, expected in data:
    real = prims(n, edges, start)
    print('{}, {}, {}, expected {}, real {}, result {}'.format(n, edges, start, expected, real, expected == real))
