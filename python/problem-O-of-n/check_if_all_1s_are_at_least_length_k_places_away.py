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

    #   https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3616
    #   runtime; 588ms, 34.90%
    #   memory; 20MB, 10.74%
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        indices = []
        for i, num in enumerate(nums):
            if num == 1:
                indices.append(i)
        for i, idx in enumerate(indices):
            if 0 == i:
                continue
            if idx - indices[i - 1] <= k:
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
