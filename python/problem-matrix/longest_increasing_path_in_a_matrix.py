#   https://leetcode.com/problems/longest-increasing-path-in-a-matrix


from collections import defaultdict


class Solution:
    def longestIncreasingPath0(self, matrix):
        if matrix is None or 0 == len(matrix) or 0 == len(matrix[0]):
            return 0

        R, C = len(matrix), len(matrix[0])
        def isValid(r, c):
            if r < 0 or R <= r or c < 0 or C <= c:
                return False
            return True

        '''
        #   Wrong Answer
        def bfs(_r, _c):
            stack, maxD, visited = [(_r, _c, 1)], 1, set()
            while stack:
                r, c, d = stack.pop()
                if (r, c) in visited:
                    continue
                maxD = max(maxD, d)
                visited.add((r, c))
                for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if isValid(nr, nc) and matrix[r][c] < matrix[nr][nc]:
                        stack.append((nr, nc, d + 1))
            return maxD
        '''
        #   Time Limit Exceeded
        def dfs(visited, r, c, d):
            visited.add((r, c))
            maxPathLen = d
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if isValid(nr, nc) and matrix[r][c] < matrix[nr][nc]:
                    maxPathLen = max(maxPathLen, dfs(visited, nr, nc, d + 1))
            return maxPathLen

        NUM = R * C
        halfNum = NUM // 2 if NUM % 2 == 0 else NUM // 2 + 1
        maxPathLen = 0
        for r in range(R):
            for c in range(C):
                maxPathLen = max(maxPathLen, dfs(set(), r, c, 1))
                if maxPathLen >= halfNum:
                    return maxPathLen
        return maxPathLen

    #   runtime; 2520ms, 5.06%
    #   memory; 25.7MB, 5.35%
    def longestIncreasingPath(self, matrix):
        if matrix is None or 0 == len(matrix) or 0 == len(matrix[0]):
            return 0

        R, C = len(matrix), len(matrix[0])
        def isValid(r, c):
            if r < 0 or R <= r or c < 0 or C <= c:
                return False
            return True

        incEdgeDict, decEdgeDict = defaultdict(set), defaultdict(set)
        for r in range(R):
            for c in range(C):
                for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if not isValid(nr, nc):
                        continue
                    if matrix[r][c] < matrix[nr][nc]:
                        incEdgeDict[(r, c)].add((nr, nc))
                        decEdgeDict[(nr, nc)].add((r, c))
                    elif matrix[r][c] > matrix[nr][nc]:
                        decEdgeDict[(r, c)].add((nr, nc))
                        incEdgeDict[(nr, nc)].add((r, c))
        starts, dist = [], [[0] * C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                if 0 == len(incEdgeDict[(r, c)]):
                    starts.append((r, c))

        def bfs(_r, _c):
            #print(_r, _c)
            q, maxPathLen = [(_r, _c, 1)], 1
            while q:
                r, c, d = q.pop(0)
                #print('\t', r, c, d)
                if dist[r][c] >= d:
                    continue
                maxPathLen = max(maxPathLen, d)
                dist[r][c] = d
                for nr, nc in decEdgeDict[(r, c)]:
                    q.append((nr, nc, d + 1))
            return maxPathLen

        maxPathLen = 0
        for r, c in starts:
            maxPathLen = max(maxPathLen, bfs(r, c))
        return maxPathLen


s = Solution()
data = [([[9,9,4], [6,6,8], [2,1,1]], 4),
        ([[3,4,5], [3,2,6], [2,2,1]], 4),
        ([[7,6,1,1],[2,7,6,0],[1,3,5,1],[6,6,3,2]], 7),
        ([[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]], 140),
        ]
for matrix, expected in data:
    real = s.longestIncreasingPath(matrix)
    for m in matrix:
        print(m)
    print('expected {}, real {}, result {}'.format(expected, real, expected == real))
