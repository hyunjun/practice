#   https://leetcode.com/problems/binary-gap

#   https://leetcode.com/problems/binary-gap/solution


class Solution:
    #   14.63%
    def binaryGap(self, N):
        idx, indices = 0, []
        while 0 < N:
            if N & 0x1:
                indices.append(idx)
            idx += 1
            N >>= 1
        maxDiff = 0
        for i, idx in enumerate(indices):
            if 0 == i:
                continue
            maxDiff = max(maxDiff, idx - indices[i - 1])
        return maxDiff


s = Solution()
data = [(22, 2),
        (5, 2),
        (6, 1),
        (8, 0),
        ]
for N, expected in data:
    real = s.binaryGap(N)
    print('{}, expected {}, real {}, result {}'.format(N, expected, real, expected == real))
