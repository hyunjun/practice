#    https://leetcode.com/problems/sort-array-by-parity-ii

#   https://leetcode.com/problems/sort-array-by-parity-ii/solution


class Solution:
    #   132ms
    def sortArrayByParityII(self, A):
        if A is None or len(A) < 2:
            return A
        res, oddIdx, evenIdx = [None] * len(A), 1, 0
        for a in A:
            if 0 == a % 2:
                res[evenIdx] = a
                evenIdx += 2
            else:
                res[oddIdx] = a
                oddIdx += 2
        return res


s = Solution()
data = [([4, 2, 5, 7], [4, 5, 2, 7]),
        ]
for A, expected in data:
    real = s.sortArrayByParityII(A)
    print('{}, expected {}, real {}, result {}'.format(A, expected, real, expected == real))
