#   https://leetcode.com/problems/maximum-product-of-three-numbers

#   https://leetcode.com/problems/maximum-product-of-three-numbers/solution


class Solution:
    #   74.59%
    def maximumProduct(self, nums):
        max1, max2, max3, min1, min2 = None, None, None, None, None
        for n in nums:
            if max1 is None or max1 <= n:
                max3 = max2
                max2 = max1
                max1 = n
            elif max2 is None or max2 <= n:
                max3 = max2
                max2 = n
            elif max3 is None or max3 < n:
                max3 = n
            if min1 is None or n <= min1:
                min2 = min1
                min1 = n
            elif min2 is None or n < min2:
                min2 = n
        if min1 < 0 and min2 < 0 and 0 < max1:
            return max(min1 * min2 * max1, max1 * max2 * max3)
        return max1 * max2 * max3


s = Solution()
data = [([1, 2, 3], 6),
        ([1, 2, 3, 4], 24),
        ([1, -2, -4, -6, 5], 120),
        ([-1, -2, -4, -6, -5], -8),
        ]
for nums, expected in data:
    real = s.maximumProduct(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
