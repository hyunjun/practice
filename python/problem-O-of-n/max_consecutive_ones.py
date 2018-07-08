#   https://leetcode.com/problems/max-consecutive-ones
#   12.68%


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        if nums is None or 0 == len(nums):
            return 0
        if 1 == len(nums):
            if 0 == nums[0]:
                return 0
            else:
                return 1
        start, end, maxConsecutiveNum = -1, -1, 0
        for i, n in enumerate(nums):
            if i == 0 and 1 == n:
                start = 0
                continue
            if 0 == nums[i - 1] and 1 == n:
                start = i
            elif 1 == nums[i - 1] and 0 == n:
                maxConsecutiveNum = max(maxConsecutiveNum, i - start)
            elif i == len(nums) - 1 and 1 == n:
                maxConsecutiveNum = max(maxConsecutiveNum, i - start + 1)
        return maxConsecutiveNum


s = Solution()
data = [([1, 1, 0, 1, 1, 1], 3),
        ([0], 0),
        ([1], 1),
        ([1, 1, 1, 1], 4),
        ]
for nums, expected in data:
    real = s.findMaxConsecutiveOnes(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
