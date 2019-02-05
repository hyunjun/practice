#   https://leetcode.com/problems/largest-perimeter-triangle

#   https://leetcode.com/problems/largest-perimeter-triangle/solution


class Solution:
    #   72ms, 99.03%
    def largestPerimeter(self, A):
        sortedA = sorted(A, reverse=True)
        for i in range(len(sortedA) - 2):
            if sortedA[i] < sortedA[i + 1] + sortedA[i + 2]:
                return sum(sortedA[i : i + 3])
        return 0


s = Solution()
data = [([2, 1, 2], 5),
        ([1, 2, 1], 0),
        ([3, 2, 3, 4], 10),
        ([3, 6, 2, 3], 8),
        ]
for A, expected in data:
    real = s.largestPerimeter(A)
    print('{}, expected {}, real {}, result {}'.format(A, expected, real, expected == real))
