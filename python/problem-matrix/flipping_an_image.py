#   https://leetcode.com/problems/flipping-an-image

#   https://leetcode.com/problems/flipping-an-image/solution


from typing import List


class Solution:
    #   11.23%
    def flipAndInvertImage(self, A):
        row, column = len(A), len(A[0])
        for r in range(row):
            i, j = 0, column - 1
            while i < j:
                A[r][i], A[r][j] = A[r][j], A[r][i]
                i += 1
                j -= 1
            for c in range(column):
                A[r][c] = 0 if 1 == A[r][c] else 1
        return A

    #   https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/565/week-2-november-8th-november-14th/3526/
    #   runtime; 48ms, 79.72%
    #   memory; 14.3MB
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        if len(A) < 1 or len(A[0]) < 1:
            return A

        R, C = len(A), len(A[0])

        def reverseAndInvert(arr):
            l, r = 0, C - 1
            while l <= r:
                for row in range(R):
                    arr[row][l], arr[row][r] = arr[row][r] ^ 1, arr[row][l] ^ 1
                l += 1
                r -= 1
            return arr

        return reverseAndInvert(A)


s = Solution()
data = [([[1,1,0],[1,0,1],[0,0,0]], [[1,0,0],[0,1,0],[1,1,1]]),
        ([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]], [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]),
        ]
for A, expected in data:
    real = s.flipAndInvertImage(A)
    print('{}, expected {}, real {}, result {}'.format(A, expected, real, expected == real))
