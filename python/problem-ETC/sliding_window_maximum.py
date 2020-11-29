#   https://leetcode.com/problems/sliding-window-maximum


from typing import List


class Solution:
    #   https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/567/week-4-november-22nd-november-28th/3546
    #   runtime; 2152ms
    #   memory; 30.2MB, 23.78%
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if nums is None or len(nums) < k:
            return []
        curMax, maxes, ret = float('-inf'), [], []
        for i, n in enumerate(nums):
            while 0 < len(maxes) and k <= i - maxes[0][0]:
                maxes.pop(0)
            while 0 < len(maxes) and maxes[-1][1] <= n:
                maxes.pop()
            maxes.append((i, n))
            if k - 1 <= i:
                ret.append(maxes[0][1])
        return ret


s = Solution()
data = [([1,3,-1,-3,5,3,6,7], 3, [3,3,5,5,6,7]),
        ([1], 1, [1]),
        ([1,-1], 1, [1,-1]),
        ([9,11], 2, [11]),
        ([4,-2], 2, [4]),
        ([7, 2, 4], 2, [7, 4]),
        ([1,3,1,2,0,5], 3, [3, 3, 2, 5]),
        ]
for nums, k, expect in data:
    real = s.maxSlidingWindow(nums, k)
    print(f'{nums} {k} expect {expect} real {real} result {expect == real}')
