#   https://leetcode.com/problems/prison-cells-after-n-days

#   https://math.stackexchange.com/questions/3311568/why-does-this-pattern-repeat-after-14-cycles-instead-of-256-can-you-give-a-proo/3311963#3311963


from typing import List


class Solution:
    #   https://leetcode.com/submissions/detail/361527930/?from=/explore/featured/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3379
    #   runtime; 36ms, 85.99%
    #   memory; 13.6MB, 95.66%
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        if 8 != len(cells) or not (1 <= N <= 10 ** 9):
            return []
        tmpCells = cells[:]
        N %= 14
        if 0 == N:
            N = 14
        while N > 0:
            tmpCells[0] = tmpCells[7] = 0
            for i in range(1, 7):
                if cells[i - 1] == cells[i + 1]:
                    tmpCells[i] = 1
                else:
                    tmpCells[i] = 0
            cells = tmpCells[:]
            N -= 1
        return cells


s = Solution()
data = [([0, 1, 0, 1, 1, 0, 0, 1], 7, [0, 0, 1, 1, 0, 0, 0, 0]),
        ([1, 0, 0, 1, 0, 0, 1, 0], 1000000000, [0, 0, 1, 1, 1, 1, 1, 0]),
        ([1, 0, 0, 1, 0, 0, 0, 1], 826, [0,  1,  1,  0,  1,  1,  1,  0]),
        ]
for cells, N, expect in data:
    real = s.prisonAfterNDays(cells, N)
    print(f'{cells} {N} expect {expect} real {real} result {expect == real}')
