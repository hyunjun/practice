#   https://leetcode.com/problems/subarray-sum-equals-k

#   https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3307


from collections import defaultdict
from typing import List


class Solution:
    #   Brute Force
    def subarraySum0(self, nums: List[int], k: int) -> int:
        if nums is None or not (1 <= len(nums) <= 20000) or not (-10 ** 7 <= k <= 10 ** 7):
            return 0
        cnt = 0
        for i, n in enumerate(nums):
            curSum = 0
            for j in range(i, len(nums)):
                curSum += nums[j]
                if curSum == k:
                    cnt += 1
        return cnt

    #   runtime; 136ms, 12.67%
    #   memory; 18.5MB, 12.00%
    def subarraySum(self, nums: List[int], k: int) -> int:
        if nums is None or not (1 <= len(nums) <= 20000) or not (-10 ** 7 <= k <= 10 ** 7):
            return 0
        curSum, subSums, subSumDict = 0, [], defaultdict(list)
        for i, n in enumerate(nums):
            curSum += n
            subSums.append(curSum)
            subSumDict[curSum].append(i)
        cnt = 0
        if k in subSumDict:
            cnt += len(subSumDict[k])
        for i in range(len(nums) - 1, -1, -1):
            target = subSums[i] - k
            if target in subSumDict:
                cnt += sum([1 if j < i else 0 for j in subSumDict[target]])
        return cnt


s = Solution()
data = [([1, 1, 1], 2, 2),
        ([1, 2, 3, 2, 1, 2, 3], 5, 4),
        ([1], 0, 0),
        ([-1, -1, 1], 0, 1),
        ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0, 55),
        ]
for nums, k, expected in data:
    real = s.subarraySum(nums, k)
    print(f'{nums} {k} expected {expected} real {real} result {expected == real}')
