#   https://leetcode.com/problems/sort-array-by-parity

#   https://leetcode.com/problems/sort-array-by-parity/solution


class Solution:
    #   18.40%
    def sortArrayByParity0(self, A):
        if A is None or len(A) < 2:
            return A
        res = list(filter(lambda t: t % 2 == 0, A))
        res.extend(list(filter(lambda t: t % 2 == 1, A)))
        return res

    #   https://leetcode.com/explore/featured/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3431
    #   runtime; 80ms, 88.40%
    #   memory; 14.5MB, 27.95%
    def sortArrayByParity1(self, A: List[int]) -> List[int]:
        return [a for a in A if a % 2 == 0] + [a for a in A if a % 2 == 1]

    #   runtime; 100ms, 41.59%
    #   memory; 14.6MB, 8.14%
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        e, o = [], []
        for a in A:
            if a % 2 == 0:
                e.append(a)
            else:
                o.append(a)
        return e + o


s = Solution()
data = [([3, 1, 2, 4], [2, 4, 3, 1]),
        ]
for A, expect in data:
    real = s.sortArrayByParity(A)
    print(f'{A}, expect {expect}, real {real}, result {expect == real}')
