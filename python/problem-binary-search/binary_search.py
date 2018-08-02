#   https://leetcode.com/problems/binary-search


class Solution:
    #   75.10%
    def search(self, nums, target):
        if nums is None or 0 == len(nums):
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1


s = Solution()
data = [([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
        ([-1, 0, 3, 5, 9, 12], 14, -1),
        ([-1, 0, 3, 5, 9, 12], -3, -1),
        ([-1], -1, 0),
        ([-1], 1, -1),
        ]
for nums, target, expected in data:
    real = s.search(nums, target)
    print('{}, {}, expected {}, real {}, result {}'.format(nums, target, expected, real, expected == real))
