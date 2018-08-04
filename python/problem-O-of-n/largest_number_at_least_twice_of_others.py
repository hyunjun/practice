#   https://leetcode.com/problems/largest-number-at-least-twice-of-others

#   https://leetcode.com/problems/largest-number-at-least-twice-of-others/solution


class Solution:
    #   6.68%
    def dominantIndex(self, nums):
        if len(nums) <= 1:
            return 0
        max1, max2 = nums[0], nums[1]
        max1Idx = 0
        if max1 < max2:
            max1, max2 = max2, max1
            max1Idx = 1
        for i, n in enumerate(nums):
            if i < 2:
                continue
            if max1 < n:
                max2 = max1
                max1 = n
                max1Idx = i
            elif max2 < n:
                max2 = n
        if max2 == 0 or max2 * 2 <= max1:
            return max1Idx
        return -1


s = Solution()
data = [([3, 6, 1, 0], 1),
        ([1, 2, 3, 4], -1),
        ([1], 0),
        ([1, 0], 0),
        ]
for nums, expected in data:
    real = s.dominantIndex(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
