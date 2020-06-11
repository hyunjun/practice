#   https://leetcode.com/problems/sort-colors/description/

#   https://leetcode.com/problems/sort-colors/discuss/461375/Python%3A-Single-pass-sorting


from typing import List


class Solution(object):
    #   runtime; 35ms, 7.06%
    def sortColors0(self, nums: List[int]) -> None:
        if nums is None or 0 == len(nums):
            return None

        d = {0:0, 1:0, 2:0}
        for n in nums:
            d[n] += 1
        idx = 0
        for key in range(3):
            i = 0
            while i < d[key]:
                nums[idx] = key
                i += 1
                idx += 1

    #   runtime; 32ms, 78.10%
    #   memory; 12.7MB, 100.00%
    def sortColors1(self, nums: List[int]) -> None:
        if nums is None or 0 == len(nums):
            return None
        z, o, t = 0, 0, 0
        for n in nums:
            if 0 == n:
                z += 1
            elif 1 == n:
                o += 1
            elif 2 == n:
                t += 1
        i, tot = 0, len(nums)
        while i < tot:
            if i < z:
                nums[i] = 0
            elif i < z + o:
                nums[i] = 1
            else:
                nums[i] = 2
            i += 1

    #   https://leetcode.com/explore/featured/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3357
    #   runtime; 28ms, 89.96%
    #   memory; 14MB
    def sortColors(self, nums: List[int]) -> None:
        counts = [0, 0, 0]
        for n in nums:
            counts[n] += 1
        s = 0
        for n, c in enumerate(counts):
            for i in range(s, s + c):
                nums[i] = n
            s += c
        

s = Solution()
data = [([0], [0]),
        ([1, 0], [0, 1]),
        ([0, 0, 1, 1, 2, 1, 2, 0, 2], [0, 0, 0, 1, 1, 1, 2, 2, 2]),
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ]
for nums, expected in data:
    original = nums[:]
    s.sortColors(nums)
    print(f'{original} expected {expected} real {nums} result {expected == nums}')
