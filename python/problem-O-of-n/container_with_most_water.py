#   https://leetcode.com/problems/container-with-most-water


from collections import defaultdict
from typing import List


class Solution:
    #   runtime; 71.00% -> 168ms, 75.03%
    #   memory; 16.4MB, 90.84%
    def maxArea(self, height):
        if height is None or len(height) < 2:
            return 0
        maxSize, l, r = 0, 0, len(height) - 1
        while l < r:
            maxSize = max(maxSize, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxSize

    #   https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3643
    #   Time Limit Exceeded
    def maxArea1(self, height: List[int]) -> int:
        if height is None or len(height) < 2:
            return 0
        d, maxSize = defaultdict(list), 0
        for h in range(max(height), min(height) - 1, -1):
            l, r = 0, len(height) - 1
            while height[l] < h:
                l += 1
            while height[r] < h:
                r -= 1
            maxSize = max(maxSize, (r - l) * min(height[l], height[r]))
        return maxSize


data = [([1, 2, 3, 4, 5], 6),
        ([5, 2, 3, 4, 5], 20),
        ([1, 1], 1),
        ([1, 2, 1], 2),
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ]
s = Solution()
for height, expect in data:
    real = s.maxArea(height)
    print(f'{height}, expect {expect}, real {real}, result {expect == real}')
