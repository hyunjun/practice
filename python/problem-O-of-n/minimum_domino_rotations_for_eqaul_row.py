#   https://leetcode.com/problems/minimum-domino-rotations-for-equal-row


class Solution:
    #   runtime; 128ms, 100.00%
    #   memory; 13.8MB, 100.00%
    def minDominoRotations(self, A, B):
        if A is None or 0 == len(A) or B is None or 0 == len(B) or len(A) != len(B):
            return -1
        aElem, bElem = A[0], B[0]
        aSwapCnt0, aSwapCnt1, aSwapExpect, bSwapCnt0, bSwapCnt1, bSwapExpect = 0, 0, len(A), 0, 0, len(A)
        for i, a in enumerate(A):
            if a != aElem and a != bElem and B[i] != aElem and B[i] != bElem:
                return -1
            if a == aElem and B[i] == aElem:
                aSwapExpect -= 1
            if a == aElem and B[i] != aElem:
                aSwapCnt0 += 1
            if a != aElem and B[i] == aElem:
                aSwapCnt1 += 1
            if a == bElem and B[i] == bElem:
                bSwapExpect -= 1
            if a == bElem and B[i] != bElem:
                bSwapCnt0 += 1
            if a != bElem and B[i] == bElem:
                bSwapCnt1 += 1
        if aSwapCnt0 + aSwapCnt1 == aSwapExpect:
            return min(aSwapCnt0, aSwapCnt1)
        if bSwapCnt0 + bSwapCnt1 == bSwapExpect:
            return min(bSwapCnt0, bSwapCnt1)
        return -1


s = Solution()
data = [([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2], 2),
        ([3, 5, 1, 2, 3], [3, 6, 3, 3, 4], -1),
        ([1,2,1,1,1,2,2,2], [2,1,2,2,2,2,2,2], 1),
        ]
for A, B, expected in data:
    real = s.minDominoRotations(A, B)
    print('{}, {}, expected {}, real {}, result {}'.format(A, B, expected, real, expected == real))
