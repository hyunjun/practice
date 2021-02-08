#   https://leetcode.com/problems/monotonic-array

#   https://leetcode.com/problems/monotonic-array/solution


from typing import List


class Solution:
    #   runtime; 104ms, 87.34%
    def isMonotonic0(self, A):
        if A is None or 0 == len(A):
            return False

        def isIncreasing():
            for i, a in enumerate(A):
                if 0 == i:
                    continue
                if A[i - 1] > a:
                    return False
            return True

        def isDecreasing():
            for i in range(len(A) - 2, -1, -1):
                if A[i] < A[i + 1]:
                    return False
            return True

        if isIncreasing() or isDecreasing():
            return True
        return False

    #   runtime; 516ms, 56.96%
    #   memory; 19.8MB, 5.26%
    def isMonotonic(self, A: List[int]) -> bool:
        if A is None or not (1 <= len(A) <= 50000):
            return False

        def isM(func, arr):
            return all(func(arr[i - 1], arr[i]) for i in range(1, len(arr)))

        def isMInc(arr):
            return isM(lambda a, b: a <= b, arr)

        def isMDec(arr):
            return isM(lambda a, b: a >= b, arr)

        return isMInc(A) or isMDec(A)


s = Solution()
data = [([1, 2, 2, 3], True),
        ([6, 5, 4, 4], True),
        ([1, 3, 2], False),
        ([1, 2, 4, 5], True),
        ([1, 1, 1], True),
        ]
for A, expected in data:
    real = s.isMonotonic(A)
    print('{}, expected {}, real {}, result {}'.format(A, expected, real, expected == real))
