#   https://leetcode.com/problems/third-maximum-number
#   89.06%

#   https://leetcode.com/problems/third-maximum-number/discuss/137731/Python-Solution-beats-96


class Solution:
    def thirdMax(self, nums):
        if nums is None or 0 == len(nums):
            return None
        max1st, max2nd, max3rd = None, None, None
        for n in nums:
            if max1st is None or max1st <= n:
                if max1st and max1st < n:
                    max3rd = max2nd
                    max2nd = max1st
                max1st = n
            elif max2nd is None or max2nd <= n < max1st:
                if max2nd and max2nd < n:
                    max3rd = max2nd
                max2nd = n
            elif max3rd is None or max3rd < n < max2nd:
                max3rd = n
        if max3rd is not None:
            return max3rd
        return max1st


s = Solution()
data = [([3, 2, 1], 1),
        ([1, 2], 2),
        ([2, 2, 3, 1], 1),
        ([1, 1, 2, 2], 2),
        ([5, 2, 2], 5),
        ([3, 3, 4, 3, 4, 3, 0, 3, 3], 0)
        ]
for nums, expected in data:
    real = s.thirdMax(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
'''
max1st  max2nd  max3rd  n   nums
x       x       x           3 2 1
3                       3
3       2               2
3       2       1       1

x       x       x           1 2
1       x       x       1
2       1       x       2

x       x       x           2 2 3 1
2       x       x       2
2       x       x       2
3       2       x       3
3       2       1       1

x       x       x           5 2 2
5       x       x       5
5       2       x       2

x       x       x           3 3 4 3 4 3 0 3 3
3       x       x       3
3       x       x       3
4       3       x       4
4       3       x       3
4       3       x       4
4       3       x       3
4       3       0       0
'''
