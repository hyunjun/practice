#   https://leetcode.com/problems/sort-array-by-parity

#   https://leetcode.com/problems/sort-array-by-parity/solution


class Solution:
    #   18.40%
    def sortArrayByParity(self, A):
        if A is None or len(A) < 2:
            return A
        res = list(filter(lambda t: t % 2 == 0, A))
        res.extend(list(filter(lambda t: t % 2 == 1, A)))
        return res


s = Solution()
data = [([3, 1, 2, 4], [2, 4, 3, 1]),
        ]
for A, expected in data:
    real = s.sortArrayByParity(A)
    print('{}, expected {}, real {}, result {}'.format(A, expected, real, expected == real))
