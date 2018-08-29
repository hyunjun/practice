#   https://leetcode.com/problems/fair-candy-swap

#   https://leetcode.com/problems/fair-candy-swap/solution


class Solution:
    #   26.65%
    def fairCandySwap(self, A, B):
        setA, setB = set(A), set(B)
        sumA, sumB = sum(A), sum(B)
        total = (sumA + sumB) // 2
        targets = (total - sumA, total - sumB)
        for a in A:
            if a + targets[0] in setB:
                if a + targets[0] + targets[1] in setA:
                    return [a, a + targets[0]]
        return []


s = Solution()
data = [([1, 1], [2, 2], [1, 2]),
        ([1, 2], [2, 3], [1, 2]),
        ([2], [1, 3], [2, 3]),
        ([1, 2, 5], [2, 4], [5, 4]),
        ]
for A, B, expected in data:
    real = s.fairCandySwap(A, B)
    print('{}, {}, expected {}, real {}, result {}'.format(A, B, expected, real, expected == real))
