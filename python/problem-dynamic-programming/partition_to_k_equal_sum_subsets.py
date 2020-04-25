#   https://leetcode.com/problems/partition-to-k-equal-sum-subsets

#   https://leetcode.com/problems/partition-to-k-equal-sum-subsets/solution


from collections import Counter
from typing import List


class Solution:
    #   runtime; 92ms, 47.62%
    #   memory; 14.1MB, 5.55%
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if nums is None or not (1 <= len(nums) <= 16) or not (1 <= k <= 16) or not (k <= len(nums)):
            return False
        totalSum = sum(nums)
        subSum = totalSum // k
        if subSum * k != totalSum:
            return False

        if any(n > subSum for n in nums):
            return False

        def addSubSum(acc, idx, arr):
            if 0 == len(arr):
                return all(a == subSum for a in acc)
            for i, a in enumerate(arr):
                if acc[idx] + a < subSum:
                    acc[idx] += a
                    subRes = addSubSum(acc, idx, arr[:i] + arr[i + 1:])
                    if subRes:
                        return True
                    acc[idx] -= a
                elif acc[idx] + a == subSum:
                    acc[idx] += a
                    subRes = addSubSum(acc, idx + 1, arr[:i] + arr[i + 1:])
                    if subRes:
                        return True
                    acc[idx] -= a
            return False

        return addSubSum([0] * k, 0, sorted(nums, reverse=True))


s = Solution()
data = [([4, 3, 2, 3, 5, 2, 1], 4, True),
        ([4, 15, 1, 1, 1, 1, 3, 11, 1, 10], 3, True),
        ([10, 10, 10, 7, 7, 7, 7, 7, 7, 6, 6, 6], 3, True),
        ([2, 2, 2, 2, 3, 4, 5], 4, False),
        ([4, 4, 6, 2, 3, 8, 10, 2, 10, 7], 4, True),
        ([85, 35, 40, 64, 86, 45, 63, 16, 5364, 110, 5653, 97, 95], 7, False),
        ]
for nums, k, expected in data:
    real = s.canPartitionKSubsets(nums, k)
    print(f'{nums} {k} expected {expected} real {real} result {expected == real}')
