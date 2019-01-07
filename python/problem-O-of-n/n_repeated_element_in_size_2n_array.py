#   https://leetcode.com/problems/n-repeated-element-in-size-2n-array

#   https://leetcode.com/problems/n-repeated-element-in-size-2n-array/solution


class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        s = set()
        for a in A:
            if a in s:
                return a
            s.add(a)
        return None


s = Solution()
data = [([1,2,3,3], 3),
        ([2,1,2,5,3,2], 2),
        ([5,1,5,2,5,3,5,4], 5),
        ]
for A, expected in data:
    real = s.repeatedNTimes(A)
    print('{}, expected {}, real {}, result {}'.format(A, expected, real, expected == real))
