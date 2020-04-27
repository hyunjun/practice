#   https://leetcode.com/problems/sort-the-matrix-diagonally


from typing import List


class Solution:
    #   runtime; 80ms, 96.75%
    #   memory; 14MB, 100.00%
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        if mat is None or not (1 <= len(mat) <= 100) or not (1 <= len(mat[0]) <= 100):
            return [[]]
        R, C = len(mat), len(mat[0])
        starts = [(0, c) for c in range(C)] + [(r, 0) for r in range(1, R)]
        for r, c in starts:
            nums = []
            _r, _c = r, c
            while _r < R and _c < C:
                nums.append(mat[_r][_c])
                _r += 1
                _c += 1
            nums = sorted(nums)
            _r, _c, idx = r, c, 0
            while _r < R and _c < C:
                mat[_r][_c] = nums[idx]
                _r += 1
                _c += 1
                idx += 1
        return mat


s = Solution()
data = [([[3,3,1,1],[2,2,1,2],[1,1,1,2]], [[1,1,1,1],[1,2,2,2],[1,2,3,3]]),
        ([[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]], [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]),
        ]
for mat, expected in data:
    print()
    for m in mat:
        print(m)
    real = s.diagonalSort(mat)
    print()
    for e in expected:
        print(e)
    print()
    for r in real:
        print(r)
