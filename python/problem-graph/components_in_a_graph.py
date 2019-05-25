#   https://www.hackerrank.com/challenges/components-in-graph


from collections import defaultdict


#   Timeout for 1/39
def componentsInGraph(gb):
    edgeDict, nodeSet = defaultdict(list), set()
    for s, e in gb:
        edgeDict[s].append(e)
        edgeDict[e].append(s)
        nodeSet.add(s)
        nodeSet.add(e)

    visited, minCnt, maxCnt = set(), float('inf'), -float('inf')

    def bfs(node):
        curVisited, q = set(), [node]
        while q:
            n = q.pop(0)
            curVisited.add(n)
            for neighbor in edgeDict[n]:
                if neighbor in curVisited:
                    continue
                q.append(neighbor)
        return curVisited

    for n in nodeSet:
        if n in visited:
            continue
        curVisited = bfs(n)
        cnt = len(curVisited)
        minCnt = min(minCnt, cnt)
        maxCnt = max(maxCnt, cnt)
        visited = visited.union(curVisited)
    return [minCnt, maxCnt]


data = [([[1, 6], [2, 7], [3, 8], [4, 9], [2, 6]], [2, 4])]
for gb, expected in data:
    real = componentsInGraph(gb)
    print('{}, expected {}, real {}, result {}'.format(gb, expected, real, expected == real))
