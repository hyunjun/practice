#   https://leetcode.com/problems/complement-of-base-10-integer


import math

class Solution:
    #   runtime; 36ms, 100.00%
    #   memory; 13.1MB, 100.00%
    def bitwiseComplement(self, N):
        if N == 0:
            return 1
        powerOf2 = 1
        while powerOf2 <= N:
            powerOf2 *= 2
        powerOf2 //= 2
        print(powerOf2)
        res = []
        while 0 < powerOf2:
            if powerOf2 <= N:
                N -= powerOf2
                res.append(1)
            else:
                res.append(0)
            powerOf2 //= 2
        print(res)
        print([0 if r == 1 else math.pow(2, len(res) - i - 1) for i, r in enumerate(res)])
        return int(sum([0 if r == 1 else math.pow(2, len(res) - i - 1) for i, r in enumerate(res)]))


s = Solution()
data = [(5, 2),
        (7, 0),
        (10, 5),
        (2, 1),
        ]
for N, expected in data:
    real = s.bitwiseComplement(N)
    print('{}, expected {}, real {}, result {}'.format(N, expected, real, expected == real))
