#   https://leetcode.com/problems/longest-turbulent-subarray

#   https://leetcode.com/problems/longest-turbulent-subarray/solution


class Solution:
    #   runtime; 232ms, 15.89%
    #   memory; 16.2MB, 32.96%
    def maxTurbulenceSize(self, A):
        if A is None or 0 == len(A):
            return 0
        if 1 == len(A):
            return 1
        s, maxLen = 0, 1
        for i in range(len(A) - 1):
            if i % 2 == 1 and A[i] > A[i + 1] or i % 2 == 0 and A[i] < A[i + 1]:
                e = i + 1
                maxLen = max(maxLen, e - s + 1)
            else:
                s = e = i + 1
        s = 0
        for i in range(len(A) - 1):
            if i % 2 == 1 and A[i] < A[i + 1] or i % 2 == 0 and A[i] > A[i + 1]:
                e = i + 1
                maxLen = max(maxLen, e - s + 1)
            else:
                s = e = i + 1
        return maxLen


s = Solution()
data = [([9, 4, 2, 10, 7, 8, 8, 1, 9], 5),
        ([4, 8, 12, 16], 2),
        ([100], 1),
        ([9, 9], 1),
        ([0, 1, 1, 0, 1, 0, 1, 1, 0, 0], 5),
        ]
for A, expected in data:
    real = s.maxTurbulenceSize(A)
    print('{}, expected {}, real {}, result {}'.format(A, expected, real, expected == real))
