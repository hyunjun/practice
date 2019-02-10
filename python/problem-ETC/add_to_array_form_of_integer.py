#   https://leetcode.com/problems/add-to-array-form-of-integer

#   https://leetcode.com/problems/add-to-array-form-of-integer/solution


class Solution:
    #   runtime; 300ms, 100.00%
    #   memory; 6.8MB, 100.00%
    def addToArrayForm(self, A, K):
        carry = 0
        for i in range(len(A) - 1, -1, -1):
            k = K % 10
            A[i] += (k + carry)
            if 9 < A[i]:
                A[i] -= 10
                carry = 1
            else:
                carry = 0
            K //= 10
        while 1 == carry or 0 < K:
            k = K % 10
            val = carry + k
            if 9 < val:
                val -= 10
                carry = 1
            else:
                carry = 0
            A.insert(0, val)
            K //= 10
        return A


s = Solution()
data = [([1, 2, 0, 0], 34, [1, 2, 3, 4]),
        ([2, 7, 4], 181, [4, 5, 5]),
        ([2, 1, 5], 806, [1, 0, 2, 1]),
        ([9, 9, 9, 9, 9, 9, 9, 9, 9], 1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
        ([0], 23, [2, 3]),
        ([0], 10000, [1, 0, 0, 0, 0])
        ]
for A, K, expected in data:
    real = s.addToArrayForm(A, K)
    print('{}, {}, expected {}, real {}, result {}'.format(A, K, expected, real, expected == real))
