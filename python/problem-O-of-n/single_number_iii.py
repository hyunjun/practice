#   https://leetcode.com/problems/single-number-iii


from collections import Counter
from functools import reduce
from typing import List


class Solution:
    #   runtime; 56ms, 89.36%
    #   memory; 15.5MB, 50.00%
    def singleNumber0(self, nums: List[int]) -> int:
        if nums is None or 0 == len(nums):
            return 0
        return [k for k, v in Counter(nums).items() if v == 1]

    #   https://leetcode.com/explore/featured/card/july-leetcoding-challenge/547/week-4-july-22nd-july-28th/3399
    #   runtime; 96ms, 24.77%
    #   memory; 15.8MB
    def singleNumber1(self, nums: List[int]) -> List[int]:
        if nums is None or 0 == len(nums):
            return 0
        res = set()
        for n in nums:
            if n in res:
                res.remove(n)
            else:
                res.add(n)
        return list(res)

    #   runtime; 88ms, 28.59%
    #   memory; 15.3MB, 81.58%
    def singleNumber(self, nums: List[int]) -> List[int]:
        if nums is None or 0 == len(nums):
            return 0
        nums.sort()
        res = []
        for i, n in enumerate(nums):
            if 0 == i:
                if n != nums[i + 1] and i + 1 < len(nums):
                    res.append(n)
            elif len(nums) - 1 == i:
                if nums[i - 1] != n:
                    res.append(n)
            else:
                if nums[i - 1] != n != nums[i + 1]:
                    res.append(n)
        return res



s = Solution()
data = [([1, 2, 1, 3, 2, 5], [3, 5])
        ]
for nums, expected in data:
    real = s.singleNumber(nums)
    print(f'{nums} expected {expected} real {real} result {sorted(expected) == sorted(real)}')
