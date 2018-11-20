#   https://leetcode.com/problems/valid-mountain-array


class Solution:
    #   Wrong Answer
    def validMountainArray0(self, A):
        if len(A) < 3:
            return False
        maxIdx = 0
        for i, a in enumerate(A):
            if A[maxIdx] < a:
                maxIdx = i
        if 0 == maxIdx or maxIdx == len(A) - 1:
            return False
        for i in range(maxIdx - 1, -1, -1):
            if A[i] >= A[maxIdx]:
                return False
        for i in range(maxIdx + 1, len(A)):
            if A[maxIdx] <= A[i]:
                return False
        return True

    #   68ms, 100.00%
    def validMountainArray(self, A):
        if len(A) < 3:
            return False
        maxIdx = 0
        for i in range(1, len(A)):
            if A[i - 1] > A[i]:
                maxIdx = i - 1
                break
        if 0 == maxIdx:
            return False
        for i in range(maxIdx + 1, len(A)):
            if A[i - 1] <= A[i]:
                return False
        return True


s = Solution()
data = [([2, 1], False),
        ([3, 5, 5], False),
        ([0, 3, 2, 1], True),
        ([1, 7, 9, 5, 4, 1, 2], False),
        ]
for A, expected in data:
    real = s.validMountainArray(A)
    print('{}, expected {}, real {}, result {}'.format(A, expected, real, expected == real))
