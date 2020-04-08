#   move all the zeroes to right
#   in-place


class Solution:
    def moveZeroes(self, nums):
        if nums is None or 0 == len(nums):
            return []
        l, r = 0, len(nums) - 1
        while l < r:
            while l < len(nums) - 1 and nums[l] != 0:
                l += 1
            while 0 < r and nums[r] == 0:
                r -= 1
            if l < r:
                nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


s = Solution()
data = [([1, 0, 8, -1, 10, 0], [1, 10, 8, -1, 0, 0]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([0, 1, 2, 3], [3, 1, 2, 0]),
        ([0, 0, 2, 3], [3, 2, 0, 0]),
        ]
for nums, expected in data:
    print(nums)
    s.moveZeroes(nums)
    print(f'\texpected {expected}, real {nums}, result {expected == nums}')
