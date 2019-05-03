#   https://www.programiz.com/dsa/prim-algorithm


from collections import defaultdict


def prim(edges):
    vSet, edgeDict = set(), defaultdict(dict)
    for src, dst, weight in edges:
        edgeDict[src][dst] = weight
        edgeDict[dst][src] = weight
        vSet.add(src)
        vSet.add(dst)

    numV = len(vSet)
    edgeNum, selected = 0, [False] * numV
    selected[0] = True
    while edgeNum < numV - 1:
        curMin, r, c = float('inf'), 0, 0
        for i in range(numV):
            if selected[i]:
                for j in range(numV):
                    if not selected[j] and i in edgeDict and j in edgeDict[i] and 0 < edgeDict[i][j]:
                        if edgeDict[i][j] < curMin:
                            curMin, r, c = edgeDict[i][j], i, j
        print('{} - {}: {}'.format(r, c, edgeDict[r][c]))
        selected[c] = True
        edgeNum += 1


edges = [[0, 1, 9], [0, 2, 75], [1, 2, 95], [1, 3, 19], [1, 4, 42], [2, 3, 51], [2, 4, 66], [3, 4, 31]]
prim(edges)
