#   https://leetcode.com/problems/search-insert-position


from typing import List


class Solution:
    #   runtime; 35ms
    def searchInsert0(self, nums, target):
        l, r = 0, len(nums) - 1

        if target <= nums[l]:
            return l
        if nums[r] < target:
            return r + 1

        while l < r:
            m = ((l + r) // 2)
            if target == nums[m]:
                return m
            elif target < nums[m]:
                r = m - 1
                if nums[r] < target:
                    return m
            else:   #   nums[m] < target
                l = m + 1
                if target <= nums[l]:
                    return l
        return -1

    #   https://leetcode.com/explore/featured/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3356
    #   runtime; 88ms, 6.15%
    #   memory; 14.5MB
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if 0 <= m - 1 and nums[m - 1] < target < nums[m]:
                return m
            if 0 == m and target < nums[m]:
                return m
            if len(nums) - 1 == m and nums[m] < target:
                return m + 1
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1


s = Solution()
data = [([1,3,5,6], 5, 2),
        ([1,3,5,6], 2, 1),
        ([1,3,5,6], 7, 4),
        ([1,3,5,6], 0, 0),
        ]
for nums, target, expect in data:
    real = s.searchInsert(nums, target)
    print(f'{nums} {target} expect {expect} real {real} result {expect == real}')
