#   https://leetcode.com/problems/max-number-of-k-sum-pairs


from collections import Counter
from typing import List


class Solution:
    #   https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3608
    #   runtime; 824ms, 22.48%
    #   memory; 26.6MB, 92.48%
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        cnt, l, r = 0, 0, len(nums) - 1
        while l < r:
            cand = nums[l] + nums[r]
            if cand == k:
                cnt += 1
                l += 1
                r -= 1
            elif cand < k:
                l += 1
            else:
                r -= 1
        return cnt


s = Solution()
data = [([1,2,3,4], 5, 2),
        ([3,1,3,4,3], 6, 1),
        ([1,1,1,1,1], 2, 2),
        ]
for nums, k, expect in data:
    real = s.maxOperations(nums, k)
    print(f'{nums} {k} expect {expect} real {real} result {expect == real}')
