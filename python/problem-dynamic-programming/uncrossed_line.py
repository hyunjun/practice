#   https://leetcode.com/problems/uncrossed-lines


class Solution:
    #   Time Limit Exceeded
    def maxUncrossedLines0(self, A, B):
        if A is None or 0 == len(A) or B is None or 0 == len(B):
            return 0
        aOnly, bOnly = set(A) - set(B), set(B) - set(A)
        A = [a for a in A if a not in aOnly]
        B = [b for b in B if b not in bOnly]

        self.cnt = -float('inf')
        def matchCount(L, l, R, r, cnt):
            if len(L) <= l or len(R) <= r:
                self.cnt = max(self.cnt, cnt)
            else:
                orgR = r
                while r < len(R):
                    if L[l] == R[r]:
                        matchCount(L, l + 1, R, r + 1, cnt + 1)
                    r += 1
                matchCount(L, l + 1, R, orgR, cnt)

        matchCount(A, 0, B, 0, 0)
        matchCount(B, 0, A, 0, 0)
        return self.cnt

    #   Time Limit Exceeded
    def maxUncrossedLines1(self, A, B):
        if A is None or 0 == len(A) or B is None or 0 == len(B):
            return 0

        aOnly, bOnly = set(A) - set(B), set(B) - set(A)
        A = [a for a in A if a not in aOnly]
        B = [b for b in B if b not in bOnly]

        self.cnt = -float('inf')
        def matchCount(L, l, R, r, cnt):
            #print(L, l, R, r, cnt)
            if len(L) <= l or len(R) <= r:
                self.cnt = max(self.cnt, cnt)
            else:
                if L[l] == R[r]:
                    matchCount(L, l + 1, R, r + 1, cnt + 1)
                else:
                    matchCount(L, l + 1, R, r, cnt)
                    matchCount(L, l, R, r + 1, cnt)

        matchCount(A, 0, B, 0, 0)
        return self.cnt

    #   runtime; 96ms, 99.60%
    #   memory; 13.5MB, 100.00%
    def maxUncrossedLines(self, A, B):
        if A is None or 0 == len(A) or B is None or 0 == len(B):
            return 0

        aOnly, bOnly = set(A) - set(B), set(B) - set(A)
        A = [a for a in A if a not in aOnly]
        B = [b for b in B if b not in bOnly]
        if 0 == len(A) or 0 == len(B):
            return 0
        dp = [[0] * len(A) for _ in range(len(B))]

        dp[0][0] = 1 if A[0] == B[0] else 0

        for i in range(1, len(dp)):
            if A[0] == B[i]:
                dp[i][0] = 1
            else:
                dp[i][0] = dp[i - 1][0]
        for j in range(1, len(dp[0])):
            if A[j] == B[0]:
                dp[0][j] = 1
            else:
                dp[0][j] = dp[0][j - 1]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if A[j] == B[i]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]


s = Solution()
data = [([1, 4, 2], [1, 2, 4], 2),
        ([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2], 3),
        ([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1], 2),
        ([3,1,2,1,4,1,2,2,5,3,2,1,1,4,5,2,3,2,5,5], [2,4,1,2,3,4,2,4,5,5,1,1,2,1,1,1,5,4,1,4,2,1,5,4,2,3,1,5,2,1], 14),
        ([1], [3], 0),
        ]
'''
    1 1 5
1   1 1 0
5   0 1 2
1   1 2 2
    3 1 2 1 4 1 2 2 5 3 2 1 1 4 5 2 3 2 5 5
2   0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
4   0 0 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
1   0 1 1 2 2 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
2   0 1 2 2 2 2 4 4 4 4 4 4 4 4 4 4 4 4 4 4
3   1 1 1 2 2 2 4 4 4 5 5 5 5 5 5 5 5 5 5 5
4   1 1 1 1 3 3 4 4 4 5 5 5 5 6 6 6 6 6 6 6
2   1
4   1
5   1
5   1
1   1
1   1
2   1
1   1
1   1
1   1
5   1
4   1
1   1
4   1
2   1
1   1
5   1
4   1
2   1
3   1
1   1
5   1
2   1
1   1
'''
for A, B, expected in data:
    real = s.maxUncrossedLines(A, B)
    print('{}, {}, expected {}, real {}, result {}'.format(A, B, expected, real, expected == real))
