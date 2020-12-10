#   https://leetcode.com/problems/valid-mountain-array


from typing import List


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
    def validMountainArray1(self, A):
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

    #   https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3561
    #   runtime; 208ms, 28.98%
    #   memory; 15.6MB
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        pinnacle = arr[0]
        for i, a in enumerate(arr):
            if 0 == i:
                continue
            if arr[i - 1] == a:
                return False
            if arr[i - 1] > a:
                pinnacle = i - 1
                break
        if pinnacle == 0:
            return False
        for i in range(pinnacle + 1, len(arr)):
            if arr[i - 1] <= arr[i]:
                return False
        return True


s = Solution()
data = [([2, 1], False),
        ([3, 5, 5], False),
        ([0, 3, 2, 1], True),
        ([1, 7, 9, 5, 4, 1, 2], False),
        ([9,8,7,6,5,4,3,2,1,0], False),
        ]
for A, expected in data:
    real = s.validMountainArray(A)
    print('{}, expected {}, real {}, result {}'.format(A, expected, real, expected == real))
