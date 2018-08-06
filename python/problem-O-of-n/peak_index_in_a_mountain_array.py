#   https://leetcode.com/problems/peak-index-in-a-mountain-array

#   https://leetcode.com/problems/peak-index-in-a-mountain-array/solution


class Solution:
    #   1.23%
    def peakIndexInMountainArray(self, A):
        peakIdx, maxVal = None, max(A)
        for i, a in enumerate(A):
            if maxVal == a:
                peakIdx = i
                break
        for i in range(1, peakIdx + 1):
            if A[i - 1] > A[i]:
                return -1
        for i in range(peakIdx, len(A) - 1):
            if A[i] < A[i + 1]:
                return -1
        return peakIdx


s = Solution()
data = [([0, 1, 0], 1),
        ([0, 2, 1, 0], 1),
        ([2, 1, 0], 0),
        ([0, 1, 2, 3], 3),
        ]
for A, expected in data:
    real = s.peakIndexInMountainArray(A)
    print('{}, expected {}, real {}, result {}'.format(A, expected, real, expected == real))
