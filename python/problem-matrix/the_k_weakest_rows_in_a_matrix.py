#   https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix


from typing import List


class Solution:
    #   runtime; 116ms, 46.49%
    #   memory; 12.9MB, 100.00%
    def kWeakestRows0(self, mat: List[List[int]], k: int) -> List[int]:
        R, C = len(mat), len(mat[0])
        if not (2 <= R <= 100 or 2 <= C <= 100 or 1 <= k <= R):
            return []
        res, visited = [], set()
        for c in range(C):
            for r in range(R):
                if mat[r][c] == 0 and r not in visited:
                    res.append(r)
                    visited.add(r)
                    if len(res) == k:
                        return res
        if len(res) == 0:
            return [0]
        if len(res) < k:
            for r in range(R):
                if r in visited:
                    continue
                res.append(r)
                visited.add(r)
                if len(res) == k:
                    break
        return res

    #   https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3641
    #   runtime; 112ms, 48.13%
    #   memory; 14.6MB, 76.29%
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [i for i, _ in sorted([(i, row) for i, row in enumerate(mat)], key=lambda t: (t[1].count(1), t[0]))[:k]]


s = Solution()
mat1 = [[1,1,0,0,0],
        [1,1,1,1,0],
        [1,0,0,0,0],
        [1,1,0,0,0],
        [1,1,1,1,1]]
mat2 = [[1,0,0,0],
        [1,1,1,1],
        [1,0,0,0],
        [1,0,0,0]]
mat3 = [[1,1,1,1,1,1],
        [1,1,1,1,1,1],
        [1,1,1,1,1,1]]
mat4 = [[1,0],
        [1,0],
        [1,0],
        [1,1]]
mat5 = [[1,1,0],
        [1,1,0],
        [1,1,1],
        [1,1,1],
        [0,0,0],
        [1,1,1],
        [1,0,0]]
data = [(mat1, 3, [2, 0, 3]),
        (mat2, 2, [0, 2]),
        (mat3, 1, [0]),
        (mat4, 4, [0, 1, 2, 3]),
        (mat5, 6, [4, 6, 0, 1, 2, 3]),
        ]
for mat, k, expect in data:
    real = s.kWeakestRows(mat, k)
    for m in mat:
        print(m)
    print(f'\t{k} expect {expect} real {real} result {expect == real}')
