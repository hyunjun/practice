#   https://leetcode.com/problems/number-of-enclaves


class Solution:
    #   runtime; 172ms, 36.58%
    #   memory; 15.5MB, 100.00%
    def numEnclaves0(self, A):
        if A is None or 0 == len(A) or 0 == len(A[0]):
            return 0
        R, C = len(A), len(A[0])
        if 1 == R or 1 == C:
            return 0
        for r in range(1, R - 1):
            for c in range(1, C - 1):
                if 1 == A[r][c]:
                    A[r][c] = 2

        def change2to1(row, col):
            if 0 == row or R - 1 == row or 0 == col or C - 1 == col or 2 != A[row][col]:
                return
            A[row][col] = 1
            for _r, _c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                change2to1(_r, _c)

        for c in range(1, C - 1):
            if A[0][c] == 1 and A[1][c] == 2:
                change2to1(1, c)
            if A[R - 1][c] == 1 and A[R - 2][c] == 2:
                change2to1(R - 2, c)
        for r in range(1, R - 1):
            if A[r][0] == 1 and A[r][1] == 2:
                change2to1(r, 1)
            if A[r][C - 1] == 1 and A[r][C - 2] == 2:
                change2to1(r, C - 2)

        ret = 0
        for r in range(1, R - 1):
            for c in range(1, C - 1):
                if 2 == A[r][c]:
                    ret += 1
        return ret

    #   runtime; 640ms, 5.02%
    #   memory; 14MB, 100.00%
    def numEnclaves1(self, A):
        if A is None or 0 == len(A) or 0 == len(A[0]):
            return 0
        R, C = len(A), len(A[0])
        if 1 == R or 1 == C:
            return 0

        def bfs(row, col):
            cnt, q = 0, [(row, col)]
            while q:
                r, c = q.pop(0)
                if r <= 0 or R - 1 <= r or c <= 0 or C - 1 <= c or 0 == A[r][c]:
                    continue
                cnt += 1
                A[r][c] = 0
                for _r, _c in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    q.append((_r, _c))
            return cnt
        
        for c in range(1, C - 1):
            if A[0][c] == 1 and A[1][c] == 1:
                bfs(1, c)
            if A[R - 1][c] == 1 and A[R - 2][c] == 1:
                bfs(R - 2, c)
        for r in range(1, R - 1):
            if A[r][0] == 1 and A[r][1] == 1:
                bfs(r, 1)
            if A[r][C - 1] == 1 and A[r][C - 2] == 1:
                bfs(r, C - 2)

        ret = 0
        for r in range(1, R - 1):
            for c in range(1, C - 1):
                ret += bfs(r, c)
        return ret

    #   runtime; 580ms, 6.75%
    #   memory; 13.8MB, 100.00%
    def numEnclaves(self, A):
        if A is None or 0 == len(A) or 0 == len(A[0]):
            return 0
        R, C = len(A), len(A[0])
        if 1 == R or 1 == C:
            return 0

        def dfs(row, col):
            cnt, stack = 0, [(row, col)]
            while stack:
                r, c = stack.pop()
                if r <= 0 or R - 1 <= r or c <= 0 or C - 1 <= c or 0 == A[r][c]:
                    continue
                cnt += 1
                A[r][c] = 0
                for _r, _c in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    stack.append((_r, _c))
            return cnt
        
        for c in range(1, C - 1):
            if A[0][c] == 1 and A[1][c] == 1:
                dfs(1, c)
            if A[R - 1][c] == 1 and A[R - 2][c] == 1:
                dfs(R - 2, c)
        for r in range(1, R - 1):
            if A[r][0] == 1 and A[r][1] == 1:
                dfs(r, 1)
            if A[r][C - 1] == 1 and A[r][C - 2] == 1:
                dfs(r, C - 2)

        ret = 0
        for r in range(1, R - 1):
            for c in range(1, C - 1):
                ret += dfs(r, c)
        return ret


s = Solution()
data = [([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]], 3),
        ([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]], 0),
        ]
for A, expected in data:
    real = s.numEnclaves(A)
    print('{}, expected {}, real {}, result {}'.format(A, expected, real, expected == real))
