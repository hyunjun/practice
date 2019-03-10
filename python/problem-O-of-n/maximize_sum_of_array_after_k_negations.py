#   https://leetcode.com/problems/maximize-sum-of-array-after-k-negations


class Solution:
    #   runtime; 20ms, 100.00%
    #   memory; 11MB, 100.00%
    def largestSumAfterKNegations(self, A, K):
        if A is None or 0 == len(A):
            return 0
        sortedA = sorted(A)
        negNum = len([i for i in sortedA if i < 0])
        if 0 < negNum:
            if K <= negNum:
                for i in range(K):
                    sortedA[i] = -sortedA[i]
                return sum(sortedA)
            for i in range(negNum):
                sortedA[i] = -sortedA[i]
            K -= negNum
            sortedA = sorted(sortedA)
        if 0 == sortedA[0] or 0 == K % 2:
            return sum(sortedA)
        return sum(sortedA[1:]) - sortedA[0]


s = Solution()
data = [([4, 2, 3], 1, 5),
        ([3, -1, 0, 2], 3, 6),
        ([2, -3, -1, 5, -4], 2, 13),
        ]
for A, K, expected in data:
    real = s.largestSumAfterKNegations(A, K)
    print('{}, {}, expected {}, real {}, result {}'.format(A, K, expected, real, expected == real))
'''
1. sort A
2. there are negative values
    if K <= # of negative values:
        make K negative values positive, and sum
    else:
        make all negative values positive
        K -= # of negative values
    sort A
3.
    if there is 0 or 0 == K % 2 -> just sum all
    if 1 == k % 2 -> make it smallest negative
'''
