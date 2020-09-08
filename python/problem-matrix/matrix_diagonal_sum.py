#   https://leetcode.com/problems/matrix-diagonal-sum


from typing import List


class Solution:
    #   runtime; 104ms, 98.80%
    #   memory; 13.9MB, 40.90%
    def diagonalSum(self, mat: List[List[int]]) -> int:
        N = len(mat)
        res = sum(mat[n][n] for n in range(N)) + sum(mat[n][N - n - 1] for n in range(N))
        if N % 2 == 1:
            res -= mat[N // 2][N // 2]
        return res


s = Solution()
mat1 = [[1,2,3],
        [4,5,6],
        [7,8,9]]
mat2 = [[1,1,1,1],
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1]]
mat3 = [[5]]
data = [(mat1, 25),
        (mat2, 8),
        (mat3, 5),
        ]
for mat, expect in data:
    real = s.diagonalSum(mat)
    for m in mat:
        print(m)
    print(f'expect {expect} real {real} result {expect == real}')
