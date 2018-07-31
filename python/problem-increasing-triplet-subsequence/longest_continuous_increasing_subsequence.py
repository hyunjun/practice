#   https://leetcode.com/problems/longest-continuous-increasing-subsequence

#   https://leetcode.com/problems/longest-continuous-increasing-subsequence/solution


class Solution:
    #   56.99%
    def findLengthOfLCIS(self, nums):
        if nums is None or 0 == len(nums):
            return 0
        s, e, maxLen = 0, 0, 1
        for i, n in enumerate(nums):
            if 0 == i:
                continue
            if nums[i - 1] >= n:
                e = i
                maxLen = max(maxLen, e - s)
                s = i
        maxLen = max(maxLen, len(nums) - s)
        return maxLen


s = Solution()
data = [([1, 3, 5, 4, 7], 3),
        ([2, 2, 2, 2, 2], 1),
        ([1, 2, 3, 4], 4),
        ([4, 3, 2, 1], 1),
        ([2], 1),
        ]
for nums, expected in data:
    real = s.findLengthOfLCIS(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
