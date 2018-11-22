#   https://leetcode.com/problems/delete-columns-to-make-sorted

#   https://leetcode.com/problems/delete-columns-to-make-sorted/solution


class Solution:
    #   276ms, 30.21%
    def minDeletionSize(self, A):
        nonSorted = 0
        for i in range(len(A[0])):
            for c in range(1, len(A)):
                if A[c - 1][i] > A[c][i]:
                    nonSorted += 1
                    break
        return nonSorted


s = Solution()
data = [(["cba","daf","ghi"], 1),
        (["a","b"], 0),
        (["zyx","wvu","tsr"], 3),
        (["rrjk","furt","guzm"], 2),
        ]
for A, expected in data:
    real = s.minDeletionSize(A)
    print('{}, expected {}, real {}, result {}'.format(A, expected, real, expected == real))
