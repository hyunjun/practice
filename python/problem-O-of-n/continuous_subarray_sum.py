#   https://leetcode.com/problems/continuous-subarray-sum


class Solution:
    #   21.11%
    def checkSubarraySum(self, nums, k):
        if nums is None or len(nums) <= 1:
            return False
        if 0 == k:
            if 0 == sum(nums):
                return True
            return False
        sums = nums[:]
        for i, n in enumerate(nums):
            if 0 == i:
                continue
            sums[i] += sums[i - 1]
            if 0 == sums[i] % k:
                return True
        for i, s in enumerate(sums):
            if 0 == i:
                continue
            for j in range(0, i):
                s -= nums[j]
                if 0 == s % k:
                    return True
        return False


s = Solution()
data = [([23, 2, 4, 6, 7], 6, True),
        ([23, 2, 6, 4, 7], 10, True),
        ([23, 2, 6, 4, 7], 6, True),
        ([23, 2, 6, 4, 7], 0, False),
        ([0], 0, False),
        ([0, 0], 0, True),
        ]
for nums, k, expected in data:
    real = s.checkSubarraySum(nums, k)
    print('{}, {}, expected {}, real {}, result {}'.format(nums, k, expected, real, expected == real))
