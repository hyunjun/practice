#   https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

#   https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/solution


class Solution:
    #   runtime; 16ms, 100.00%
    #   memory; 10.8MB, 71.74%
    def findMin(self, nums):
        if nums is None or 0 == len(nums):
            return None
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if l == r or l == m and nums[l] < nums[r] or 0 <= m - 1 and nums[m - 1] > nums[m] < nums[m + 1]:
                return nums[m]
            if nums[m] < nums[r]:
                r = m - 1
            elif nums[m] > nums[r]:
                l = m + 1
        return None
'''
a b c
a < b < c
a < b > c b is the biggest
a > b < c b is the smallest
'''

s = Solution()
data = [([3, 4, 5, 1, 2], 1),
        ([4, 5, 1, 2, 3], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([0, 1, 2, 4, 5, 6, 7], 0),
        ([0, 1, 2, 4, 5, 7], 0),
        ([7, 6, 5, 4, 2, 1, 0], 0),
        ([7, 6, 5, 4, 1, 0], 0),
        ([7, 0, 1, 2, 4, 5, 6], 0),
        ([7, 0, 1, 2, 4, 6], 0),
        ]
for nums, expected in data:
    real = s.findMin(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
