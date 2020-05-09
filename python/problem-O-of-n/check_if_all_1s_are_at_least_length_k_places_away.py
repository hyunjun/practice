#   https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away


from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if 0 == k:
            return True
        if nums is None or not (1 <= len(nums) <= 10 ** 5):
            return False
        s = 0
        while s < len(nums) and nums[s] == 0:
            s += 1
        for i in range(s + 1, len(nums)):
            if 1 == nums[i]:
                if i - s > k:
                    s = i
                else:
                    return False
        return True


s = Solution()
data = [([1,0,0,0,1,0,0,1], 2, True),
        ([1,0,0,1,0,1], 2, False),
        ([1,1,1,1,1], 0, True),
        ([0,1,0,1], 1, True),
        ]
for nums, k, expected in data:
    real = s.kLengthApart(nums, k)
    print(f'{nums} {k} expected {expected} real {real} result {expected == real}')
