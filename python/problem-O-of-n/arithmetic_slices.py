#   https://leetcode.com/problems/arithmetic-slices

#   https://leetcode.com/problems/arithmetic-slices/solution


class Solution:
    #   3.76%
    def numberOfArithmeticSlices(self, A):
        def getTotalCount(num):
            _sum, cnt = 0, 1
            for i in range(num, 2, -1):
                _sum += cnt
                cnt += 1
            return _sum

        if A is None or len(A) < 3:
            return 0
        diff, prev, res = A[1] - A[0], 0, 0
        for i in range(1, len(A)):
            if diff != A[i] - A[i - 1]:
                res += getTotalCount(i - prev)
                diff = A[i] - A[i - 1]
                prev = i - 1
        res += getTotalCount(len(A) - prev)
        return res


s = Solution()
data = [([1, 3, 5, 7, 9], 6),
        ([1, 2, 3, 4], 3),
        ([1, 2, 3, 5, 7], 2),
        ]
for A, expected in data:
    real = s.numberOfArithmeticSlices(A)
    print('{}, expected {}, real {}, result {}'.format(A, expected, real, expected == real))
