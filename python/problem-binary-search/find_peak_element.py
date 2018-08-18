#   https://leetcode.com/problems/find-peak-element

#   https://leetcode.com/problems/find-peak-element/solution


class Solution:
    #   99.05%
    def findPeakElement(self, nums):
        if nums is None or 0 == len(nums):
            return -1
        if 1 == len(nums):
            return 0
        if 2 == len(nums):
            if nums[0] > nums[1]:
                return 0
            return 1
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if (0 == m and nums[m] > nums[m + 1]) or \
               (m == len(nums) - 1 and nums[m - 1] < nums[m]) or \
               (nums[m - 1] < nums[m] > nums[m + 1]):
                return m
            if nums[m - 1] < nums[m + 1]:
                l = m + 1
            else:
                r = m - 1
        return -1


s = Solution()
data = [([1, 2, 3, 1], 2),
        ([1, 2, 1, 3, 5, 6, 4], 5),   #    1 or 5
        ([1, 2, 3], 2),
        ([3, 2, 1], 0),
        ([1, 1, 1], -1),
        ]
for nums, expected in data:
    real = s.findPeakElement(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
