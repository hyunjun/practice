#   https://leetcode.com/problems/house-robber
#   21.86%

#   https://leetcode.com/problems/house-robber/discuss/55696/Python-solution-3-lines.


class Solution:
    def rob(self, nums):
        if nums is None or 0 == len(nums):
            return 0
        maximized = 0
        for i, n in enumerate(nums):
            if 2 < i:
                nums[i] += max(nums[i - 2], nums[i - 3])
            elif 1 < i:
                nums[i] += nums[i - 2]
            if maximized < nums[i]:
                maximized = nums[i]
        return maximized


s = Solution()
data = [([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([13, 1, 1, 4, 2], 17),
        ([2, 1, 1, 2], 4)
        ]
for nums, expected in data:
    real = s.rob(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
