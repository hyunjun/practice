#   https://leetcode.com/problems/maximum-subarray
#   97.13%


class Solution:
    def maxSubArray(self, nums):
        if nums is None or 0 == len(nums):
            return 0
        curSum, maxSum = nums[0], nums[0]
        for i in range(1, len(nums)):
            if curSum + nums[i] < nums[i]:
                curSum = nums[i]
            else:
                curSum += nums[i]
            maxSum = max(maxSum, curSum)
        return maxSum


s = Solution()
data = [([1, 2], 3), ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6)]
for nums, expected in data:
    real = s.maxSubArray(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
