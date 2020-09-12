#   https://leetcode.com/problems/combination-sum-iv


from typing import List


class Solution:
    #   Time Limit Exceeded
    def combinationSum4_0(self, nums: List[int], target: int) -> int:

        self.res = set()
        def getSum(acc, curSum):
            for n in nums:
                if curSum + n > target:
                    continue
                acc.append(n)
                if curSum + n == target:
                    self.res.add(tuple(acc))
                else:
                    getSum(acc, curSum + n)
                acc.pop()
        getSum([], 0)

        return len(self.res)

    #   runtime; 52ms, 45.11%
    #   memory; 14.1MB, 58.67%
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, len(dp)):
            for n in nums:
                if i < n:
                    continue
                if n == 1:
                    dp[i] = dp[i - 1]
                elif 0 <= i - n:
                    dp[i] += dp[i - n]
        return dp[-1]


s = Solution()
data = [([1, 2, 3], 4, 7),
        ([4, 2, 1], 32, 39882198),
        ([4, 3, 2], 32, 74594),
        ]
for nums, target, expect in data:
    real = s.combinationSum4(nums, target)
    print(f'{nums} {target} expect {expect} real {real} result {expect == real}')
