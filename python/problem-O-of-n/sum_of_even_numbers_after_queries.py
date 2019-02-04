#   https://leetcode.com/problems/sum-of-even-numbers-after-queries

#   https://leetcode.com/problems/sum-of-even-numbers-after-queries/solution


class Solution:
    #   172ms, 100.00%
    def sumEvenAfterQueries(self, A, queries):
        if A is None or 0 == len(A):
            return 0
        sumEven, ret = sum([a for a in A if 0 == a % 2]), [None] * len(A)
        for i, (n, idx) in enumerate(queries):
            cand = n + A[idx]
            print('[{}] cand num {}'.format(i, cand))
            if 0 == A[idx] % 2:
                sumEven -= A[idx]
            if 0 == cand % 2:
                sumEven += cand
            ret[i] = sumEven
            A[idx] = cand
            print('\t{}'.format(A))
        return ret


s = Solution()
data = [([1, 2, 3, 4], [[1, 0], [-3, 1], [-4, 0], [2, 3]], [8, 6, 2, 4]),
        ([1], [[4, 0]], [0]),
        ([4], [[5, 0]], [0]),
        ]
for A, queries, expected in data:
    real = s.sumEvenAfterQueries(A, queries)
    print('{}, {}, expected {}, real {}, result {}'.format(A, queries, expected, real, expected == real))
