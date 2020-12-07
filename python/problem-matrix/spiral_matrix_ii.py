#   https://leetcode.com/problems/spiral-matrix-ii


from typing import List


class Solution:
    #   https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3557
    #   runtime; 32ms, 60.27%
    #   memory; 14.4MB
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        direction, r, c, num = 2, 0, -1, 1
        while num <= n ** 2:
            if direction == 1:
                r -= 1
            elif direction == 2:
                c += 1
            elif direction == 4:
                r += 1
            elif direction == 8:
                c -= 1
            if c == -1 or c == n or r == n or matrix[r][c] != 0:
                if direction == 1:
                    r += 1
                elif direction == 2:
                    c -= 1
                elif direction == 4:
                    r -= 1
                elif direction == 8:
                    c += 1
                if direction == 8:
                    direction = 1
                else:
                    direction *= 2
                continue
            matrix[r][c] = num
            num += 1
        return matrix


s = Solution()
data = [(3, [[1,2,3],[8,9,4],[7,6,5]]),
        (1, [[1]]),
        ]
for n, expect in data:
    real = s.generateMatrix(n)
    print(f'{n} expect {expect} real {real} result {expect == real}')
