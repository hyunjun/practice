#   https://leetcode.com/problems/special-positions-in-a-binary-matrix


from typing import List


class Solution:
    #   runtime; 168ms, 100.00%
    #   memory; 14.2MB, 16.67%
    def numSpecial(self, mat: List[List[int]]) -> int:
        R, C, cnt = len(mat), len(mat[0]), 0
        for r, m in enumerate(mat):
            if sum(m) != 1:
                continue
            for c in range(C):
                if mat[r][c] != 1:
                    continue
                cnt += 1 if sum(mat[y][c] for y in range(R)) == 1 else 0
        return cnt


s = Solution()
mat1 = [[1,0,0],
        [0,0,1],
        [1,0,0]]
mat2 = [[1,0,0],
        [0,1,0],
        [0,0,1]]
mat3 = [[0,0,0,1],
        [1,0,0,0],
        [0,1,1,0],
        [0,0,0,0]]
mat4 = [[0,0,0,0,0],
        [1,0,0,0,0],
        [0,1,0,0,0],
        [0,0,1,0,0],
        [0,0,0,1,1]]
mat5 = [[0,0,0,0,0,1,0,0],
        [0,0,0,0,1,0,0,1],
        [0,0,0,0,1,0,0,0],
        [1,0,0,0,1,0,0,0],
        [0,0,1,1,0,0,0,0]]
data = [(mat1, 1),
        (mat2, 3),
        (mat3, 2),
        (mat4, 3),
        (mat5, 1),
        ]
for mat, expect in data:
    real = s.numSpecial(mat)
    for m in mat:
        print(m)
    print(f'expect {expect} real {real} result {expect == real}')
