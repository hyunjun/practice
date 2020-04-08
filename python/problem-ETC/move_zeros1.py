#   https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3286/


class Solution:
    #   runtime; 48ms, 75.52%
    #   memory; 14.9MB
    def moveZeroes(self, nums):
        if nums is None or 0 == len(nums):
            return []
        z = 0
        while z < len(nums) and nums[z] != 0:
            z += 1
        for i in range(z, len(nums)):
            if nums[i] == 0:
                continue
            nums[z] = nums[i]
            z += 1
        for i in range(z, len(nums)):
            nums[i] = 0


s = Solution()
data = [([1, 0, 8, -1, 10, 0], [1, 8, -1, 10, 0, 0]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([0, 1, 2, 3], [1, 2, 3, 0]),
        ([0, 0, 2, 3], [2, 3, 0, 0]),
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0])
        ]
for nums, expected in data:
    print(nums)
    s.moveZeroes(nums)
    print(f'\texpected {expected}, real {nums}, result {expected == nums}')
