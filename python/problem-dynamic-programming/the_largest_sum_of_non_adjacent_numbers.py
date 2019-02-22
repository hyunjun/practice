#   https://medium.com/@karangupta_3592/given-a-list-of-integers-write-a-function-that-returns-the-largest-sum-of-non-adjacent-numbers-9e368f8e69c8


class Solution:
    def largestSumOfNonAdjacent(self, nums):
        if nums is None or 0 == len(nums):
            return 0
        if 2 == len(nums):
            return max(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i, n in enumerate(nums):
            for j in [i + 2, i + 3]:
                if j < len(nums):
                    dp[j] = max(dp[j], nums[j] + dp[i])
            print(dp)
        return dp[-1]


s = Solution()
data = [([2, 4, 6, 2, 5], 13),
        ([5, 1, 1, 5], 10),
        ]
for nums, expected in data:
    real = s.largestSumOfNonAdjacent(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
