#   https://www.interviewbit.com/problems/max-sum-contiguous-subarray

#   https://medium.com/solvingalgo/how-to-solve-algorithmic-problems-maximum-sum-of-a-contiguous-subarray-5568adbfc5b


class Solution:
    def maxSubArray(self, A):
        if A is None or 0 == len(A):
            return 0
        if 1 == len(A):
            return A[0]
        curSum, maxSum = A[0], A[0]
        for i, a in enumerate(A):
            if 0 == i:
                continue
            if a + curSum < a:
                curSum = a
            else:
                curSum += a
            maxSum = max(maxSum, curSum)
        return maxSum


s = Solution()
data = [([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([4, -1, 6, -100, 5], 9),
        ]
for A, expected in data:
    real = s.maxSubArray(A)
    print('{}, expected {}, real {}, result {}'.format(A, expected, real, expected == real))
